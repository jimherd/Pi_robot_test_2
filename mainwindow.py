# This Python file uses the following encoding: utf-8

import sys
import serial
import serial.tools.list_ports
import random
import pyttsx3

from Globals import This_platform, Platform_test

from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QMessageBox, QLabel, QWidget
from PySide6.QtGui     import QAction
from PySide6           import QtWidgets
from PySide6.QtUiTools import QUiLoader
from qt_material       import apply_stylesheet   # added
from ui_form           import Ui_MainWindow

from Command_IO import  Command_IO, ErrorCode, Joints, ServoCommands

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

loader = QUiLoader()                # Set up a loader object
Command_IO = Command_IO(Ui_MainWindow)
ErrorCode = ErrorCode
Platform_test = Platform_test

DEFAULT_PORT    =  9
SPEED_THRESHOLD = 21
NOS_SERVOS      =  8

OFF = 0
ON  = 1

baudrate_options = ["115200", "256000", "9600"]
stepper_cmds_options = ["Relative move", "Absolute move", "Relative move group", "Calibrate"]
stepper_profile_cmds_options = ["fast", "medium", "slow"]
stepper_joints_options = ["Neck"]

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(self.exit_program)
        self.ui.actionAbout.triggered.connect(self.about_message)
        ports = list(serial.tools.list_ports.comports())
        self.ui.info_textEdit.append("log ports")
        for p in ports:
            self.ui.info_textEdit.append(str(p))
            self.ui.serial_port_comboBox.addItem(str(p).split(" ")[0])

        self.error_code_label = QLabel(None)
        self.ui.statusbar.addPermanentWidget(self.error_code_label)
        self.error_code_label.setText("Status code : OK ")
        self.ui.statusbar.addPermanentWidget(QLabel("      "))
        self.serial_port_label = QLabel(None)
        self.ui.statusbar.addPermanentWidget(self.serial_port_label)
        self.serial_port_label.setText("Port : Unknown ")
        self.ui.statusbar.addPermanentWidget(QLabel("  "))
        self.serial_port_baudrate_label = QLabel(None)
        self.ui.statusbar.addPermanentWidget(self.serial_port_baudrate_label)
        self.serial_port_baudrate_label.setText("Baudrate : Unknown  ")
        self.ui.statusbar.addPermanentWidget(QLabel("  "))
        self.platform_label = QLabel(None)
        self.ui.statusbar.addPermanentWidget(self.platform_label)
        self.platform_label.setText("Platform : Unknown ")
        # update servo data tab with custom data (does not include mouth)
        servo_data = ((self.ui.lab_00, -25, self.ui.lab_01, +25, self.ui.slider_00, 0, self.ui.slider_01, 0, 250,
                          self.ui.lab_02, "Left/Right", "Left_Eye"),
                      (self.ui.lab_10, -45, self.ui.lab_11, +45, self.ui.slider_10, 0, self.ui.slider_11, 0, 250,
                          self.ui.lab_12, "Down/Up", "Left_Eye"),
                      (self.ui.lab_20, -25, self.ui.lab_21, +25, self.ui.slider_20, 0, self.ui.slider_21, 0, 250,
                          self.ui.lab_22, "EyeLid", "Left_Eye"),
                      (self.ui.lab_30, -30, self.ui.lab_31, +30, self.ui.slider_30, 0, self.ui.slider_31, 0, 250,
                          self.ui.lab_32, "EyeBrow", "Left_Eye"),
                      (self.ui.lab_40, -25, self.ui.lab_41, +25, self.ui.slider_40, 0, self.ui.slider_41, 0, 250,
                          self.ui.lab_42, "Left/Right", "Left_Eye"),
                      (self.ui.lab_50, -45, self.ui.lab_51, +45, self.ui.slider_50, 0, self.ui.slider_51, 0, 250,
                          self.ui.lab_52, "Down/Up", "Left_Eye"),
                      (self.ui.lab_60, -25, self.ui.lab_61, +25, self.ui.slider_60, 0, self.ui.slider_61, 0, 250,
                          self.ui.lab_62, "EyeLid", "Left_Eye"),
                      (self.ui.lab_70, -30, self.ui.lab_71, +30, self.ui.slider_70, 0, self.ui.slider_71, 0, 250,
                          self.ui.lab_72, "EyeBrow", "Left_Eye"),
                          )
    # Load servo tab with configuration data
        for index in range(NOS_SERVOS):
            # slider max/min labels
            servo_data[index][0].setText(str(servo_data[index][1]))
            servo_data[index][2].setText(str(servo_data[index][3]))
            # position slider max/min values
            servo_data[index][4].setMinimum(servo_data[index][1])
            servo_data[index][4].setMaximum(servo_data[index][3])
            # speed max/min values
            servo_data[index][6].setMinimum(servo_data[index][7])
            servo_data[index][6].setMaximum(servo_data[index][8])
            # item name
            servo_data[index][9].setText(servo_data[index][10])

        # load stepper motor tab with configuration data
        self.ui.comboBox.addItems(stepper_joints_options)
        self.ui.comboBox_2.addItems(stepper_profile_cmds_options)
        self.ui.pushButton_2.clicked.connect(self.go_stepper_cmd)

        self.about_msg = QMessageBox(self)
        serial_port = None
        serial_baud_rate = None
        engine = pyttsx3.init()
        engine.say('Hello jim.')
        engine.runAndWait()
        Platform_test.check_platform(self)
        self.platform_label.setText("Platform: " + Platform_test.get_platform_name(self))

    # route SERVO go buttons to a single slot with and added button code
        self.ui.button_00.clicked.connect(lambda x:self.go_servo_cmd(Joints.LEFT_EYE_RIGHT_LEFT))
        self.ui.button_10.clicked.connect(lambda x:self.go_servo_cmd(Joints.LEFT_EYE_UP_DOWN))
        self.ui.button_20.clicked.connect(lambda x:self.go_servo_cmd(Joints.LEFT_EYE_LID))
        self.ui.button_30.clicked.connect(lambda x:self.go_servo_cmd(Joints.LEFT_EYE_BROW))
        self.ui.button_40.clicked.connect(lambda x:self.go_servo_cmd(Joints.RIGHT_EYE_RIGHT_LEFT))
        self.ui.button_50.clicked.connect(lambda x:self.go_servo_cmd(Joints.RIGHT_EYE_UP_DOWN))
        self.ui.button_60.clicked.connect(lambda x:self.go_servo_cmd(Joints.RIGHT_EYE_LID))
        self.ui.button_70.clicked.connect(lambda x:self.go_servo_cmd(Joints.RIGHT_EYE_BROW))
        self.ui.button_80.clicked.connect(self.Mouth_on_off)
        self_mouth_state = OFF

# End of initialoisation code
#
# System functions
#
    def exit_program(self):
        self.ui.info_textEdit.append("exit test")
        QApplication.quit()

    def about_message(self):
        self.about_msg.about(self, "About", "Pi the Robot test program")

    def open_serial_port(self):
        self.ui.info_textEdit.append("about to open port")
        serial_port = self.ui.serial_port_comboBox.currentText()
        serial_baud_rate = int(self.ui.baudrates_comboBox.currentText())
        status = Command_IO.open_port(MainWindow, serial_port, serial_baud_rate)
        if (status != ErrorCode.OK):
            self.ui.info_textEdit.append("Open fail")
            self.log_status(status)
        else:
            self.ui.info_textEdit.append("Open sucess")
            self.ui.run_servos_tab.setEnabled(True)
            self.serial_port_label.setText("Port: " + serial_port)
            self.serial_port_baudrate_label.setText("Baudrate: " + str(serial_baud_rate))

    def close_serial_port(self):
        Command_IO.close_port()
        self.ui.run_servos_tab.setEnabled(False)
        self.ui.info_textEdit.append("Serial port closed")
        self.serial_port_label.setText("Port : Unknown")
        self.serial_port_baudrate_label.setText("Baudrate : Unknown  ")

    def createStatusBar(self):
        self.ui.statusbar.showMessage("Ready")

    def log_message(self, message):
        self.ui.info_textEdit.append(str(message))

    def log_status(self, error_code):
        self.error_code_label.setText("Status code : " + str(error_code))

    def ping(self):
        self.cmd_string = "ping 0 " + str(random.randint(1,98)) + "\n"
        self.log_message(self.cmd_string)
        first_val = 0

        status =  Command_IO.do_command(self.cmd_string, first_val)
        print(status)
        self.log_message(Command_IO.reply_string)
        return status

    def go_servo_cmd(self, joint_code):
        match joint_code:
            case Joints.LEFT_EYE_RIGHT_LEFT:
                servo_position = self.ui.slider_00.value()
                servo_speed = self.ui.slider_01.value()
                servo_group = self.ui.checkbox_00.isChecked()
            case Joints.LEFT_EYE_UP_DOWN:
                servo_position = self.ui.slider_10.value()
                servo_speed = self.ui.slider_11.value()
                servo_group = self.ui.checkbox_10.isChecked()
            case Joints.LEFT_EYE_LID:
                servo_position = self.ui.slider_20.value()
                servo_speed = self.ui.slider_21.value()
                servo_group = self.ui.checkbox_20.isChecked()
            case Joints.LEFT_EYE_BROW:
                servo_position = self.ui.slider_30.value()
                servo_speed = self.ui.slider_31.value()
                servo_group = self.ui.checkbox_30.isChecked()
            case Joints.RIGHT_EYE_RIGHT_LEFT:
                servo_position = self.ui.slider_40.value()
                servo_speed = self.ui.slider_41.value()
                servo_group = self.ui.checkbox_40.isChecked()
            case Joints.RIGHT_EYE_UP_DOWN:
                servo_position = self.ui.slider_50.value()
                servo_speed = self.ui.slider_51.value()
                servo_group = self.ui.checkbox_50.isChecked()
            case Joints.RIGHT_EYE_LID:
                servo_position = self.ui.slider_60.value()
                servo_speed = self.ui.slider_61.value()
                servo_group = self.ui.checkbox_60.isChecked()
            case Joints.RIGHT_EYE_BROW:
                servo_position = self.ui.slider_70.value()
                servo_speed = self.ui.slider_71.value()
                servo_group = self.ui.checkbox_70.isChecked()
        status = self.Execute_servo_cmd(joint_code, servo_position, servo_speed, servo_group)
        self.log_status(status)

    def go_stepper_cmd(self):
        stepper_no = self.ui.comboBox.currentIndex()
        stepper_speed_profile = self.ui.comboBox_2.currentIndex()
        stepper_step_value = self.ui.slider_step_value()
        stepper_group = self.ui.checkBox.isChecked()
        stepper_rel = self.ui.radioButton_1.isChecked()
        stepper_abs = self.ui.radioButton_2.isChecked()
        stepper_calibrate = self.ui.radioButton.isChecked()

    def Execute_servo_cmd(self, joint, position, speed, group):
        # select type of move command
        if ((group == False) and (speed < SPEED_THRESHOLD)):
            servo_cmd = ServoCommands.ABS_MOVE
        elif ((group == True) and (speed < SPEED_THRESHOLD)):
            servo_cmd = ServoCommands.ABS_MOVE_SYNC
        elif ((group == False) and (speed >= SPEED_THRESHOLD)):
            servo_cmd = ServoCommands.SPEED_MOVE
        else:
            servo_cmd = ServoCommands.SPEED_MOVE_SYNC
        # construct appropriate command string
        if (speed < SPEED_THRESHOLD):
            self.cmd_string =(f"servo {DEFAULT_PORT} {servo_cmd} {joint} {position}\n")
        else:
            self.cmd_string =(f"servo {DEFAULT_PORT} {servo_cmd} {joint} {position} {speed}\n")
        # log command for debug
        self.log_message(self.cmd_string)
        # execute servo move command
        first_val = 0
        status =  Command_IO.do_command(self.cmd_string, first_val)
        print(status)
        # log reply string
        self.log_message(Command_IO.reply_string)
        return status

    def Mouth_on_off(self):
        if (self.ui.checkbox_80.ischecked() == False):
            servo_cmd = ServoCommands.ABS_MOVE
        else:
            servo_cmd = ServoCommands.ABS_MOVE_SYNC

        if (self.mouth_state == OFF):
            self.cmd_string = (f"servo {DEFAULT_PORT} {servo_cmd} joints.Mouth +45\n")   # turn ON
            self.ui.button_80.setText("Stop")
            self.mouth = ON
        else:
            self.cmd_string = (f"servo {DEFAULT_PORT} {servo_cmd} joints.Mouth -45\n")   # turn OFF
            self.ui.button_80.setText("Start")
            self.mouth = OFF

#
# Main call
#
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(window, theme='dark_blue_custom.xml')
    window.showMaximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
