import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):  # 继承主窗口
    def __init__(self):  # parent=None保证了QMainWindow是主窗口
        super().__init__()

        # 设置主窗口标题
        self.setWindowTitle('FirstMainWindow')
        # 设置尺寸
        self.resize(400, 300)
        self.status = self.statusBar()#定义下方状态栏
        self.status.showMessage('5秒后消失', 5000)#定义状态栏信息的内容和显示时间


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(''))#设置标题栏图标
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
