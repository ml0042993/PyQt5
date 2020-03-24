import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import pyqtSlot,Qt
# from PyQt5.QtGui import QFont
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

	'''
	editInput：为QLineEdit组件名称
	setAlignment()：设置对齐方式
	'''
	def on_btnAlign_Left_clicked(self):#居左
		self.ui.editInput.setAlignment(Qt.AlignLeft)
	def on_btnAlign_Center_clicked(self):#居中
		self.ui.editInput.setAlignment(Qt.AlignCenter)
	def on_btnAlign_Right_clicked(self):#居右
		self.ui.editInput.setAlignment(Qt.AlignRight)

	@pyqtSlot(bool)
	def on_btnFont_Bold_clicked(self,checked):#粗体
		font = self.ui.editInput.font()#获取字体对象
		font.setBold(checked)#checked=True，即当参数为真时，setBold()将font设置为粗体
		self.ui.editInput.setFont(font)#设置字体
	@pyqtSlot(bool)
	def on_btnFont_Italic_clicked(self,checked):#斜体
		font = self.ui.editInput.font()
		font.setItalic(checked)
		self.ui.editInput.setFont(font)
	@pyqtSlot(bool)
	def on_btnFont_UnderLine_clicked(self,checked):#下划线
		font = self.ui.editInput.font()
		font.setUnderline(checked)
		self.ui.editInput.setFont(font)

	@pyqtSlot(bool)
	def on_chkBox_Readonly_clicked(self,checked):#只读
		self.ui.editInput.setReadOnly(checked)
	@pyqtSlot(bool)
	def on_chkBox_Enable_clicked(self,checked):#锁定QLineEdit组件
		self.ui.editInput.setEnabled(checked)
	@pyqtSlot(bool)
	def on_chkBox_ClearButton_clicked(self,checked):#聚焦后清除原有内容
		self.ui.editInput.setClearButtonEnabled(checked)
	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyWidget()
	form.show()

	sys.exit(app.exec_())