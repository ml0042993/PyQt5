#窗体业务逻辑类文件
#与UI窗体类对应的业务逻辑

import sys
from PyQt5.QtWidgets import QApplication,QDialog
from ui_Dialog import Ui_Dialog

class QmyDialog(QDialog):
    def __init__(self):
        super().__init__()#调用父类构造函数，创建窗体
        self.ui = Ui_Dialog()#创建UI对象
        self.ui.setupUi(self)#构造UI

    def on_btnClear_clicked(self):
        #清空
        self.ui.TextEdit.clear()#注意命名要和ui_Dialog内的命名一致

    def on_checkBoxBold_toggled(self,checked):
        #加粗，checked是勾选状态是一个bool型
        # print(checked)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form =QmyDialog()
    form.show()
    sys.exit(app.exec_())