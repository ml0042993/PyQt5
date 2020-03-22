#窗体业务逻辑类文件
#与UI窗体类对应的业务逻辑

import sys
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5 import QtCore#包含pyqtSolt

from PyQt5.QtCore import Qt
from ui_Dialog import Ui_Dialog
from PyQt5.QtGui import QPalette

class QmyDialog(QDialog):
    def __init__(self):
        super().__init__()#调用父类构造函数，创建窗体
        self.ui = Ui_Dialog()#创建UI对象
        self.ui.setupUi(self)#构造UI
        #将clicked（）信号与统一个槽函数do_set_TextColor（）关联
        self.ui.radioBlack.clicked.connect(self.do_set_TextColor)
        self.ui.radioRed.clicked.connect(self.do_set_TextColor)
        self.ui.radioBlue.clicked.connect(self.do_set_TextColor)

    def on_btnClear_clicked(self):
        #清空
        self.ui.TextEdit.clear()#注意命名要和ui_Dialog内的命名一致

    def on_checkBoxBold_toggled(self,checked):
        #加粗，checked是勾选状态是一个bool型
        print(checked)
        font =self.ui.TextEdit.font()
        # print(font)
        font.setBold(checked)
        self.ui.TextEdit.setFont(font)
    def on_checkBoxUnder_clicked(self):
        #下划线
        checked = self.ui.checkBoxUnder.isChecked()#获取勾选状态,bool型
        # print(checked)
        font = self.ui.TextEdit.font()
        font.setUnderline(checked)
        self.ui.TextEdit.setFont(font)
    @QtCore.pyqtSlot(bool)#书上未说明要导入QtCore
    #该修饰符的作用是将函数的参数类型声明清楚，让函数明确使用的是哪一种信号（clicked（）或者是clicked(bool），这里用于区分overload型信号的选择
    def on_checkBoxItalic_clicked(self,checked):#添加新功能
        # print(checked)
        font = self.ui.TextEdit.font()
        # print(font)
        font.setItalic(checked)
        # print(12)
        self.ui.TextEdit.setFont(font)
        # print(13)

    def do_set_TextColor(self):
        #添加自定义槽函数
        plet = self.ui.TextEdit.palette()#获取调色板palette（）
        if (self.ui.radioBlack.isChecked()):#isChecked是否选取
            plet.setColor(QPalette.Text,Qt.black) #black
        elif(self.ui.radioRed.isChecked()):
            plet.setColor(QPalette.Text, Qt.red)
        elif(self.ui.radioBlue.isChecked()):
            plet.setColor(QPalette.Text, Qt.blue)
        self.ui.TextEdit.setPalette(plet)#设置颜色

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form =QmyDialog()
    form.show()
    sys.exit(app.exec_())