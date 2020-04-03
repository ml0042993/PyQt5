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
        Widget.resize(565, 370)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(Widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnInsert = QtWidgets.QPushButton(self.groupBox)
        self.btnInsert.setObjectName("btnInsert")
        self.gridLayout_2.addWidget(self.btnInsert, 1, 1, 1, 1)
        self.btnAdd = QtWidgets.QPushButton(self.groupBox)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout_2.addWidget(self.btnAdd, 1, 0, 1, 1)
        self.btnClear = QtWidgets.QPushButton(self.groupBox)
        self.btnClear.setObjectName("btnClear")
        self.gridLayout_2.addWidget(self.btnClear, 2, 1, 1, 1)
        self.btnReset = QtWidgets.QPushButton(self.groupBox)
        self.btnReset.setObjectName("btnReset")
        self.gridLayout_2.addWidget(self.btnReset, 0, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setObjectName("listView")
        self.gridLayout_2.addWidget(self.listView, 4, 0, 1, 2)
        self.btnDel = QtWidgets.QPushButton(self.groupBox)
        self.btnDel.setObjectName("btnDel")
        self.gridLayout_2.addWidget(self.btnDel, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnClearText = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClearText.setObjectName("btnClearText")
        self.verticalLayout_2.addWidget(self.btnClearText)
        self.btnStringList = QtWidgets.QPushButton(self.groupBox_2)
        self.btnStringList.setObjectName("btnStringList")
        self.verticalLayout_2.addWidget(self.btnStringList)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.verticalLayout_3.addWidget(self.splitter)
        self.groupBox_3 = QtWidgets.QGroupBox(Widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.groupBox.setTitle(_translate("Widget", "GroupBox"))
        self.btnInsert.setText(_translate("Widget", "插入项"))
        self.btnAdd.setText(_translate("Widget", "添加项"))
        self.btnClear.setText(_translate("Widget", "清空列表"))
        self.btnReset.setText(_translate("Widget", "恢复列表"))
        self.btnDel.setText(_translate("Widget", "删除当前项"))
        self.groupBox_2.setTitle(_translate("Widget", "GroupBox"))
        self.btnClearText.setText(_translate("Widget", "清空文本"))
        self.btnStringList.setText(_translate("Widget", "显示数据模型的StringList"))
        self.groupBox_3.setTitle(_translate("Widget", "GroupBox"))
        self.label.setText(_translate("Widget", "TextLabel"))
