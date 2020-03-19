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
		self.center()#调用定义函数

	def center(self):
		'''
		系统默认窗口居中,该方法可以修改窗口打开的出现位置,其窗口的坐标以左上角为基准点
		'''
		#获取屏幕坐标系
		screen = QDesktopWidget().screenGeometry()
		#获取窗口坐标系
		size = self.geometry()

		#居中屏幕的左边的X坐标
		left = (screen.width() - size.width())/2
		top = (screen.height() - size.height())/2

		self.move(left,top)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = CenterForm()
	# main.center()#也可在此处调用
	main.show()
	sys.exit(app.exec_())
