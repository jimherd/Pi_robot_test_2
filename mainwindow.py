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

from Command_IO import  Command_IO, ErrorCode, Joints

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

loader = QUiLoader()                # Set up a loader object
Command_IO = Command_IO(Ui_MainWindow)
ErrorCode = ErrorCode
Platform_test = Platform_test

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

        self.about_msg = QMessageBox(self)
        serial_port = None
        serial_baud_rate = None
        engine = pyttsx3.init()
        engine.say('Hello jim.')
        engine.runAndWait()
        Platform_test.check_platform(self)
        self.platform_label.setText("Platform: " + Platform_test.get_platform_name(self))

    # route SERVO go button to a single slot with and added button code
        self.ui.Left_LR_go_button.clicked.connect(lambda x:self.go_button_pushed(Joints.LEFT_EYE_RIGHT_LEFT))
        self.ui.Left_UD_go_button.clicked.connect(lambda x:self.go_button_pushed(Joints.LEFT_EYE_UP_DOWN))
        self.ui.Left_eyelid_go_button.clicked.connect(lambda x:self.go_button_pushed(Joints.LEFT_EYE_LID))
        self.ui.Left_eyebrow_go_button.clicked.connect(lambda x:self.go_button_pushed(Joints.LEFT_EYE_BROW))
        self.ui.Right_LR_go_button.clicked.connect(lambda x:self.go_button_pushed(Joints.RIGHT_EYE_UP_DOWN))
        self.ui.Right_UD_go_button.clicked.connect(lambda x:self.go_button_pushed(Joints.RIGHT_EYE_LEFT_RIGHT))
        self.ui.Right_eyelid_go_button.clicked.connect(lambda x:self.go_button_pushed(Joints.RIGHT_EYE_LID))
        self.ui.Right_eyebrow_go_button.clicked.connect(lambda x:self.go_button_pushed(Joints.RIGHT_EYE_BROW))


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

    def go_button_pushed(self, joint_code):
        match joint_code:
            case Joints.LEFT_EYE_RIGHT_LEFT:
                servo_position = self.ui.Left_LR_position_slider.value()
                servo_speed = self.ui.Left_LR_speed_slider.value()
                servo_group = self.ui.Left_LR_group_checkbox.isChecked()
            case Joints.LEFT_EYE_UP_DOWN:
                servo_position = self.ui.Left_UD_position_slider.value()
                servo_speed = self.ui.Left_UD_speed_slider.value()
                servo_group = self.ui.Left_UD_group_checkbox.isChecked()
            case Joints.LEFT_EYE_LID:
                servo_position = self.ui.Left_eyelid_position_slider.value()
                servo_speed = self.ui.Left_eyelid_speed_slider.value()
                servo_group = self.ui.Left_eyelid_group_checkbox.isChecked()
            case Joints.LEFT_EYE_BROW:
                servo_position = self.ui.Left_eyebrow_position_slider.value()
                servo_speed = self.ui.Left_eyebrow_speed_slider.value()
                servo_group = self.ui.Left_eyebrow_group_checkbox.isChecked()

            case Joints.RIGHT_EYE_RIGHT_LEFT:
                servo_position = self.ui.Right_LR_position_slider.value()
                servo_speed = self.ui.Right_LR_speed_slider.value()
                servo_group = self.ui.Right_LR_group_checkbox.isChecked()
            case Joints.RIGHT_EYE_UP_DOWN:
                servo_position = self.ui.Right_UD_position_slider.value()
                servo_speed = self.ui.Right_UD_speed_slider.value()
                servo_group = self.ui.Right_UD_group_checkbox.isChecked()
            case Joints.RIGHT_EYE_LID:
                servo_position = self.ui.Right_eyelid_position_slider.value()
                servo_speed = self.ui.Right_eyelid_speed_slider.value()
                servo_group = self.ui.Right_eyelid_group_checkbox.isChecked()
            case Joints.RIGHT_EYE_BROW:
                servo_position = self.ui.Right_eyebrow_position_slider.value()
                servo_speed = self.ui.Right_eyebrow_speed_slider.value()
                servo_group = self.ui.Right_eyebrow_group_checkbox.isChecked()
        self.Execute_servo_cmd(joint_code, servo_position, servo_speed, servo_group)


    def Execute_servo_cmd(self, joint, position, speed, group):
        print(position)
        print(speed)
        print(group)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(window, theme='dark_blue_custom.xml')
    window.showMaximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
