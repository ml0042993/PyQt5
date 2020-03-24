import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtGui import QFont
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

	##==========由connectSlotsByName()自动关联的槽函数====
	def on_btnAlign_Left_Clicked(self):
		self.ui.editInput.setAlignment(Qt.AlignLeft)
	def on_btnAlign_Center_Clicked(self):
		self.ui.editInput.setAlignment(Qt.AlignCenter)
	def on_btnAlign_Right_Clicked(self):
		self.ui.editInput.setAlignment(Qt.AlignRight)
	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyWidget()
	form.show()

	sys.exit(app.exec_())