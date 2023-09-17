# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1309, 1200)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setCheckable(False)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(435, 35, 886, 741))
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.set_serial_port_tab = QWidget()
        self.set_serial_port_tab.setObjectName(u"set_serial_port_tab")
        self.set_serial_port_tab.setEnabled(True)
        self.widget = QWidget(self.set_serial_port_tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 5, 796, 371))
        self.serial_port_comboBox = QComboBox(self.widget)
        self.serial_port_comboBox.setObjectName(u"serial_port_comboBox")
        self.serial_port_comboBox.setGeometry(QRect(40, 75, 116, 24))
        font = QFont()
        font.setPointSize(12)
        self.serial_port_comboBox.setFont(font)
        self.baudrates_comboBox = QComboBox(self.widget)
        self.baudrates_comboBox.addItem("")
        self.baudrates_comboBox.addItem("")
        self.baudrates_comboBox.setObjectName(u"baudrates_comboBox")
        self.baudrates_comboBox.setGeometry(QRect(200, 75, 111, 24))
        self.baudrates_comboBox.setFont(font)
        self.baudrates_comboBox.setEditable(False)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 96, 16))
        self.label.setFont(font)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(215, 50, 101, 16))
        self.label_8.setFont(font)
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(75, 130, 196, 141))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.open_serial_port = QPushButton(self.layoutWidget)
        self.open_serial_port.setObjectName(u"open_serial_port")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setKerning(False)
        self.open_serial_port.setFont(font1)

        self.verticalLayout.addWidget(self.open_serial_port)

        self.close_serial_port = QPushButton(self.layoutWidget)
        self.close_serial_port.setObjectName(u"close_serial_port")
        self.close_serial_port.setFont(font)
        self.close_serial_port.setFlat(False)

        self.verticalLayout.addWidget(self.close_serial_port)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 285, 106, 41))
        self.pushButton.setFont(font)
        self.tabWidget.addTab(self.set_serial_port_tab, "")
        self.run_servos_tab = QWidget()
        self.run_servos_tab.setObjectName(u"run_servos_tab")
        self.run_servos_tab.setEnabled(False)
        self.layoutWidget1 = QWidget(self.run_servos_tab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(15, 5, 759, 276))
        font2 = QFont()
        font2.setBold(False)
        self.layoutWidget1.setFont(font2)
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.line_19 = QFrame(self.layoutWidget1)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShadow(QFrame.Plain)
        self.line_19.setLineWidth(3)
        self.line_19.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_19, 6, 7, 1, 1)

        self.line_25 = QFrame(self.layoutWidget1)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShadow(QFrame.Plain)
        self.line_25.setLineWidth(3)
        self.line_25.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_25, 7, 0, 1, 9)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.line_13 = QFrame(self.layoutWidget1)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShadow(QFrame.Plain)
        self.line_13.setLineWidth(3)
        self.line_13.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_13, 0, 7, 1, 1)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.Left_eyebrow_group_checkbox = QCheckBox(self.layoutWidget1)
        self.Left_eyebrow_group_checkbox.setObjectName(u"Left_eyebrow_group_checkbox")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        self.Left_eyebrow_group_checkbox.setFont(font4)
        self.Left_eyebrow_group_checkbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_eyebrow_group_checkbox, 8, 8, 1, 1)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.line_9 = QFrame(self.layoutWidget1)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_9, 2, 4, 1, 1)

        self.line_23 = QFrame(self.layoutWidget1)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShadow(QFrame.Plain)
        self.line_23.setLineWidth(3)
        self.line_23.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_23, 8, 4, 1, 1)

        self.line_6 = QFrame(self.layoutWidget1)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_6, 4, 7, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_18 = QLabel(self.layoutWidget1)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_18)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.label_19 = QLabel(self.layoutWidget1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_19)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.label_20 = QLabel(self.layoutWidget1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_20)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.Left_UD_position_slider = QSlider(self.layoutWidget1)
        self.Left_UD_position_slider.setObjectName(u"Left_UD_position_slider")
        self.Left_UD_position_slider.setMinimum(-45)
        self.Left_UD_position_slider.setMaximum(45)
        self.Left_UD_position_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.Left_UD_position_slider)


        self.gridLayout.addLayout(self.verticalLayout_5, 4, 2, 1, 1)

        self.line_3 = QFrame(self.layoutWidget1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_3, 2, 1, 1, 1)

        self.Left_UD_group_checkbox = QCheckBox(self.layoutWidget1)
        self.Left_UD_group_checkbox.setObjectName(u"Left_UD_group_checkbox")
        self.Left_UD_group_checkbox.setFont(font4)
        self.Left_UD_group_checkbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_UD_group_checkbox, 4, 8, 1, 1)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_15)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.Left_LR_position_slider = QSlider(self.layoutWidget1)
        self.Left_LR_position_slider.setObjectName(u"Left_LR_position_slider")
        self.Left_LR_position_slider.setMinimum(-60)
        self.Left_LR_position_slider.setMaximum(60)
        self.Left_LR_position_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.Left_LR_position_slider)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 2, 1, 1)

        self.line_4 = QFrame(self.layoutWidget1)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_4, 4, 1, 1, 1)

        self.line_14 = QFrame(self.layoutWidget1)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShadow(QFrame.Plain)
        self.line_14.setLineWidth(3)
        self.line_14.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_14, 0, 4, 1, 1)

        self.line_15 = QFrame(self.layoutWidget1)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShadow(QFrame.Plain)
        self.line_15.setLineWidth(3)
        self.line_15.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_15, 5, 0, 1, 11)

        self.line_11 = QFrame(self.layoutWidget1)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_11, 0, 1, 1, 1)

        self.Left_LR_group_checkbox = QCheckBox(self.layoutWidget1)
        self.Left_LR_group_checkbox.setObjectName(u"Left_LR_group_checkbox")
        self.Left_LR_group_checkbox.setFont(font4)
        self.Left_LR_group_checkbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_LR_group_checkbox, 2, 8, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.line_2 = QFrame(self.layoutWidget1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.HLine)

        self.horizontalLayout_6.addWidget(self.line_2)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.line_21 = QFrame(self.layoutWidget1)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShadow(QFrame.Plain)
        self.line_21.setLineWidth(3)
        self.line_21.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_21, 8, 9, 1, 1)

        self.line_7 = QFrame(self.layoutWidget1)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_7, 2, 7, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_16)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_17)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.Left_LR_speed_slider = QSlider(self.layoutWidget1)
        self.Left_LR_speed_slider.setObjectName(u"Left_LR_speed_slider")
        self.Left_LR_speed_slider.setMinimum(0)
        self.Left_LR_speed_slider.setMaximum(30)
        self.Left_LR_speed_slider.setOrientation(Qt.Horizontal)
        self.Left_LR_speed_slider.setInvertedAppearance(True)
        self.Left_LR_speed_slider.setInvertedControls(False)

        self.verticalLayout_4.addWidget(self.Left_LR_speed_slider)


        self.gridLayout.addLayout(self.verticalLayout_4, 2, 6, 1, 1)

        self.Left_eyelid_go_button = QPushButton(self.layoutWidget1)
        self.Left_eyelid_go_button.setObjectName(u"Left_eyelid_go_button")
        self.Left_eyelid_go_button.setFont(font4)
        self.Left_eyelid_go_button.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_eyelid_go_button, 6, 10, 1, 1)

        self.line_22 = QFrame(self.layoutWidget1)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShadow(QFrame.Plain)
        self.line_22.setLineWidth(3)
        self.line_22.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_22, 8, 7, 1, 1)

        self.line = QFrame(self.layoutWidget1)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 11)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_31 = QLabel(self.layoutWidget1)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_31)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)

        self.label_32 = QLabel(self.layoutWidget1)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_32)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.Left_eyebrow_speed_slider_2 = QSlider(self.layoutWidget1)
        self.Left_eyebrow_speed_slider_2.setObjectName(u"Left_eyebrow_speed_slider_2")
        self.Left_eyebrow_speed_slider_2.setMinimum(0)
        self.Left_eyebrow_speed_slider_2.setMaximum(30)
        self.Left_eyebrow_speed_slider_2.setOrientation(Qt.Horizontal)
        self.Left_eyebrow_speed_slider_2.setInvertedAppearance(True)
        self.Left_eyebrow_speed_slider_2.setInvertedControls(False)

        self.verticalLayout_10.addWidget(self.Left_eyebrow_speed_slider_2)


        self.gridLayout.addLayout(self.verticalLayout_10, 8, 6, 1, 1)

        self.line_20 = QFrame(self.layoutWidget1)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShadow(QFrame.Plain)
        self.line_20.setLineWidth(3)
        self.line_20.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_20, 6, 9, 1, 1)

        self.Left_eyebrow_spinbox = QSpinBox(self.layoutWidget1)
        self.Left_eyebrow_spinbox.setObjectName(u"Left_eyebrow_spinbox")
        self.Left_eyebrow_spinbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Left_eyebrow_spinbox.setMinimum(-45)
        self.Left_eyebrow_spinbox.setMaximum(45)

        self.gridLayout.addWidget(self.Left_eyebrow_spinbox, 8, 3, 1, 1)

        self.Left_LR_spinbox = QSpinBox(self.layoutWidget1)
        self.Left_LR_spinbox.setObjectName(u"Left_LR_spinbox")
        self.Left_LR_spinbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Left_LR_spinbox.setMinimum(-60)
        self.Left_LR_spinbox.setMaximum(60)

        self.gridLayout.addWidget(self.Left_LR_spinbox, 2, 3, 1, 1)

        self.Left_eyebrow_go_button = QPushButton(self.layoutWidget1)
        self.Left_eyebrow_go_button.setObjectName(u"Left_eyebrow_go_button")
        self.Left_eyebrow_go_button.setFont(font4)
        self.Left_eyebrow_go_button.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_eyebrow_go_button, 8, 10, 1, 1)

        self.Left_UD_go_button = QPushButton(self.layoutWidget1)
        self.Left_UD_go_button.setObjectName(u"Left_UD_go_button")
        self.Left_UD_go_button.setFont(font4)
        self.Left_UD_go_button.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_UD_go_button, 4, 10, 1, 1)

        self.Left_UD_spinbox = QSpinBox(self.layoutWidget1)
        self.Left_UD_spinbox.setObjectName(u"Left_UD_spinbox")
        self.Left_UD_spinbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Left_UD_spinbox.setMinimum(-45)
        self.Left_UD_spinbox.setMaximum(45)

        self.gridLayout.addWidget(self.Left_UD_spinbox, 4, 3, 1, 1)

        self.line_10 = QFrame(self.layoutWidget1)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_10, 2, 9, 1, 1)

        self.Left_eyelid_spinbox = QSpinBox(self.layoutWidget1)
        self.Left_eyelid_spinbox.setObjectName(u"Left_eyelid_spinbox")
        self.Left_eyelid_spinbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Left_eyelid_spinbox.setMinimum(-45)
        self.Left_eyelid_spinbox.setMaximum(45)

        self.gridLayout.addWidget(self.Left_eyelid_spinbox, 6, 3, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_28 = QLabel(self.layoutWidget1)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_28)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)

        self.label_29 = QLabel(self.layoutWidget1)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_29)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)

        self.label_30 = QLabel(self.layoutWidget1)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_30)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.Left_eyebrow_position_slider = QSlider(self.layoutWidget1)
        self.Left_eyebrow_position_slider.setObjectName(u"Left_eyebrow_position_slider")
        self.Left_eyebrow_position_slider.setMinimum(-45)
        self.Left_eyebrow_position_slider.setMaximum(45)
        self.Left_eyebrow_position_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.Left_eyebrow_position_slider)


        self.gridLayout.addLayout(self.verticalLayout_9, 8, 2, 1, 1)

        self.line_5 = QFrame(self.layoutWidget1)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_5, 4, 9, 1, 1)

        self.line_8 = QFrame(self.layoutWidget1)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_8, 4, 4, 1, 1)

        self.Left_eyelid_group_checkbox = QCheckBox(self.layoutWidget1)
        self.Left_eyelid_group_checkbox.setObjectName(u"Left_eyelid_group_checkbox")
        self.Left_eyelid_group_checkbox.setFont(font4)
        self.Left_eyelid_group_checkbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_eyelid_group_checkbox, 6, 8, 1, 1)

        self.line_16 = QFrame(self.layoutWidget1)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShadow(QFrame.Plain)
        self.line_16.setLineWidth(3)
        self.line_16.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_16, 1, 0, 1, 11)

        self.line_24 = QFrame(self.layoutWidget1)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShadow(QFrame.Plain)
        self.line_24.setLineWidth(3)
        self.line_24.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_24, 8, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_23 = QLabel(self.layoutWidget1)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_23)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_12)

        self.label_24 = QLabel(self.layoutWidget1)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_24)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)

        self.label_25 = QLabel(self.layoutWidget1)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_25)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.Left_eyelid_position_slider = QSlider(self.layoutWidget1)
        self.Left_eyelid_position_slider.setObjectName(u"Left_eyelid_position_slider")
        self.Left_eyelid_position_slider.setMinimum(-45)
        self.Left_eyelid_position_slider.setMaximum(45)
        self.Left_eyelid_position_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.Left_eyelid_position_slider)


        self.gridLayout.addLayout(self.verticalLayout_7, 6, 2, 1, 1)

        self.line_17 = QFrame(self.layoutWidget1)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShadow(QFrame.Plain)
        self.line_17.setLineWidth(3)
        self.line_17.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_17, 6, 1, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_26 = QLabel(self.layoutWidget1)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_26)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)

        self.label_27 = QLabel(self.layoutWidget1)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_27)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.Left_eyelid_speed_slider = QSlider(self.layoutWidget1)
        self.Left_eyelid_speed_slider.setObjectName(u"Left_eyelid_speed_slider")
        self.Left_eyelid_speed_slider.setMinimum(0)
        self.Left_eyelid_speed_slider.setMaximum(30)
        self.Left_eyelid_speed_slider.setOrientation(Qt.Horizontal)
        self.Left_eyelid_speed_slider.setInvertedAppearance(True)
        self.Left_eyelid_speed_slider.setInvertedControls(False)

        self.verticalLayout_8.addWidget(self.Left_eyelid_speed_slider)


        self.gridLayout.addLayout(self.verticalLayout_8, 6, 6, 1, 1)

        self.line_12 = QFrame(self.layoutWidget1)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShadow(QFrame.Plain)
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_12, 0, 9, 1, 1)

        self.line_18 = QFrame(self.layoutWidget1)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShadow(QFrame.Plain)
        self.line_18.setLineWidth(3)
        self.line_18.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_18, 6, 4, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_21 = QLabel(self.layoutWidget1)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_21)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)

        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_22)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.Left_UD_speed_slider = QSlider(self.layoutWidget1)
        self.Left_UD_speed_slider.setObjectName(u"Left_UD_speed_slider")
        self.Left_UD_speed_slider.setMinimum(0)
        self.Left_UD_speed_slider.setMaximum(30)
        self.Left_UD_speed_slider.setOrientation(Qt.Horizontal)
        self.Left_UD_speed_slider.setInvertedAppearance(True)
        self.Left_UD_speed_slider.setInvertedControls(False)

        self.verticalLayout_6.addWidget(self.Left_UD_speed_slider)


        self.gridLayout.addLayout(self.verticalLayout_6, 4, 6, 1, 1)

        self.Left_LR_go_button = QPushButton(self.layoutWidget1)
        self.Left_LR_go_button.setObjectName(u"Left_LR_go_button")
        self.Left_LR_go_button.setFont(font4)
        self.Left_LR_go_button.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_LR_go_button, 2, 10, 1, 1)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 6, 1, 1)

        self.label_56 = QLabel(self.layoutWidget1)
        self.label_56.setObjectName(u"label_56")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        self.label_56.setFont(font5)
        self.label_56.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 0)")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_56, 0, 0, 1, 1)

        self.Left_UD_go_button.raise_()
        self.label_6.raise_()
        self.Left_UD_group_checkbox.raise_()
        self.line_22.raise_()
        self.Left_LR_go_button.raise_()
        self.Left_eyelid_go_button.raise_()
        self.Left_eyebrow_go_button.raise_()
        self.label_7.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_16.raise_()
        self.line_20.raise_()
        self.line_19.raise_()
        self.Left_eyebrow_spinbox.raise_()
        self.line_11.raise_()
        self.Left_LR_spinbox.raise_()
        self.Left_LR_group_checkbox.raise_()
        self.line_8.raise_()
        self.line_4.raise_()
        self.line_12.raise_()
        self.line_5.raise_()
        self.line_21.raise_()
        self.line_15.raise_()
        self.line_24.raise_()
        self.line_18.raise_()
        self.Left_eyelid_group_checkbox.raise_()
        self.line_23.raise_()
        self.Left_eyelid_spinbox.raise_()
        self.Left_eyebrow_group_checkbox.raise_()
        self.line_14.raise_()
        self.line.raise_()
        self.Left_UD_spinbox.raise_()
        self.line_17.raise_()
        self.line_13.raise_()
        self.line_10.raise_()
        self.line_3.raise_()
        self.line_9.raise_()
        self.label_3.raise_()
        self.line_25.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_56.raise_()
        self.layoutWidget_2 = QWidget(self.run_servos_tab)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(15, 290, 759, 276))
        self.layoutWidget_2.setFont(font2)
        self.gridLayout_2 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_26 = QFrame(self.layoutWidget_2)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShadow(QFrame.Plain)
        self.line_26.setLineWidth(3)
        self.line_26.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_26, 6, 7, 1, 1)

        self.line_27 = QFrame(self.layoutWidget_2)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShadow(QFrame.Plain)
        self.line_27.setLineWidth(3)
        self.line_27.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_27, 7, 0, 1, 9)

        self.label_10 = QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 6, 0, 1, 1)

        self.line_28 = QFrame(self.layoutWidget_2)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShadow(QFrame.Plain)
        self.line_28.setLineWidth(3)
        self.line_28.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_28, 0, 7, 1, 1)

        self.label_12 = QLabel(self.layoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 8, 0, 1, 1)

        self.Right_eyebrow_group_checkbox = QCheckBox(self.layoutWidget_2)
        self.Right_eyebrow_group_checkbox.setObjectName(u"Right_eyebrow_group_checkbox")
        self.Right_eyebrow_group_checkbox.setFont(font4)
        self.Right_eyebrow_group_checkbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.Right_eyebrow_group_checkbox, 8, 8, 1, 1)

        self.label_14 = QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)

        self.line_29 = QFrame(self.layoutWidget_2)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShadow(QFrame.Plain)
        self.line_29.setLineWidth(3)
        self.line_29.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_29, 2, 4, 1, 1)

        self.line_30 = QFrame(self.layoutWidget_2)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShadow(QFrame.Plain)
        self.line_30.setLineWidth(3)
        self.line_30.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_30, 8, 4, 1, 1)

        self.line_31 = QFrame(self.layoutWidget_2)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShadow(QFrame.Plain)
        self.line_31.setLineWidth(3)
        self.line_31.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_31, 4, 7, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_33 = QLabel(self.layoutWidget_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_33)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_18)

        self.label_34 = QLabel(self.layoutWidget_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_34)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_19)

        self.label_35 = QLabel(self.layoutWidget_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_35.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_35)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.Right_UD_position_slider = QSlider(self.layoutWidget_2)
        self.Right_UD_position_slider.setObjectName(u"Right_UD_position_slider")
        self.Right_UD_position_slider.setMinimum(-45)
        self.Right_UD_position_slider.setMaximum(45)
        self.Right_UD_position_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_11.addWidget(self.Right_UD_position_slider)


        self.gridLayout_2.addLayout(self.verticalLayout_11, 4, 2, 1, 1)

        self.line_32 = QFrame(self.layoutWidget_2)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShadow(QFrame.Plain)
        self.line_32.setLineWidth(3)
        self.line_32.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_32, 2, 1, 1, 1)

        self.Left_UD_group_checkbox_5 = QCheckBox(self.layoutWidget_2)
        self.Left_UD_group_checkbox_5.setObjectName(u"Left_UD_group_checkbox_5")
        self.Left_UD_group_checkbox_5.setFont(font4)
        self.Left_UD_group_checkbox_5.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.Left_UD_group_checkbox_5, 4, 8, 1, 1)

        self.label_36 = QLabel(self.layoutWidget_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_36, 0, 2, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_37 = QLabel(self.layoutWidget_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_37)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_20)

        self.label_38 = QLabel(self.layoutWidget_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_38)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_21)

        self.label_39 = QLabel(self.layoutWidget_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_39)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.Right_LR_position_slider = QSlider(self.layoutWidget_2)
        self.Right_LR_position_slider.setObjectName(u"Right_LR_position_slider")
        self.Right_LR_position_slider.setMinimum(-60)
        self.Right_LR_position_slider.setMaximum(60)
        self.Right_LR_position_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_12.addWidget(self.Right_LR_position_slider)


        self.gridLayout_2.addLayout(self.verticalLayout_12, 2, 2, 1, 1)

        self.line_33 = QFrame(self.layoutWidget_2)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShadow(QFrame.Plain)
        self.line_33.setLineWidth(3)
        self.line_33.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_33, 4, 1, 1, 1)

        self.line_34 = QFrame(self.layoutWidget_2)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShadow(QFrame.Plain)
        self.line_34.setLineWidth(3)
        self.line_34.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_34, 0, 4, 1, 1)

        self.line_35 = QFrame(self.layoutWidget_2)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShadow(QFrame.Plain)
        self.line_35.setLineWidth(3)
        self.line_35.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_35, 5, 0, 1, 11)

        self.line_36 = QFrame(self.layoutWidget_2)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShadow(QFrame.Plain)
        self.line_36.setLineWidth(3)
        self.line_36.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_36, 0, 1, 1, 1)

        self.Right_LR_group_checkbox_2 = QCheckBox(self.layoutWidget_2)
        self.Right_LR_group_checkbox_2.setObjectName(u"Right_LR_group_checkbox_2")
        self.Right_LR_group_checkbox_2.setFont(font4)
        self.Right_LR_group_checkbox_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.Right_LR_group_checkbox_2, 2, 8, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_40 = QLabel(self.layoutWidget_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)
        self.label_40.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_40)

        self.line_37 = QFrame(self.layoutWidget_2)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShadow(QFrame.Plain)
        self.line_37.setLineWidth(3)
        self.line_37.setFrameShape(QFrame.HLine)

        self.horizontalLayout_17.addWidget(self.line_37)


        self.gridLayout_2.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)

        self.line_38 = QFrame(self.layoutWidget_2)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShadow(QFrame.Plain)
        self.line_38.setLineWidth(3)
        self.line_38.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_38, 8, 9, 1, 1)

        self.line_39 = QFrame(self.layoutWidget_2)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShadow(QFrame.Plain)
        self.line_39.setLineWidth(3)
        self.line_39.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_39, 2, 7, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_41 = QLabel(self.layoutWidget_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_41)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_22)

        self.label_42 = QLabel(self.layoutWidget_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_42)


        self.verticalLayout_13.addLayout(self.horizontalLayout_18)

        self.Right_LR_speed_slider = QSlider(self.layoutWidget_2)
        self.Right_LR_speed_slider.setObjectName(u"Right_LR_speed_slider")
        self.Right_LR_speed_slider.setMinimum(0)
        self.Right_LR_speed_slider.setMaximum(30)
        self.Right_LR_speed_slider.setOrientation(Qt.Horizontal)
        self.Right_LR_speed_slider.setInvertedAppearance(True)
        self.Right_LR_speed_slider.setInvertedControls(False)

        self.verticalLayout_13.addWidget(self.Right_LR_speed_slider)


        self.gridLayout_2.addLayout(self.verticalLayout_13, 2, 6, 1, 1)

        self.Right_eyelid_go_button = QPushButton(self.layoutWidget_2)
        self.Right_eyelid_go_button.setObjectName(u"Right_eyelid_go_button")
        self.Right_eyelid_go_button.setFont(font4)
        self.Right_eyelid_go_button.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.Right_eyelid_go_button, 6, 10, 1, 1)

        self.line_40 = QFrame(self.layoutWidget_2)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShadow(QFrame.Plain)
        self.line_40.setLineWidth(3)
        self.line_40.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_40, 8, 7, 1, 1)

        self.line_41 = QFrame(self.layoutWidget_2)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setFrameShadow(QFrame.Plain)
        self.line_41.setLineWidth(3)
        self.line_41.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_41, 3, 0, 1, 11)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_43 = QLabel(self.layoutWidget_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_43)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_23)

        self.label_44 = QLabel(self.layoutWidget_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_44.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_44)


        self.verticalLayout_14.addLayout(self.horizontalLayout_19)

        self.Right_eyebrow_speed_slider = QSlider(self.layoutWidget_2)
        self.Right_eyebrow_speed_slider.setObjectName(u"Right_eyebrow_speed_slider")
        self.Right_eyebrow_speed_slider.setMinimum(0)
        self.Right_eyebrow_speed_slider.setMaximum(30)
        self.Right_eyebrow_speed_slider.setOrientation(Qt.Horizontal)
        self.Right_eyebrow_speed_slider.setInvertedAppearance(True)
        self.Right_eyebrow_speed_slider.setInvertedControls(False)

        self.verticalLayout_14.addWidget(self.Right_eyebrow_speed_slider)


        self.gridLayout_2.addLayout(self.verticalLayout_14, 8, 6, 1, 1)

        self.line_42 = QFrame(self.layoutWidget_2)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShadow(QFrame.Plain)
        self.line_42.setLineWidth(3)
        self.line_42.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_42, 6, 9, 1, 1)

        self.Right_eyebrow_spinbox = QSpinBox(self.layoutWidget_2)
        self.Right_eyebrow_spinbox.setObjectName(u"Right_eyebrow_spinbox")
        self.Right_eyebrow_spinbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Right_eyebrow_spinbox.setMinimum(-45)
        self.Right_eyebrow_spinbox.setMaximum(45)

        self.gridLayout_2.addWidget(self.Right_eyebrow_spinbox, 8, 3, 1, 1)

        self.Right_LR_spinbox = QSpinBox(self.layoutWidget_2)
        self.Right_LR_spinbox.setObjectName(u"Right_LR_spinbox")
        self.Right_LR_spinbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Right_LR_spinbox.setMinimum(-60)
        self.Right_LR_spinbox.setMaximum(60)

        self.gridLayout_2.addWidget(self.Right_LR_spinbox, 2, 3, 1, 1)

        self.Right_eyebrow_go_button = QPushButton(self.layoutWidget_2)
        self.Right_eyebrow_go_button.setObjectName(u"Right_eyebrow_go_button")
        self.Right_eyebrow_go_button.setFont(font4)
        self.Right_eyebrow_go_button.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.Right_eyebrow_go_button, 8, 10, 1, 1)

        self.Right_UD_go_button = QPushButton(self.layoutWidget_2)
        self.Right_UD_go_button.setObjectName(u"Right_UD_go_button")
        self.Right_UD_go_button.setFont(font4)
        self.Right_UD_go_button.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.Right_UD_go_button, 4, 10, 1, 1)

        self.Right_UD_spinbox = QSpinBox(self.layoutWidget_2)
        self.Right_UD_spinbox.setObjectName(u"Right_UD_spinbox")
        self.Right_UD_spinbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Right_UD_spinbox.setMinimum(-45)
        self.Right_UD_spinbox.setMaximum(45)

        self.gridLayout_2.addWidget(self.Right_UD_spinbox, 4, 3, 1, 1)

        self.line_43 = QFrame(self.layoutWidget_2)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShadow(QFrame.Plain)
        self.line_43.setLineWidth(3)
        self.line_43.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_43, 2, 9, 1, 1)

        self.Right_eyelid_spinbox = QSpinBox(self.layoutWidget_2)
        self.Right_eyelid_spinbox.setObjectName(u"Right_eyelid_spinbox")
        self.Right_eyelid_spinbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Right_eyelid_spinbox.setMinimum(-45)
        self.Right_eyelid_spinbox.setMaximum(45)

        self.gridLayout_2.addWidget(self.Right_eyelid_spinbox, 6, 3, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_45 = QLabel(self.layoutWidget_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_45.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_45)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_24)

        self.label_46 = QLabel(self.layoutWidget_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_46)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_25)

        self.label_47 = QLabel(self.layoutWidget_2)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_47)


        self.verticalLayout_15.addLayout(self.horizontalLayout_20)

        self.Right_eyebrow_position_slider = QSlider(self.layoutWidget_2)
        self.Right_eyebrow_position_slider.setObjectName(u"Right_eyebrow_position_slider")
        self.Right_eyebrow_position_slider.setMinimum(-45)
        self.Right_eyebrow_position_slider.setMaximum(45)
        self.Right_eyebrow_position_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_15.addWidget(self.Right_eyebrow_position_slider)


        self.gridLayout_2.addLayout(self.verticalLayout_15, 8, 2, 1, 1)

        self.line_44 = QFrame(self.layoutWidget_2)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShadow(QFrame.Plain)
        self.line_44.setLineWidth(3)
        self.line_44.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_44, 4, 9, 1, 1)

        self.line_45 = QFrame(self.layoutWidget_2)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setFrameShadow(QFrame.Plain)
        self.line_45.setLineWidth(3)
        self.line_45.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_45, 4, 4, 1, 1)

        self.Right_eyelid_group_checkbox = QCheckBox(self.layoutWidget_2)
        self.Right_eyelid_group_checkbox.setObjectName(u"Right_eyelid_group_checkbox")
        self.Right_eyelid_group_checkbox.setFont(font4)
        self.Right_eyelid_group_checkbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.Right_eyelid_group_checkbox, 6, 8, 1, 1)

        self.line_46 = QFrame(self.layoutWidget_2)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setFrameShadow(QFrame.Plain)
        self.line_46.setLineWidth(3)
        self.line_46.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_46, 1, 0, 1, 11)

        self.line_47 = QFrame(self.layoutWidget_2)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setFrameShadow(QFrame.Plain)
        self.line_47.setLineWidth(3)
        self.line_47.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_47, 8, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_48 = QLabel(self.layoutWidget_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_48)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_26)

        self.label_49 = QLabel(self.layoutWidget_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_49.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_49)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_27)

        self.label_50 = QLabel(self.layoutWidget_2)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_50.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_50)


        self.verticalLayout_16.addLayout(self.horizontalLayout_21)

        self.Right_eyelid_position_slider = QSlider(self.layoutWidget_2)
        self.Right_eyelid_position_slider.setObjectName(u"Right_eyelid_position_slider")
        self.Right_eyelid_position_slider.setMinimum(-45)
        self.Right_eyelid_position_slider.setMaximum(45)
        self.Right_eyelid_position_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_16.addWidget(self.Right_eyelid_position_slider)


        self.gridLayout_2.addLayout(self.verticalLayout_16, 6, 2, 1, 1)

        self.line_48 = QFrame(self.layoutWidget_2)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setFrameShadow(QFrame.Plain)
        self.line_48.setLineWidth(3)
        self.line_48.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_48, 6, 1, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_51 = QLabel(self.layoutWidget_2)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_51)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_28)

        self.label_52 = QLabel(self.layoutWidget_2)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_52)


        self.verticalLayout_17.addLayout(self.horizontalLayout_22)

        self.Right_eyelid_speed_slider = QSlider(self.layoutWidget_2)
        self.Right_eyelid_speed_slider.setObjectName(u"Right_eyelid_speed_slider")
        self.Right_eyelid_speed_slider.setMinimum(0)
        self.Right_eyelid_speed_slider.setMaximum(30)
        self.Right_eyelid_speed_slider.setOrientation(Qt.Horizontal)
        self.Right_eyelid_speed_slider.setInvertedAppearance(True)
        self.Right_eyelid_speed_slider.setInvertedControls(False)

        self.verticalLayout_17.addWidget(self.Right_eyelid_speed_slider)


        self.gridLayout_2.addLayout(self.verticalLayout_17, 6, 6, 1, 1)

        self.line_49 = QFrame(self.layoutWidget_2)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setFrameShadow(QFrame.Plain)
        self.line_49.setLineWidth(3)
        self.line_49.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_49, 0, 9, 1, 1)

        self.line_50 = QFrame(self.layoutWidget_2)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShadow(QFrame.Plain)
        self.line_50.setLineWidth(3)
        self.line_50.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_50, 6, 4, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_53 = QLabel(self.layoutWidget_2)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_53.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_53)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_29)

        self.label_54 = QLabel(self.layoutWidget_2)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_54.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.label_54)


        self.verticalLayout_18.addLayout(self.horizontalLayout_23)

        self.Right_UD_speed_slider = QSlider(self.layoutWidget_2)
        self.Right_UD_speed_slider.setObjectName(u"Right_UD_speed_slider")
        self.Right_UD_speed_slider.setMinimum(0)
        self.Right_UD_speed_slider.setMaximum(30)
        self.Right_UD_speed_slider.setOrientation(Qt.Horizontal)
        self.Right_UD_speed_slider.setInvertedAppearance(True)
        self.Right_UD_speed_slider.setInvertedControls(False)

        self.verticalLayout_18.addWidget(self.Right_UD_speed_slider)


        self.gridLayout_2.addLayout(self.verticalLayout_18, 4, 6, 1, 1)

        self.Right_LR_go_button = QPushButton(self.layoutWidget_2)
        self.Right_LR_go_button.setObjectName(u"Right_LR_go_button")
        self.Right_LR_go_button.setFont(font4)
        self.Right_LR_go_button.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.Right_LR_go_button, 2, 10, 1, 1)

        self.label_55 = QLabel(self.layoutWidget_2)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font3)
        self.label_55.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_55, 0, 6, 1, 1)

        self.label_57 = QLabel(self.layoutWidget_2)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font5)
        self.label_57.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 0)")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_57, 0, 0, 1, 1)

        self.tabWidget.addTab(self.run_servos_tab, "")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 15, 401, 406))
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 15, 91, 16))
        self.label_9.setFont(font)
        self.info_textEdit = QTextEdit(self.widget_2)
        self.info_textEdit.setObjectName(u"info_textEdit")
        self.info_textEdit.setGeometry(QRect(20, 40, 371, 301))
        self.info_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1309, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setFont(font)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.Left_eyelid_position_slider.valueChanged.connect(self.Left_eyelid_spinbox.setValue)
        self.Left_LR_spinbox.valueChanged.connect(self.Left_LR_position_slider.setValue)
        self.Left_eyebrow_position_slider.valueChanged.connect(self.Left_eyebrow_spinbox.setValue)
        self.Left_LR_position_slider.sliderMoved.connect(self.Left_LR_spinbox.setValue)
        self.Left_eyebrow_spinbox.valueChanged.connect(self.Left_eyebrow_position_slider.setValue)
        self.Left_UD_spinbox.valueChanged.connect(self.Left_UD_position_slider.setValue)
        self.Left_UD_position_slider.sliderMoved.connect(self.Left_UD_spinbox.setValue)
        self.Left_eyelid_spinbox.valueChanged.connect(self.Left_eyelid_position_slider.setValue)
        self.open_serial_port.clicked.connect(MainWindow.open_serial_port)
        self.close_serial_port.clicked.connect(MainWindow.close_serial_port)
        self.pushButton.clicked.connect(MainWindow.ping)
        self.Right_LR_position_slider.valueChanged.connect(self.Right_LR_spinbox.setValue)
        self.Right_LR_spinbox.valueChanged.connect(self.Right_LR_position_slider.setValue)
        self.Right_UD_position_slider.valueChanged.connect(self.Right_UD_spinbox.setValue)
        self.Right_UD_spinbox.valueChanged.connect(self.Right_UD_position_slider.setValue)
        self.Right_eyelid_position_slider.valueChanged.connect(self.Right_eyelid_spinbox.setValue)
        self.Right_eyelid_spinbox.valueChanged.connect(self.Right_eyelid_position_slider.setValue)
        self.Right_eyebrow_position_slider.valueChanged.connect(self.Right_eyebrow_spinbox.setValue)
        self.Right_eyebrow_spinbox.valueChanged.connect(self.Right_eyebrow_position_slider.setValue)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.baudrates_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"115200", None))
        self.baudrates_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"9600", None))

        self.baudrates_comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"115200", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Serial ports", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Baud rates", None))
        self.open_serial_port.setText(QCoreApplication.translate("MainWindow", u"Open serial port", None))
        self.close_serial_port.setText(QCoreApplication.translate("MainWindow", u"Close serial port", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ping", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_serial_port_tab), QCoreApplication.translate("MainWindow", u"Set serial port", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Eyelid", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Eyebrow", None))
        self.Left_eyebrow_group_checkbox.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"UP/DOWN", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.Left_UD_group_checkbox.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"-60", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"+60", None))
        self.Left_LR_group_checkbox.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LEFT/RIGHT", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Left_eyelid_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Left_eyebrow_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.Left_UD_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.Left_eyelid_group_checkbox.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Left_LR_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Left eye", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Eyelid", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Eyebrow", None))
        self.Right_eyebrow_group_checkbox.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"UP/DOWN", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.Left_UD_group_checkbox_5.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"-60", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"+60", None))
        self.Right_LR_group_checkbox_2.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"LEFT/RIGHT", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Right_eyelid_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Right_eyebrow_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.Right_UD_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.Right_eyelid_group_checkbox.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Right_LR_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Right eye", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.run_servos_tab), QCoreApplication.translate("MainWindow", u"Run_servos", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

