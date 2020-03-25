# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(302, 206)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setEnabled(True)
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnStart = QtWidgets.QPushButton(self.groupBox)
        self.btnStart.setObjectName("btnStart")
        self.gridLayout.addWidget(self.btnStart, 0, 0, 1, 1)
        self.btnStop = QtWidgets.QPushButton(self.groupBox)
        self.btnStop.setEnabled(False)
        self.btnStop.setObjectName("btnStop")
        self.gridLayout.addWidget(self.btnStop, 0, 1, 1, 1)
        self.btnSetIntv = QtWidgets.QPushButton(self.groupBox)
        self.btnSetIntv.setObjectName("btnSetIntv")
        self.gridLayout.addWidget(self.btnSetIntv, 1, 0, 1, 1)
        self.spinBoxIntv = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxIntv.setMaximum(9999)
        self.spinBoxIntv.setProperty("value", 1000)
        self.spinBoxIntv.setObjectName("spinBoxIntv")
        self.gridLayout.addWidget(self.spinBoxIntv, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LCDHour = QtWidgets.QLCDNumber(self.groupBox_2)
        self.LCDHour.setSmallDecimalPoint(False)
        self.LCDHour.setDigitCount(2)
        self.LCDHour.setProperty("value", 10.0)
        self.LCDHour.setObjectName("LCDHour")
        self.horizontalLayout.addWidget(self.LCDHour)
        self.LCDMin = QtWidgets.QLCDNumber(self.groupBox_2)
        self.LCDMin.setDigitCount(2)
        self.LCDMin.setProperty("value", 26.0)
        self.LCDMin.setProperty("intValue", 26)
        self.LCDMin.setObjectName("LCDMin")
        self.horizontalLayout.addWidget(self.LCDMin)
        self.LCDSec = QtWidgets.QLCDNumber(self.groupBox_2)
        self.LCDSec.setDigitCount(2)
        self.LCDSec.setProperty("value", 10.0)
        self.LCDSec.setObjectName("LCDSec")
        self.horizontalLayout.addWidget(self.LCDSec)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.LabElapsedTime = QtWidgets.QLabel(Widget)
        self.LabElapsedTime.setMaximumSize(QtCore.QSize(16777215, 50))
        self.LabElapsedTime.setObjectName("LabElapsedTime")
        self.verticalLayout_2.addWidget(self.LabElapsedTime)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.groupBox.setTitle(_translate("Widget", "定时器"))
        self.btnStart.setText(_translate("Widget", "开始"))
        self.btnStop.setText(_translate("Widget", "停止"))
        self.btnSetIntv.setText(_translate("Widget", "设置周期"))
        self.spinBoxIntv.setSuffix(_translate("Widget", " ms"))
        self.groupBox_2.setTitle(_translate("Widget", "当前时间(小时:分:秒)"))
        self.LabElapsedTime.setText(_translate("Widget", "流逝的时间"))
