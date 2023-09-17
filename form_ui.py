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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(888, 600)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setCheckable(False)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionSet_Serial_Port = QAction(MainWindow)
        self.actionSet_Serial_Port.setObjectName(u"actionSet_Serial_Port")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 90, 759, 276))
        font = QFont()
        font.setBold(False)
        self.layoutWidget.setFont(font)
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 5, 1, 1)

        self.Left_UD_go_button = QPushButton(self.layoutWidget)
        self.Left_UD_go_button.setObjectName(u"Left_UD_go_button")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.Left_UD_go_button.setFont(font2)
        self.Left_UD_go_button.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_UD_go_button, 4, 9, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_15)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.Left_LR_position_slider = QSlider(self.layoutWidget)
        self.Left_LR_position_slider.setObjectName(u"Left_LR_position_slider")
        self.Left_LR_position_slider.setMinimum(-60)
        self.Left_LR_position_slider.setMaximum(60)
        self.Left_LR_position_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.Left_LR_position_slider)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 2, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.Left_UD_group_checkbox = QCheckBox(self.layoutWidget)
        self.Left_UD_group_checkbox.setObjectName(u"Left_UD_group_checkbox")
        self.Left_UD_group_checkbox.setFont(font2)
        self.Left_UD_group_checkbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_UD_group_checkbox, 4, 7, 1, 1)

        self.line_22 = QFrame(self.layoutWidget)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShadow(QFrame.Plain)
        self.line_22.setLineWidth(3)
        self.line_22.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_22, 8, 6, 1, 1)

        self.Left_LR_go_button = QPushButton(self.layoutWidget)
        self.Left_LR_go_button.setObjectName(u"Left_LR_go_button")
        self.Left_LR_go_button.setFont(font2)
        self.Left_LR_go_button.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_LR_go_button, 2, 9, 1, 1)

        self.Left_UD_go_button_2 = QPushButton(self.layoutWidget)
        self.Left_UD_go_button_2.setObjectName(u"Left_UD_go_button_2")
        self.Left_UD_go_button_2.setFont(font2)
        self.Left_UD_go_button_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_UD_go_button_2, 6, 9, 1, 1)

        self.Left_UD_go_button_3 = QPushButton(self.layoutWidget)
        self.Left_UD_go_button_3.setObjectName(u"Left_UD_go_button_3")
        self.Left_UD_go_button_3.setFont(font2)
        self.Left_UD_go_button_3.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_UD_go_button_3, 8, 9, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_21 = QLabel(self.layoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_21)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)

        self.label_22 = QLabel(self.layoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_22)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.Left_UD_speed_slider = QSlider(self.layoutWidget)
        self.Left_UD_speed_slider.setObjectName(u"Left_UD_speed_slider")
        self.Left_UD_speed_slider.setMinimum(0)
        self.Left_UD_speed_slider.setMaximum(30)
        self.Left_UD_speed_slider.setOrientation(Qt.Horizontal)
        self.Left_UD_speed_slider.setInvertedAppearance(True)
        self.Left_UD_speed_slider.setInvertedControls(False)

        self.verticalLayout_6.addWidget(self.Left_UD_speed_slider)


        self.gridLayout.addLayout(self.verticalLayout_6, 4, 5, 1, 1)

        self.line_6 = QFrame(self.layoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_6, 4, 6, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_18)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_19)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_20)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.Left_UD_position_slider = QSlider(self.layoutWidget)
        self.Left_UD_position_slider.setObjectName(u"Left_UD_position_slider")
        self.Left_UD_position_slider.setMinimum(-45)
        self.Left_UD_position_slider.setMaximum(45)
        self.Left_UD_position_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.Left_UD_position_slider)


        self.gridLayout.addLayout(self.verticalLayout_5, 4, 2, 1, 1)

        self.line_7 = QFrame(self.layoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_7, 2, 6, 1, 1)

        self.line_16 = QFrame(self.layoutWidget)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShadow(QFrame.Plain)
        self.line_16.setLineWidth(3)
        self.line_16.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_16, 1, 0, 1, 10)

        self.line_20 = QFrame(self.layoutWidget)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShadow(QFrame.Plain)
        self.line_20.setLineWidth(3)
        self.line_20.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_20, 6, 8, 1, 1)

        self.line_19 = QFrame(self.layoutWidget)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShadow(QFrame.Plain)
        self.line_19.setLineWidth(3)
        self.line_19.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_19, 6, 6, 1, 1)

        self.Left_UD_spinbox_3 = QSpinBox(self.layoutWidget)
        self.Left_UD_spinbox_3.setObjectName(u"Left_UD_spinbox_3")
        self.Left_UD_spinbox_3.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Left_UD_spinbox_3.setMinimum(-45)
        self.Left_UD_spinbox_3.setMaximum(45)

        self.gridLayout.addWidget(self.Left_UD_spinbox_3, 8, 3, 1, 1)

        self.line_11 = QFrame(self.layoutWidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_11, 0, 1, 1, 1)

        self.Left_LR_spinbox = QSpinBox(self.layoutWidget)
        self.Left_LR_spinbox.setObjectName(u"Left_LR_spinbox")
        self.Left_LR_spinbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Left_LR_spinbox.setMinimum(-60)
        self.Left_LR_spinbox.setMaximum(60)

        self.gridLayout.addWidget(self.Left_LR_spinbox, 2, 3, 1, 1)

        self.Left_LR_group_checkbox = QCheckBox(self.layoutWidget)
        self.Left_LR_group_checkbox.setObjectName(u"Left_LR_group_checkbox")
        self.Left_LR_group_checkbox.setFont(font2)
        self.Left_LR_group_checkbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_LR_group_checkbox, 2, 7, 1, 1)

        self.line_8 = QFrame(self.layoutWidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_8, 4, 4, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_26 = QLabel(self.layoutWidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_26)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)

        self.label_27 = QLabel(self.layoutWidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_27)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.Left_UD_speed_slider_2 = QSlider(self.layoutWidget)
        self.Left_UD_speed_slider_2.setObjectName(u"Left_UD_speed_slider_2")
        self.Left_UD_speed_slider_2.setMinimum(0)
        self.Left_UD_speed_slider_2.setMaximum(30)
        self.Left_UD_speed_slider_2.setOrientation(Qt.Horizontal)
        self.Left_UD_speed_slider_2.setInvertedAppearance(True)
        self.Left_UD_speed_slider_2.setInvertedControls(False)

        self.verticalLayout_8.addWidget(self.Left_UD_speed_slider_2)


        self.gridLayout.addLayout(self.verticalLayout_8, 6, 5, 1, 1)

        self.line_4 = QFrame(self.layoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_4, 4, 1, 1, 1)

        self.line_12 = QFrame(self.layoutWidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShadow(QFrame.Plain)
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_12, 0, 8, 1, 1)

        self.line_5 = QFrame(self.layoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_5, 4, 8, 1, 1)

        self.line_21 = QFrame(self.layoutWidget)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShadow(QFrame.Plain)
        self.line_21.setLineWidth(3)
        self.line_21.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_21, 8, 8, 1, 1)

        self.line_15 = QFrame(self.layoutWidget)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShadow(QFrame.Plain)
        self.line_15.setLineWidth(3)
        self.line_15.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_15, 5, 0, 1, 10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_28 = QLabel(self.layoutWidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_28)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)

        self.label_29 = QLabel(self.layoutWidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_29)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)

        self.label_30 = QLabel(self.layoutWidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_30)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.Left_UD_position_slider_3 = QSlider(self.layoutWidget)
        self.Left_UD_position_slider_3.setObjectName(u"Left_UD_position_slider_3")
        self.Left_UD_position_slider_3.setMinimum(-45)
        self.Left_UD_position_slider_3.setMaximum(45)
        self.Left_UD_position_slider_3.setOrientation(Qt.Horizontal)

        self.verticalLayout_9.addWidget(self.Left_UD_position_slider_3)


        self.gridLayout.addLayout(self.verticalLayout_9, 8, 2, 1, 1)

        self.line_24 = QFrame(self.layoutWidget)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShadow(QFrame.Plain)
        self.line_24.setLineWidth(3)
        self.line_24.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_24, 8, 1, 1, 1)

        self.line_18 = QFrame(self.layoutWidget)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShadow(QFrame.Plain)
        self.line_18.setLineWidth(3)
        self.line_18.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_18, 6, 4, 1, 1)

        self.Left_UD_group_checkbox_2 = QCheckBox(self.layoutWidget)
        self.Left_UD_group_checkbox_2.setObjectName(u"Left_UD_group_checkbox_2")
        self.Left_UD_group_checkbox_2.setFont(font2)
        self.Left_UD_group_checkbox_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_UD_group_checkbox_2, 6, 7, 1, 1)

        self.line_23 = QFrame(self.layoutWidget)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShadow(QFrame.Plain)
        self.line_23.setLineWidth(3)
        self.line_23.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_23, 8, 4, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.HLine)

        self.horizontalLayout_6.addWidget(self.line_2)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.Left_UD_spinbox_2 = QSpinBox(self.layoutWidget)
        self.Left_UD_spinbox_2.setObjectName(u"Left_UD_spinbox_2")
        self.Left_UD_spinbox_2.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Left_UD_spinbox_2.setMinimum(-45)
        self.Left_UD_spinbox_2.setMaximum(45)

        self.gridLayout.addWidget(self.Left_UD_spinbox_2, 6, 3, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_31 = QLabel(self.layoutWidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_31)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)

        self.label_32 = QLabel(self.layoutWidget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_32)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.Left_UD_speed_slider_3 = QSlider(self.layoutWidget)
        self.Left_UD_speed_slider_3.setObjectName(u"Left_UD_speed_slider_3")
        self.Left_UD_speed_slider_3.setMinimum(0)
        self.Left_UD_speed_slider_3.setMaximum(30)
        self.Left_UD_speed_slider_3.setOrientation(Qt.Horizontal)
        self.Left_UD_speed_slider_3.setInvertedAppearance(True)
        self.Left_UD_speed_slider_3.setInvertedControls(False)

        self.verticalLayout_10.addWidget(self.Left_UD_speed_slider_3)


        self.gridLayout.addLayout(self.verticalLayout_10, 8, 5, 1, 1)

        self.Left_UD_group_checkbox_3 = QCheckBox(self.layoutWidget)
        self.Left_UD_group_checkbox_3.setObjectName(u"Left_UD_group_checkbox_3")
        self.Left_UD_group_checkbox_3.setFont(font2)
        self.Left_UD_group_checkbox_3.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.Left_UD_group_checkbox_3, 8, 7, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_16)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_17)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.Left_LR_speed_slider = QSlider(self.layoutWidget)
        self.Left_LR_speed_slider.setObjectName(u"Left_LR_speed_slider")
        self.Left_LR_speed_slider.setMinimum(0)
        self.Left_LR_speed_slider.setMaximum(30)
        self.Left_LR_speed_slider.setOrientation(Qt.Horizontal)
        self.Left_LR_speed_slider.setInvertedAppearance(True)
        self.Left_LR_speed_slider.setInvertedControls(False)

        self.verticalLayout_4.addWidget(self.Left_LR_speed_slider)


        self.gridLayout.addLayout(self.verticalLayout_4, 2, 5, 1, 1)

        self.line_14 = QFrame(self.layoutWidget)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShadow(QFrame.Plain)
        self.line_14.setLineWidth(3)
        self.line_14.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_14, 0, 4, 1, 1)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 10)

        self.Left_UD_spinbox = QSpinBox(self.layoutWidget)
        self.Left_UD_spinbox.setObjectName(u"Left_UD_spinbox")
        self.Left_UD_spinbox.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.Left_UD_spinbox.setMinimum(-45)
        self.Left_UD_spinbox.setMaximum(45)

        self.gridLayout.addWidget(self.Left_UD_spinbox, 4, 3, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_23 = QLabel(self.layoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_23)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_12)

        self.label_24 = QLabel(self.layoutWidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_24)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)

        self.label_25 = QLabel(self.layoutWidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_25)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.Left_UD_position_slider_2 = QSlider(self.layoutWidget)
        self.Left_UD_position_slider_2.setObjectName(u"Left_UD_position_slider_2")
        self.Left_UD_position_slider_2.setMinimum(-45)
        self.Left_UD_position_slider_2.setMaximum(45)
        self.Left_UD_position_slider_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.Left_UD_position_slider_2)


        self.gridLayout.addLayout(self.verticalLayout_7, 6, 2, 1, 1)

        self.line_17 = QFrame(self.layoutWidget)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShadow(QFrame.Plain)
        self.line_17.setLineWidth(3)
        self.line_17.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_17, 6, 1, 1, 1)

        self.line_13 = QFrame(self.layoutWidget)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShadow(QFrame.Plain)
        self.line_13.setLineWidth(3)
        self.line_13.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_13, 0, 6, 1, 1)

        self.line_10 = QFrame(self.layoutWidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_10, 2, 8, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_3, 2, 1, 1, 1)

        self.line_9 = QFrame(self.layoutWidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QFrame.VLine)

        self.gridLayout.addWidget(self.line_9, 2, 4, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.line_25 = QFrame(self.layoutWidget)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShadow(QFrame.Plain)
        self.line_25.setLineWidth(3)
        self.line_25.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line_25, 7, 0, 1, 8)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 888, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSet_Serial_Port)
        self.menuFile.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.Left_LR_position_slider.sliderMoved.connect(self.Left_LR_spinbox.setValue)
        self.Left_LR_spinbox.valueChanged.connect(self.Left_LR_position_slider.setValue)
        self.Left_UD_position_slider.sliderMoved.connect(self.Left_UD_spinbox.setValue)
        self.Left_UD_spinbox.valueChanged.connect(self.Left_UD_position_slider.setValue)
        self.Left_UD_position_slider_3.valueChanged.connect(self.Left_UD_spinbox_3.setValue)
        self.Left_UD_spinbox_3.valueChanged.connect(self.Left_UD_position_slider_3.setValue)
        self.Left_UD_position_slider_2.valueChanged.connect(self.Left_UD_spinbox_2.setValue)
        self.Left_UD_spinbox_2.valueChanged.connect(self.Left_UD_position_slider_2.setValue)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionSet_Serial_Port.setText(QCoreApplication.translate("MainWindow", u"Set Serial Port", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.Left_UD_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"-60", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"+60", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Eyelid", None))
        self.Left_UD_group_checkbox.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.Left_LR_go_button.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.Left_UD_go_button_2.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.Left_UD_go_button_3.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Eyebrow", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.Left_LR_group_checkbox.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.Left_UD_group_checkbox_2.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LEFT/RIGHT", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Left_UD_group_checkbox_3.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"-45", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"UP/DOWN", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

