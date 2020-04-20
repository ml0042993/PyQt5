import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt,QEvent
from PyQt5.QtGui import QPainter, QPixmap
# from PyQt5.QtWidgets import
# from PyQt5.QtSql import
# from PyQt5.QtMultimedia import
# from PyQt5.QtMultimediaWidgets import

from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建窗体
		self.ui = Ui_Widget()#创建Ui对象
		self.ui.setupUi(self)#构造UI
	##==========自定义功能函数==========

	##==========事件处理函数===========
	def paintEvent(self, event):
		'''
		paintEvent(),在界面需要重新绘制时触发，在此事件函数内可以实现一些自定义的绘制功能
		:param event:
		:return:
		'''
		painter = QPainter(self)
		pic = QPixmap("th.jpg")
		painter.drawPixmap(0,0,self.width(),self.height(),pic)
		super().paintEvent(event)

	def resizeEvent(self, event):
		'''
		resizeEvent()在窗体改变大小时触发
		:param event:
		:return:
		'''
		W = self.width()
		H = self.height()
		WBtn = self.ui.pushButton.width()
		HBtn = self.ui.pushButton.width()
		self.ui.pushButton.setGeometry((W-WBtn)/2,(H-HBtn)/2,WBtn,HBtn)
	def closeEvent(self, event):
		'''
		窗口关闭时触发
		:param event:
		:return:
		'''
		dlgTitle = "Qusetion消息框"
		strInfo = 'CloseEvent事件触发，确定要退出吗'
		defaultBtn = QMessageBox.NoButton
		result = QMessageBox.question(self,dlgTitle,strInfo,QMessageBox.Yes|QMessageBox.No,defaultBtn)
		if result == QMessageBox.Yes:
			event.accept()#关闭窗口
		else:
			event.ignore()#不关闭
	def mousePressEvent(self, event):
		pt = event.pos()
		if event.button() == Qt.LeftButton:
			self.ui.label.setText("(x,y)=(%d,%d)"%(pt.x(),pt.y()))
			rect = self.ui.label.geometry()
			self.ui.label.setGeometry(pt.x(),pt.y(),rect.width(),rect.height())
		super().mousePressEvent(event)

	def keyPressEvent(self, event):
		rect = self.ui.pushButton_2.geometry()

		if event.key() in set([Qt.Key_A,Qt.Key_Left]):
			self.ui.pushButton_2.setGeometry(rect.left()-20,rect.top(),rect.width(),rect.height())
		elif event.key() in set([Qt.Key_D,Qt.Key_Right]):
			self.ui.pushButton_2.setGeometry(rect.right()+20,rect.top(),rect.width(),rect.height())
		elif event.key() in set([Qt.Key_W,Qt.Key_Up]):
			self.ui.pushButton_2.setGeometry(rect.right(),rect.top()-20,rect.width(),rect.height())
		elif event.key() in set([Qt.Key_S,Qt.Key_Down]):
			self.ui.pushButton_2.setGeometry(rect.right(),rect.top()+20,rect.width(),rect.height())



	##==========由connectSlotsByName()自动关联的槽函数====

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyWidget()
	form.show()

	sys.exit(app.exec_())


