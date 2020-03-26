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
        Widget.resize(477, 186)
        self.verticalLayout = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnIniItems = QtWidgets.QPushButton(self.groupBox_2)
        self.btnIniItems.setObjectName("btnIniItems")
        self.gridLayout.addWidget(self.btnIniItems, 0, 0, 1, 1)
        self.btnClearItems = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClearItems.setObjectName("btnClearItems")
        self.gridLayout.addWidget(self.btnClearItems, 0, 1, 1, 1)
        self.chkBoxEditable = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkBoxEditable.setObjectName("chkBoxEditable")
        self.gridLayout.addWidget(self.chkBoxEditable, 0, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 3)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnIni2 = QtWidgets.QPushButton(self.groupBox_3)
        self.btnIni2.setObjectName("btnIni2")
        self.verticalLayout_2.addWidget(self.btnIni2)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.groupBox.setTitle(_translate("Widget", "选择的内容"))
        self.groupBox_2.setTitle(_translate("Widget", "简单的ComboBox"))
        self.btnIniItems.setText(_translate("Widget", "初始化列表"))
        self.btnClearItems.setText(_translate("Widget", "清除列表"))
        self.chkBoxEditable.setText(_translate("Widget", "可编辑"))
        self.comboBox.setItemText(0, _translate("Widget", "北京市"))
        self.comboBox.setItemText(1, _translate("Widget", "上海市"))
        self.groupBox_3.setTitle(_translate("Widget", "有用户数据的ComboBox"))
        self.btnIni2.setText(_translate("Widget", "初始化城市+区号"))
import res_rc