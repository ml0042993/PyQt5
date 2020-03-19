# 令主窗口居中

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):  # 继承主窗口
	def __init__(self):  # parent=None保证了QMainWindow是主窗口
		super().__init__()

		# 设置主窗口标题
		self.setWindowTitle('窗口居中')
		# 设置尺寸
		self.resize(400, 300)

	def center(self):
		#获取屏幕坐标系
		screen = QDesktopWidget().screenFeometry()
		#获取窗口坐标系
		size = self.geometry()

		#居中屏幕的左边的X坐标
		left = (screen.width() - size.width())/2
		top = (screen.height() - size.height())/2

		self.move(left,top)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = CenterForm()
	main.show()
	sys.exit(app.exec_())
