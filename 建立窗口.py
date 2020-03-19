import sys

from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
	#创建QAPPlication类的实例
	app =QApplication(sys.argv)
	#创建一个窗口
	widget = QWidget()
	#设置窗口大小
	widget.resize(400,200)
	#移动窗口
	widget.move(300,300)

	#设置标题
	widget.setWindowTitle('窗口实例')
	#显示窗口
	widget.show()
	#进入程序主循环,并通过exit函数确保主循环能够安全结束
	sys.exit(app.exec_())

