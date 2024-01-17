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
        self.tabWidget.setGeometry(QRect(430, 40, 921, 671))
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

        self.lab_22 = QLabel(self.layoutWidget1)
        self.lab_22.setObjectName(u"lab_22")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        self.lab_22.setFont(font3)
        self.lab_22.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.lab_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lab_22, 6, 0, 1, 1)

        self.line_13 = QFrame(self.layoutWidget1)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShadow(QFrame.Plain)
        self.line_13.setLineWidth(3)
        self.line_13.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_13, 0, 7, 1, 1)

        self.lab_32 = QLabel(self.layoutWidget1)
        self.lab_32.setObjectName(u"lab_32")
        self.lab_32.setFont(font3)
        self.lab_32.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.lab_32.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lab_32, 8, 0, 1, 1)

        self.checkbox_30 = QCheckBox(self.layoutWidget1)
        self.checkbox_30.setObjectName(u"checkbox_30")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        self.checkbox_30.setFont(font4)
        self.checkbox_30.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.checkbox_30, 8, 8, 1, 1)

        self.lab_12 = QLabel(self.layoutWidget1)
        self.lab_12.setObjectName(u"lab_12")
        self.lab_12.setFont(font3)
        self.lab_12.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.lab_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lab_12, 4, 0, 1, 1)

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
        self.lab_10 = QLabel(self.layoutWidget1)
        self.lab_10.setObjectName(u"lab_10")
        self.lab_10.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lab_10)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.label_19 = QLabel(self.layoutWidget1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_19)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.lab_11 = QLabel(self.layoutWidget1)
        self.lab_11.setObjectName(u"lab_11")
        self.lab_11.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lab_11)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.slider_10 = QSlider(self.layoutWidget1)
        self.slider_10.setObjectName(u"slider_10")
        self.slider_10.setMinimum(-45)
        self.slider_10.setMaximum(45)
        self.slider_10.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.slider_10)


        self.gridLayout.addLayout(self.verticalLayout_5, 4, 2, 1, 1)

        self.line_3 = QFrame(self.layoutWidget1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_3, 2, 1, 1, 1)

        self.checkbox_10 = QCheckBox(self.layoutWidget1)
        self.checkbox_10.setObjectName(u"checkbox_10")
        self.checkbox_10.setFont(font4)
        self.checkbox_10.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.checkbox_10, 4, 8, 1, 1)

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
        self.lab_00 = QLabel(self.layoutWidget1)
        self.lab_00.setObjectName(u"lab_00")
        self.lab_00.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_00.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lab_00)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.lab_01 = QLabel(self.layoutWidget1)
        self.lab_01.setObjectName(u"lab_01")
        self.lab_01.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_01.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lab_01)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.slider_00 = QSlider(self.layoutWidget1)
        self.slider_00.setObjectName(u"slider_00")
        self.slider_00.setMinimum(-60)
        self.slider_00.setMaximum(60)
        self.slider_00.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.slider_00)


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

        self.checkbox_00 = QCheckBox(self.layoutWidget1)
        self.checkbox_00.setObjectName(u"checkbox_00")
        self.checkbox_00.setFont(font4)
        self.checkbox_00.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.checkbox_00, 2, 8, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lab_02 = QLabel(self.layoutWidget1)
        self.lab_02.setObjectName(u"lab_02")
        self.lab_02.setFont(font3)
        self.lab_02.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.lab_02.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lab_02)

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

        self.slider_01 = QSlider(self.layoutWidget1)
        self.slider_01.setObjectName(u"slider_01")
        self.slider_01.setMinimum(0)
        self.slider_01.setMaximum(250)
        self.slider_01.setSingleStep(5)
        self.slider_01.setOrientation(Qt.Horizontal)
        self.slider_01.setInvertedAppearance(False)
        self.slider_01.setInvertedControls(False)

        self.verticalLayout_4.addWidget(self.slider_01)


        self.gridLayout.addLayout(self.verticalLayout_4, 2, 6, 1, 1)

        self.button_20 = QPushButton(self.layoutWidget1)
        self.button_20.setObjectName(u"button_20")
        self.button_20.setFont(font4)
        self.button_20.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.button_20, 6, 10, 1, 1)

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

        self.slider_31 = QSlider(self.layoutWidget1)
        self.slider_31.setObjectName(u"slider_31")
        self.slider_31.setMinimum(0)
        self.slider_31.setMaximum(250)
        self.slider_31.setSingleStep(5)
        self.slider_31.setOrientation(Qt.Horizontal)
        self.slider_31.setInvertedAppearance(False)
        self.slider_31.setInvertedControls(False)

        self.verticalLayout_10.addWidget(self.slider_31)


        self.gridLayout.addLayout(self.verticalLayout_10, 8, 6, 1, 1)

        self.line_20 = QFrame(self.layoutWidget1)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShadow(QFrame.Plain)
        self.line_20.setLineWidth(3)
        self.line_20.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_20, 6, 9, 1, 1)

        self.spinbox_30 = QSpinBox(self.layoutWidget1)
        self.spinbox_30.setObjectName(u"spinbox_30")
        self.spinbox_30.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.spinbox_30.setMinimum(-45)
        self.spinbox_30.setMaximum(45)

        self.gridLayout.addWidget(self.spinbox_30, 8, 3, 1, 1)

        self.spinbox_00 = QSpinBox(self.layoutWidget1)
        self.spinbox_00.setObjectName(u"spinbox_00")
        self.spinbox_00.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.spinbox_00.setMinimum(-60)
        self.spinbox_00.setMaximum(60)

        self.gridLayout.addWidget(self.spinbox_00, 2, 3, 1, 1)

        self.button_30 = QPushButton(self.layoutWidget1)
        self.button_30.setObjectName(u"button_30")
        self.button_30.setFont(font4)
        self.button_30.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.button_30, 8, 10, 1, 1)

        self.button_10 = QPushButton(self.layoutWidget1)
        self.button_10.setObjectName(u"button_10")
        self.button_10.setFont(font4)
        self.button_10.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.button_10, 4, 10, 1, 1)

        self.spinbox_10 = QSpinBox(self.layoutWidget1)
        self.spinbox_10.setObjectName(u"spinbox_10")
        self.spinbox_10.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.spinbox_10.setMinimum(-45)
        self.spinbox_10.setMaximum(45)

        self.gridLayout.addWidget(self.spinbox_10, 4, 3, 1, 1)

        self.line_10 = QFrame(self.layoutWidget1)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_10, 2, 9, 1, 1)

        self.spinbox_20 = QSpinBox(self.layoutWidget1)
        self.spinbox_20.setObjectName(u"spinbox_20")
        self.spinbox_20.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.spinbox_20.setMinimum(-45)
        self.spinbox_20.setMaximum(45)

        self.gridLayout.addWidget(self.spinbox_20, 6, 3, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lab_30 = QLabel(self.layoutWidget1)
        self.lab_30.setObjectName(u"lab_30")
        self.lab_30.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.lab_30)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)

        self.label_29 = QLabel(self.layoutWidget1)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_29)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)

        self.lab_31 = QLabel(self.layoutWidget1)
        self.lab_31.setObjectName(u"lab_31")
        self.lab_31.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.lab_31)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.slider_30 = QSlider(self.layoutWidget1)
        self.slider_30.setObjectName(u"slider_30")
        self.slider_30.setMinimum(-45)
        self.slider_30.setMaximum(45)
        self.slider_30.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.slider_30)


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

        self.checkbox_20 = QCheckBox(self.layoutWidget1)
        self.checkbox_20.setObjectName(u"checkbox_20")
        self.checkbox_20.setFont(font4)
        self.checkbox_20.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.checkbox_20, 6, 8, 1, 1)

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
        self.lab_20 = QLabel(self.layoutWidget1)
        self.lab_20.setObjectName(u"lab_20")
        self.lab_20.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.lab_20)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_12)

        self.label_24 = QLabel(self.layoutWidget1)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_24)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)

        self.lab_21 = QLabel(self.layoutWidget1)
        self.lab_21.setObjectName(u"lab_21")
        self.lab_21.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.lab_21)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.slider_20 = QSlider(self.layoutWidget1)
        self.slider_20.setObjectName(u"slider_20")
        self.slider_20.setMinimum(-45)
        self.slider_20.setMaximum(45)
        self.slider_20.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.slider_20)


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

        self.slider_21 = QSlider(self.layoutWidget1)
        self.slider_21.setObjectName(u"slider_21")
        self.slider_21.setMinimum(0)
        self.slider_21.setMaximum(250)
        self.slider_21.setSingleStep(5)
        self.slider_21.setOrientation(Qt.Horizontal)
        self.slider_21.setInvertedAppearance(False)
        self.slider_21.setInvertedControls(False)

        self.verticalLayout_8.addWidget(self.slider_21)


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

        self.slider_11 = QSlider(self.layoutWidget1)
        self.slider_11.setObjectName(u"slider_11")
        self.slider_11.setMinimum(0)
        self.slider_11.setMaximum(250)
        self.slider_11.setSingleStep(5)
        self.slider_11.setOrientation(Qt.Horizontal)
        self.slider_11.setInvertedAppearance(False)
        self.slider_11.setInvertedControls(False)

        self.verticalLayout_6.addWidget(self.slider_11)


        self.gridLayout.addLayout(self.verticalLayout_6, 4, 6, 1, 1)

        self.button_00 = QPushButton(self.layoutWidget1)
        self.button_00.setObjectName(u"button_00")
        self.button_00.setFont(font4)
        self.button_00.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.button_00, 2, 10, 1, 1)

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

        self.button_10.raise_()
        self.lab_22.raise_()
        self.checkbox_10.raise_()
        self.line_22.raise_()
        self.button_00.raise_()
        self.button_20.raise_()
        self.button_30.raise_()
        self.lab_32.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_16.raise_()
        self.line_20.raise_()
        self.line_19.raise_()
        self.spinbox_30.raise_()
        self.line_11.raise_()
        self.spinbox_00.raise_()
        self.checkbox_00.raise_()
        self.line_8.raise_()
        self.line_4.raise_()
        self.line_12.raise_()
        self.line_5.raise_()
        self.line_21.raise_()
        self.line_15.raise_()
        self.line_24.raise_()
        self.line_18.raise_()
        self.checkbox_20.raise_()
        self.line_23.raise_()
        self.spinbox_20.raise_()
        self.checkbox_30.raise_()
        self.line_14.raise_()
        self.line.raise_()
        self.spinbox_10.raise_()
        self.line_17.raise_()
        self.line_13.raise_()
        self.line_10.raise_()
        self.line_3.raise_()
        self.line_9.raise_()
        self.lab_12.raise_()
        self.line_25.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_56.raise_()
        self.layoutWidget_2 = QWidget(self.run_servos_tab)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(15, 290, 759, 340))
        self.layoutWidget_2.setFont(font2)
        self.gridLayout_2 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_43 = QFrame(self.layoutWidget_2)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShadow(QFrame.Plain)
        self.line_43.setLineWidth(3)
        self.line_43.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_43, 2, 9, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lab_60 = QLabel(self.layoutWidget_2)
        self.lab_60.setObjectName(u"lab_60")
        self.lab_60.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_60.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.lab_60)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_26)

        self.label_49 = QLabel(self.layoutWidget_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_49.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_49)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_27)

        self.lab_61 = QLabel(self.layoutWidget_2)
        self.lab_61.setObjectName(u"lab_61")
        self.lab_61.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_61.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.lab_61)


        self.verticalLayout_16.addLayout(self.horizontalLayout_21)

        self.slider_60 = QSlider(self.layoutWidget_2)
        self.slider_60.setObjectName(u"slider_60")
        self.slider_60.setMinimum(-45)
        self.slider_60.setMaximum(45)
        self.slider_60.setOrientation(Qt.Horizontal)

        self.verticalLayout_16.addWidget(self.slider_60)


        self.gridLayout_2.addLayout(self.verticalLayout_16, 6, 2, 1, 1)

        self.line_54 = QFrame(self.layoutWidget_2)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setFrameShadow(QFrame.Plain)
        self.line_54.setLineWidth(3)
        self.line_54.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_54, 11, 1, 1, 1)

        self.line_33 = QFrame(self.layoutWidget_2)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShadow(QFrame.Plain)
        self.line_33.setLineWidth(3)
        self.line_33.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_33, 4, 1, 1, 1)

        self.line_39 = QFrame(self.layoutWidget_2)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShadow(QFrame.Plain)
        self.line_39.setLineWidth(3)
        self.line_39.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_39, 2, 7, 1, 1)

        self.line_42 = QFrame(self.layoutWidget_2)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShadow(QFrame.Plain)
        self.line_42.setLineWidth(3)
        self.line_42.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_42, 6, 9, 1, 1)

        self.label_57 = QLabel(self.layoutWidget_2)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font5)
        self.label_57.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 0)")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_57, 0, 0, 1, 1)

        self.line_32 = QFrame(self.layoutWidget_2)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShadow(QFrame.Plain)
        self.line_32.setLineWidth(3)
        self.line_32.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_32, 2, 1, 1, 1)

        self.button_40 = QPushButton(self.layoutWidget_2)
        self.button_40.setObjectName(u"button_40")
        self.button_40.setFont(font4)
        self.button_40.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.button_40, 2, 10, 1, 1)

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

        self.slider_51 = QSlider(self.layoutWidget_2)
        self.slider_51.setObjectName(u"slider_51")
        self.slider_51.setMinimum(0)
        self.slider_51.setMaximum(250)
        self.slider_51.setSingleStep(5)
        self.slider_51.setOrientation(Qt.Horizontal)
        self.slider_51.setInvertedAppearance(False)
        self.slider_51.setInvertedControls(False)

        self.verticalLayout_18.addWidget(self.slider_51)


        self.gridLayout_2.addLayout(self.verticalLayout_18, 4, 6, 1, 1)

        self.lab_72 = QLabel(self.layoutWidget_2)
        self.lab_72.setObjectName(u"lab_72")
        self.lab_72.setFont(font3)
        self.lab_72.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.lab_72.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lab_72, 8, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lab_42 = QLabel(self.layoutWidget_2)
        self.lab_42.setObjectName(u"lab_42")
        self.lab_42.setFont(font3)
        self.lab_42.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.lab_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.lab_42)

        self.line_37 = QFrame(self.layoutWidget_2)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShadow(QFrame.Plain)
        self.line_37.setLineWidth(3)
        self.line_37.setFrameShape(QFrame.HLine)

        self.horizontalLayout_17.addWidget(self.line_37)


        self.gridLayout_2.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)

        self.button_70 = QPushButton(self.layoutWidget_2)
        self.button_70.setObjectName(u"button_70")
        self.button_70.setFont(font4)
        self.button_70.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.button_70, 8, 10, 1, 1)

        self.checkbox_60 = QCheckBox(self.layoutWidget_2)
        self.checkbox_60.setObjectName(u"checkbox_60")
        self.checkbox_60.setFont(font4)
        self.checkbox_60.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.checkbox_60, 6, 8, 1, 1)

        self.label_55 = QLabel(self.layoutWidget_2)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font3)
        self.label_55.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_55, 0, 6, 1, 1)

        self.line_41 = QFrame(self.layoutWidget_2)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setFrameShadow(QFrame.Plain)
        self.line_41.setLineWidth(3)
        self.line_41.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_41, 3, 0, 1, 11)

        self.line_53 = QFrame(self.layoutWidget_2)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setFrameShadow(QFrame.Plain)
        self.line_53.setLineWidth(3)
        self.line_53.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_53, 9, 0, 1, 11)

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

        self.slider_61 = QSlider(self.layoutWidget_2)
        self.slider_61.setObjectName(u"slider_61")
        self.slider_61.setMinimum(0)
        self.slider_61.setMaximum(250)
        self.slider_61.setSingleStep(5)
        self.slider_61.setOrientation(Qt.Horizontal)
        self.slider_61.setInvertedAppearance(False)
        self.slider_61.setInvertedControls(False)

        self.verticalLayout_17.addWidget(self.slider_61)


        self.gridLayout_2.addLayout(self.verticalLayout_17, 6, 6, 1, 1)

        self.checkbox_40 = QCheckBox(self.layoutWidget_2)
        self.checkbox_40.setObjectName(u"checkbox_40")
        self.checkbox_40.setFont(font4)
        self.checkbox_40.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.checkbox_40, 2, 8, 1, 1)

        self.checkbox_80 = QCheckBox(self.layoutWidget_2)
        self.checkbox_80.setObjectName(u"checkbox_80")
        self.checkbox_80.setFont(font4)
        self.checkbox_80.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.checkbox_80, 11, 8, 1, 1)

        self.line_36 = QFrame(self.layoutWidget_2)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShadow(QFrame.Plain)
        self.line_36.setLineWidth(3)
        self.line_36.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_36, 0, 1, 1, 1)

        self.line_49 = QFrame(self.layoutWidget_2)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setFrameShadow(QFrame.Plain)
        self.line_49.setLineWidth(3)
        self.line_49.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_49, 0, 9, 1, 1)

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

        self.slider_71 = QSlider(self.layoutWidget_2)
        self.slider_71.setObjectName(u"slider_71")
        self.slider_71.setMinimum(0)
        self.slider_71.setMaximum(250)
        self.slider_71.setSingleStep(5)
        self.slider_71.setOrientation(Qt.Horizontal)
        self.slider_71.setInvertedAppearance(False)
        self.slider_71.setInvertedControls(False)

        self.verticalLayout_14.addWidget(self.slider_71)


        self.gridLayout_2.addLayout(self.verticalLayout_14, 8, 6, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lab_40 = QLabel(self.layoutWidget_2)
        self.lab_40.setObjectName(u"lab_40")
        self.lab_40.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.lab_40)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_20)

        self.label_38 = QLabel(self.layoutWidget_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_38)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_21)

        self.lab_41 = QLabel(self.layoutWidget_2)
        self.lab_41.setObjectName(u"lab_41")
        self.lab_41.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.lab_41)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.slider_40 = QSlider(self.layoutWidget_2)
        self.slider_40.setObjectName(u"slider_40")
        self.slider_40.setMinimum(-60)
        self.slider_40.setMaximum(60)
        self.slider_40.setOrientation(Qt.Horizontal)

        self.verticalLayout_12.addWidget(self.slider_40)


        self.gridLayout_2.addLayout(self.verticalLayout_12, 2, 2, 1, 1)

        self.button_50 = QPushButton(self.layoutWidget_2)
        self.button_50.setObjectName(u"button_50")
        self.button_50.setFont(font4)
        self.button_50.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.button_50, 4, 10, 1, 1)

        self.line_45 = QFrame(self.layoutWidget_2)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setFrameShadow(QFrame.Plain)
        self.line_45.setLineWidth(3)
        self.line_45.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_45, 4, 4, 1, 1)

        self.line_50 = QFrame(self.layoutWidget_2)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShadow(QFrame.Plain)
        self.line_50.setLineWidth(3)
        self.line_50.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_50, 6, 4, 1, 1)

        self.spinbox_50 = QSpinBox(self.layoutWidget_2)
        self.spinbox_50.setObjectName(u"spinbox_50")
        self.spinbox_50.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.spinbox_50.setMinimum(-45)
        self.spinbox_50.setMaximum(45)

        self.gridLayout_2.addWidget(self.spinbox_50, 4, 3, 1, 1)

        self.spinbox_70 = QSpinBox(self.layoutWidget_2)
        self.spinbox_70.setObjectName(u"spinbox_70")
        self.spinbox_70.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.spinbox_70.setMinimum(-45)
        self.spinbox_70.setMaximum(45)

        self.gridLayout_2.addWidget(self.spinbox_70, 8, 3, 1, 1)

        self.line_46 = QFrame(self.layoutWidget_2)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setFrameShadow(QFrame.Plain)
        self.line_46.setLineWidth(3)
        self.line_46.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_46, 1, 0, 1, 11)

        self.checkbox_70 = QCheckBox(self.layoutWidget_2)
        self.checkbox_70.setObjectName(u"checkbox_70")
        self.checkbox_70.setFont(font4)
        self.checkbox_70.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.checkbox_70, 8, 8, 1, 1)

        self.checkbox_50 = QCheckBox(self.layoutWidget_2)
        self.checkbox_50.setObjectName(u"checkbox_50")
        self.checkbox_50.setFont(font4)
        self.checkbox_50.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.checkbox_50, 4, 8, 1, 1)

        self.line_31 = QFrame(self.layoutWidget_2)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShadow(QFrame.Plain)
        self.line_31.setLineWidth(3)
        self.line_31.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_31, 4, 7, 1, 1)

        self.lab_62 = QLabel(self.layoutWidget_2)
        self.lab_62.setObjectName(u"lab_62")
        self.lab_62.setFont(font3)
        self.lab_62.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.lab_62.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lab_62, 6, 0, 1, 1)

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

        self.slider_41 = QSlider(self.layoutWidget_2)
        self.slider_41.setObjectName(u"slider_41")
        self.slider_41.setMinimum(0)
        self.slider_41.setMaximum(250)
        self.slider_41.setSingleStep(5)
        self.slider_41.setOrientation(Qt.Horizontal)
        self.slider_41.setInvertedAppearance(False)
        self.slider_41.setInvertedControls(False)

        self.verticalLayout_13.addWidget(self.slider_41)


        self.gridLayout_2.addLayout(self.verticalLayout_13, 2, 6, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lab_50 = QLabel(self.layoutWidget_2)
        self.lab_50.setObjectName(u"lab_50")
        self.lab_50.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_50.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.lab_50)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_18)

        self.label_34 = QLabel(self.layoutWidget_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_34)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_19)

        self.lab_51 = QLabel(self.layoutWidget_2)
        self.lab_51.setObjectName(u"lab_51")
        self.lab_51.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.lab_51)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.slider_50 = QSlider(self.layoutWidget_2)
        self.slider_50.setObjectName(u"slider_50")
        self.slider_50.setMinimum(-45)
        self.slider_50.setMaximum(45)
        self.slider_50.setOrientation(Qt.Horizontal)

        self.verticalLayout_11.addWidget(self.slider_50)


        self.gridLayout_2.addLayout(self.verticalLayout_11, 4, 2, 1, 1)

        self.line_34 = QFrame(self.layoutWidget_2)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShadow(QFrame.Plain)
        self.line_34.setLineWidth(3)
        self.line_34.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_34, 0, 4, 1, 1)

        self.lab_52 = QLabel(self.layoutWidget_2)
        self.lab_52.setObjectName(u"lab_52")
        self.lab_52.setFont(font3)
        self.lab_52.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.lab_52.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lab_52, 4, 0, 1, 1)

        self.line_29 = QFrame(self.layoutWidget_2)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShadow(QFrame.Plain)
        self.line_29.setLineWidth(3)
        self.line_29.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_29, 2, 4, 1, 1)

        self.line_48 = QFrame(self.layoutWidget_2)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setFrameShadow(QFrame.Plain)
        self.line_48.setLineWidth(3)
        self.line_48.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_48, 6, 1, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lab_70 = QLabel(self.layoutWidget_2)
        self.lab_70.setObjectName(u"lab_70")
        self.lab_70.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_70.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.lab_70)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_24)

        self.label_46 = QLabel(self.layoutWidget_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_46)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_25)

        self.lab_71 = QLabel(self.layoutWidget_2)
        self.lab_71.setObjectName(u"lab_71")
        self.lab_71.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_71.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.lab_71)


        self.verticalLayout_15.addLayout(self.horizontalLayout_20)

        self.slider_70 = QSlider(self.layoutWidget_2)
        self.slider_70.setObjectName(u"slider_70")
        self.slider_70.setMinimum(-45)
        self.slider_70.setMaximum(45)
        self.slider_70.setOrientation(Qt.Horizontal)

        self.verticalLayout_15.addWidget(self.slider_70)


        self.gridLayout_2.addLayout(self.verticalLayout_15, 8, 2, 1, 1)

        self.line_27 = QFrame(self.layoutWidget_2)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShadow(QFrame.Plain)
        self.line_27.setLineWidth(3)
        self.line_27.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_27, 7, 0, 1, 11)

        self.line_26 = QFrame(self.layoutWidget_2)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShadow(QFrame.Plain)
        self.line_26.setLineWidth(3)
        self.line_26.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_26, 6, 7, 1, 1)

        self.button_60 = QPushButton(self.layoutWidget_2)
        self.button_60.setObjectName(u"button_60")
        self.button_60.setFont(font4)
        self.button_60.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.button_60, 6, 10, 1, 1)

        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 11, 0, 1, 1)

        self.spinbox_60 = QSpinBox(self.layoutWidget_2)
        self.spinbox_60.setObjectName(u"spinbox_60")
        self.spinbox_60.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.spinbox_60.setMinimum(-45)
        self.spinbox_60.setMaximum(45)

        self.gridLayout_2.addWidget(self.spinbox_60, 6, 3, 1, 1)

        self.spinbox_40 = QSpinBox(self.layoutWidget_2)
        self.spinbox_40.setObjectName(u"spinbox_40")
        self.spinbox_40.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.spinbox_40.setMinimum(-60)
        self.spinbox_40.setMaximum(60)

        self.gridLayout_2.addWidget(self.spinbox_40, 2, 3, 1, 1)

        self.line_38 = QFrame(self.layoutWidget_2)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShadow(QFrame.Plain)
        self.line_38.setLineWidth(3)
        self.line_38.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_38, 8, 9, 1, 1)

        self.label_36 = QLabel(self.layoutWidget_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_36, 0, 2, 1, 1)

        self.line_44 = QFrame(self.layoutWidget_2)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShadow(QFrame.Plain)
        self.line_44.setLineWidth(3)
        self.line_44.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_44, 4, 9, 1, 1)

        self.button_80 = QPushButton(self.layoutWidget_2)
        self.button_80.setObjectName(u"button_80")
        self.button_80.setFont(font4)
        self.button_80.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.button_80, 11, 10, 1, 1)

        self.line_28 = QFrame(self.layoutWidget_2)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShadow(QFrame.Plain)
        self.line_28.setLineWidth(3)
        self.line_28.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_28, 0, 7, 1, 1)

        self.line_30 = QFrame(self.layoutWidget_2)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShadow(QFrame.Plain)
        self.line_30.setLineWidth(3)
        self.line_30.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_30, 8, 4, 1, 1)

        self.line_35 = QFrame(self.layoutWidget_2)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShadow(QFrame.Plain)
        self.line_35.setLineWidth(3)
        self.line_35.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_35, 5, 0, 1, 11)

        self.line_47 = QFrame(self.layoutWidget_2)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setFrameShadow(QFrame.Plain)
        self.line_47.setLineWidth(3)
        self.line_47.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_47, 8, 1, 1, 1)

        self.line_40 = QFrame(self.layoutWidget_2)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShadow(QFrame.Plain)
        self.line_40.setLineWidth(3)
        self.line_40.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_40, 8, 7, 1, 1)

        self.line_51 = QFrame(self.layoutWidget_2)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setFrameShadow(QFrame.Plain)
        self.line_51.setLineWidth(3)
        self.line_51.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_51, 12, 0, 1, 11)

        self.line_52 = QFrame(self.layoutWidget_2)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setFrameShadow(QFrame.Plain)
        self.line_52.setLineWidth(3)
        self.line_52.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_52, 10, 0, 1, 11)

        self.line_55 = QFrame(self.layoutWidget_2)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setFrameShadow(QFrame.Plain)
        self.line_55.setLineWidth(3)
        self.line_55.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_55, 11, 4, 1, 1)

        self.line_56 = QFrame(self.layoutWidget_2)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setFrameShadow(QFrame.Plain)
        self.line_56.setLineWidth(3)
        self.line_56.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_56, 11, 7, 1, 1)

        self.line_57 = QFrame(self.layoutWidget_2)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setFrameShadow(QFrame.Plain)
        self.line_57.setLineWidth(3)
        self.line_57.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_57, 11, 9, 1, 1)

        self.tabWidget.addTab(self.run_servos_tab, "")
        self.run_steppers_tab = QWidget()
        self.run_steppers_tab.setObjectName(u"run_steppers_tab")
        self.layoutWidget2 = QWidget(self.run_steppers_tab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(55, 75, 391, 352))
        self.gridLayout_3 = QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget2)
        self.label_15.setObjectName(u"label_15")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_15.setFont(font6)
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_15, 13, 0, 1, 1)

        self.line_60 = QFrame(self.layoutWidget2)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setFrameShape(QFrame.HLine)
        self.line_60.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_60, 7, 0, 1, 4)

        self.line_65 = QFrame(self.layoutWidget2)
        self.line_65.setObjectName(u"line_65")
        self.line_65.setFrameShape(QFrame.VLine)
        self.line_65.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_65, 1, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10.setIndent(-3)

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.line_67 = QFrame(self.layoutWidget2)
        self.line_67.setObjectName(u"line_67")
        self.line_67.setFrameShape(QFrame.VLine)
        self.line_67.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_67, 8, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.layoutWidget2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)

        self.gridLayout_3.addLayout(self.horizontalLayout, 13, 2, 1, 1)

        self.line_69 = QFrame(self.layoutWidget2)
        self.line_69.setObjectName(u"line_69")
        self.line_69.setFrameShape(QFrame.VLine)
        self.line_69.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_69, 13, 1, 1, 1)

        self.label_11 = QLabel(self.layoutWidget2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_11, 11, 0, 1, 1)

        self.line_62 = QFrame(self.layoutWidget2)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setFrameShape(QFrame.HLine)
        self.line_62.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_62, 12, 0, 1, 4)

        self.line_61 = QFrame(self.layoutWidget2)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setFrameShape(QFrame.HLine)
        self.line_61.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_61, 10, 0, 1, 4)

        self.spinBox = QSpinBox(self.layoutWidget2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setFrame(True)
        self.spinBox.setProperty("showGroupSeparator", False)
        self.spinBox.setMinimum(-60)
        self.spinBox.setMaximum(60)
        self.spinBox.setSingleStep(5)

        self.gridLayout_3.addWidget(self.spinBox, 5, 3, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lab_33 = QLabel(self.layoutWidget2)
        self.lab_33.setObjectName(u"lab_33")
        self.lab_33.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.lab_33)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_30)

        self.label_30 = QLabel(self.layoutWidget2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.label_30)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_31)

        self.lab_34 = QLabel(self.layoutWidget2)
        self.lab_34.setObjectName(u"lab_34")
        self.lab_34.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.lab_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_24.addWidget(self.lab_34)


        self.verticalLayout_19.addLayout(self.horizontalLayout_24)

        self.slider_step_value = QSlider(self.layoutWidget2)
        self.slider_step_value.setObjectName(u"slider_step_value")
        self.slider_step_value.setMinimum(-60)
        self.slider_step_value.setMaximum(60)
        self.slider_step_value.setOrientation(Qt.Horizontal)

        self.verticalLayout_19.addWidget(self.slider_step_value)


        self.gridLayout_3.addLayout(self.verticalLayout_19, 5, 2, 1, 1)

        self.line_63 = QFrame(self.layoutWidget2)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setFrameShape(QFrame.HLine)
        self.line_63.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_63, 0, 0, 1, 4)

        self.line_66 = QFrame(self.layoutWidget2)
        self.line_66.setObjectName(u"line_66")
        self.line_66.setFrameShape(QFrame.VLine)
        self.line_66.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_66, 5, 1, 1, 1)

        self.line_68 = QFrame(self.layoutWidget2)
        self.line_68.setObjectName(u"line_68")
        self.line_68.setFrameShape(QFrame.VLine)
        self.line_68.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_68, 11, 1, 1, 1)

        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_7, 8, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.checkBox = QCheckBox(self.layoutWidget2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font1)

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 11, 2, 1, 1)

        self.line_58 = QFrame(self.layoutWidget2)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setFrameShape(QFrame.HLine)
        self.line_58.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_58, 2, 0, 1, 4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_33)

        self.comboBox = QComboBox(self.layoutWidget2)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_34)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 1)

        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.comboBox_2 = QComboBox(self.layoutWidget2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_3.addWidget(self.comboBox_2)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_32)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 1)

        self.gridLayout_3.addLayout(self.horizontalLayout_3, 8, 2, 1, 1)

        self.line_64 = QFrame(self.layoutWidget2)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setFrameShape(QFrame.HLine)
        self.line_64.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_64, 14, 0, 1, 4)

        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(False)
        self.label_3.setFont(font7)

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.line_59 = QFrame(self.layoutWidget2)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setFrameShape(QFrame.HLine)
        self.line_59.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_59, 4, 0, 1, 4)

        self.line_70 = QFrame(self.layoutWidget2)
        self.line_70.setObjectName(u"line_70")
        self.line_70.setFrameShape(QFrame.VLine)
        self.line_70.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_70, 3, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_35)

        self.comboBox_3 = QComboBox(self.layoutWidget2)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_5.addWidget(self.comboBox_3)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_36)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 2, 1, 1)

        self.tabWidget.addTab(self.run_steppers_tab, "")
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
        self.slider_20.valueChanged.connect(self.spinbox_20.setValue)
        self.spinbox_00.valueChanged.connect(self.slider_00.setValue)
        self.slider_30.valueChanged.connect(self.spinbox_30.setValue)
        self.slider_00.sliderMoved.connect(self.spinbox_00.setValue)
        self.spinbox_30.valueChanged.connect(self.slider_30.setValue)
        self.spinbox_10.valueChanged.connect(self.slider_10.setValue)
        self.slider_10.sliderMoved.connect(self.spinbox_10.setValue)
        self.spinbox_20.valueChanged.connect(self.slider_20.setValue)
        self.open_serial_port.clicked.connect(MainWindow.open_serial_port)
        self.close_serial_port.clicked.connect(MainWindow.close_serial_port)
        self.pushButton.clicked.connect(MainWindow.ping)
        self.slider_40.valueChanged.connect(self.spinbox_40.setValue)
        self.spinbox_40.valueChanged.connect(self.slider_40.setValue)
        self.slider_50.valueChanged.connect(self.spinbox_50.setValue)
        self.spinbox_50.valueChanged.connect(self.slider_50.setValue)
        self.slider_60.valueChanged.connect(self.spinbox_60.setValue)
        self.spinbox_60.valueChanged.connect(self.slider_60.setValue)
        self.slider_70.valueChanged.connect(self.spinbox_70.setValue)
        self.spinbox_70.valueChanged.connect(self.slider_70.setValue)
        self.slider_step_value.valueChanged.connect(self.spinBox.setValue)
        self.spinBox.valueChanged.connect(self.slider_step_value.setValue)

        self.tabWidget.setCurrentIndex(1)


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
        self.lab_22.setText(QCoreApplication.translate("MainWindow", u"Eyelid", None))
        self.lab_32.setText(QCoreApplication.translate("MainWindow", u"Eyebrow", None))
        self.checkbox_30.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.lab_12.setText(QCoreApplication.translate("MainWindow", u"UP/DOWN", None))
        self.lab_10.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lab_11.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.checkbox_10.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.lab_00.setText(QCoreApplication.translate("MainWindow", u"-60", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lab_01.setText(QCoreApplication.translate("MainWindow", u"+60", None))
        self.checkbox_00.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.lab_02.setText(QCoreApplication.translate("MainWindow", u"LEFT/RIGHT", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.button_20.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.button_30.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.button_10.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.lab_30.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lab_31.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.checkbox_20.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.lab_20.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lab_21.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.button_00.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Left eye", None))
        self.lab_60.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lab_61.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Right eye", None))
        self.button_40.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.lab_72.setText(QCoreApplication.translate("MainWindow", u"Eyebrow", None))
        self.lab_42.setText(QCoreApplication.translate("MainWindow", u"LEFT/RIGHT", None))
        self.button_70.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.checkbox_60.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.checkbox_40.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.checkbox_80.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.lab_40.setText(QCoreApplication.translate("MainWindow", u"-60", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lab_41.setText(QCoreApplication.translate("MainWindow", u"+60", None))
        self.button_50.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.checkbox_70.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.checkbox_50.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.lab_62.setText(QCoreApplication.translate("MainWindow", u"Eyelid", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.lab_50.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lab_51.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.lab_52.setText(QCoreApplication.translate("MainWindow", u"UP/DOWN", None))
        self.lab_70.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lab_71.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.button_60.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mouth", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.button_80.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.run_servos_tab), QCoreApplication.translate("MainWindow", u"Run servo motors", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Type of MOVE", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Add to group move", None))
        self.lab_33.setText(QCoreApplication.translate("MainWindow", u"-60", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lab_34.setText(QCoreApplication.translate("MainWindow", u"+60", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Speed profile", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select stepper motor", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Move angle (degrees)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.run_steppers_tab), QCoreApplication.translate("MainWindow", u"Run stepper motors", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

