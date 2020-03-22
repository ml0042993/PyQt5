# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(368, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBoxUnder = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.checkBoxUnder.setFont(font)
        self.checkBoxUnder.setObjectName("checkBoxUnder")
        self.horizontalLayout_2.addWidget(self.checkBoxUnder)
        self.checkBoxBold = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxBold.setObjectName("checkBoxBold")
        self.horizontalLayout_2.addWidget(self.checkBoxBold)
        self.checkBoxItalic = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxItalic.setObjectName("checkBoxItalic")
        self.horizontalLayout_2.addWidget(self.checkBoxItalic)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioBlack = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioBlack.setObjectName("radioBlack")
        self.horizontalLayout_3.addWidget(self.radioBlack)
        self.radioBlue = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioBlue.setObjectName("radioBlue")
        self.horizontalLayout_3.addWidget(self.radioBlue)
        self.radioRed = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioRed.setObjectName("radioRed")
        self.horizontalLayout_3.addWidget(self.radioRed)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.TextEdit = QtWidgets.QPlainTextEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.TextEdit.setFont(font)
        self.TextEdit.setObjectName("TextEdit")
        self.verticalLayout.addWidget(self.TextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnClear = QtWidgets.QPushButton(Dialog)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout.addWidget(self.btnOk)
        self.btnClose = QtWidgets.QPushButton(Dialog)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.btnOk.clicked.connect(Dialog.accept)
        self.btnClose.clicked.connect(Dialog.close)
        #QMetaObject元类，功能为搜索Diagol上的所有从属组件，将匹配的信号和槽函数关联
        #所设定的函数格式为on_<object name>_<signal_name>(<signal parameters>)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "信号与槽"))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox"))
        self.checkBoxUnder.setText(_translate("Dialog", "Underline"))
        self.checkBoxBold.setText(_translate("Dialog", "Bold"))
        self.checkBoxItalic.setText(_translate("Dialog", "Italic"))
        self.groupBox_2.setTitle(_translate("Dialog", "GroupBox"))
        self.radioBlack.setText(_translate("Dialog", "Black"))
        self.radioBlue.setText(_translate("Dialog", "Blue"))
        self.radioRed.setText(_translate("Dialog", "Red"))
        self.TextEdit.setPlainText(_translate("Dialog", "PyQt5 编程指南\n"
"python 和 Qt\n"
""))
        self.btnClear.setText(_translate("Dialog", "清空"))
        self.btnOk.setText(_translate("Dialog", "确定"))
        self.btnClose.setText(_translate("Dialog", "退出"))
