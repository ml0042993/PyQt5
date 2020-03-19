#退出主程序窗口

import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow,QHBoxLayout,QWidget,QPushButton
#QHBoxLayout水平布局,QPushButton按钮类
from PyQt5.QtGui import QIcon


class QuitApp(QMainWindow):
	def __init__(self):
		super().__init__()
		self.resize(300,300)
		self.setWindowTitle('退出程序')
		#创建一个Button按钮
		self.button1=QPushButton('exit')
		#信号与槽绑定
		self.button1.clicked.connect(self.onClick_Button)
		#创建水平布局layout

		layout = QHBoxLayout()
		#水平布局上加入按钮button1
		layout.addWidget(self.button1)
		#创建主画布mainFrame
		mainFrame = QWidget()
		#将水平布局layout(现在已经包括了按钮)放入主画布mainFrame中
		mainFrame.setLayout(layout)
		#将主画布放入到窗口上
		self.setCentralWidget(mainFrame)
	#创建按钮点击事件函数(自定义的槽)
	def onClick_Button(self):
		sender = self.sender()
		print(sender.text())
		#QApplication对象的指针可以通过instance()函数
		app = QApplication.instance()
		print(app.__doc__)
		app.quit()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = QuitApp()
	# main.center()#也可在此处调用
	main.show()
	sys.exit(app.exec_())
