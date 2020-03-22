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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form =QmyDialog()
    form.show()
    sys.exit(app.exec_())