# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_FormHello.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormHello(object):
    def setupUi(self, FormHello):
        FormHello.setObjectName("FormHello")
        FormHello.resize(400, 300)
        self.btnClose = QtWidgets.QPushButton(FormHello)
        self.btnClose.setGeometry(QtCore.QRect(150, 160, 75, 23))
        self.btnClose.setObjectName("btnClose")
        self.labelHello = QtWidgets.QLabel(FormHello)
        self.labelHello.setGeometry(QtCore.QRect(120, 120, 141, 16))
        self.labelHello.setObjectName("labelHello")

        self.retranslateUi(FormHello)
        QtCore.QMetaObject.connectSlotsByName(FormHello)

    def retranslateUi(self, FormHello):
        _translate = QtCore.QCoreApplication.translate
        FormHello.setWindowTitle(_translate("FormHello", "Form"))
        self.btnClose.setText(_translate("FormHello", "关闭"))
        self.labelHello.setText(_translate("FormHello", "Hello,by UI Designer"))
