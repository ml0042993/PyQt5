import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt
# from PyQt5.QtGui import
# from PyQt5.QtWidgets import
# from PyQt5.QtSql import
# from PyQt5.QtMultimedia import
# from PyQt5.QtMultimediaWidgets import

from ui_Widget import Ui_Widget

class QMyLabel(QLabel):
	doubleClicked = pyqtSignal()
	def mouseDoubleClickEvent(self, event):
		self.doubleClicked.emit()

class QmyWidget(QWidget):
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建窗体
		self.ui = Ui_Widget()#创建Ui对象
		self.ui.setupUi(self)#构造UI

		self.resize(280,150)

		labHello = QMyLabel(self)
		labHello.setText("hit me")
		font = labHello.font()
		font.setPointSize(14)
		font.setBold(True)
		labHello.setFont(font)
		size = labHello.sizeHint()
		labHello.setGeometry(70,60,size.width(),size.height())
		labHello.doubleClicked.connect(self.do_doubleClicked)

	def do_doubleClicked(self):
		print('标签被双击')
	def mouseDoubleClickEvent(self, event):
		print("窗口双击事件响应")

	##==========自定义功能函数==========

	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyWidget()
	form.show()

	sys.exit(app.exec_())