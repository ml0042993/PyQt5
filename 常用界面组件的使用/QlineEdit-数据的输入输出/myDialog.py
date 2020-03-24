import sys
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtGui import
# from PyQt5.QtWidgets import
# from PyQt5.QtSql import
# from PyQt5.QtMultimedia import
# from PyQt5.QtMultimediaWidgets import

from ui_Dialog import Ui_Dialog

class QmyDialog(QDialog):
	'''
	text()是获取文本内容
	setText()是设置文本内容
	value()是获取数值int或者float型
	setValue()是赋值
	'''
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建窗体
		self.ui = Ui_Dialog()#创建Ui对象
		self.ui.setupUi(self)#构造UI
	##==========自定义功能函数==========

	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====
	def on_pushButton_clicked(self):
		num = int(self.ui.lineEdit.text())
		price = float(self.ui.lineEdit_2.text())
		total = num*price
		self.ui.lineEdit_3.setText('{}'.format(total))
	@pyqtSlot(int)
	def on_spinBox_valueChanged(self,count):
		price = self.ui.doubleSpinBox.value()#doubleSpinBox是单价spin框的名称
		self.ui.doubleSpinBox_2.setValue(count*price)#doubleSpinBox_2是自动计价的显示框
	@pyqtSlot(float)
	def on_doubleSpinBox_valueChanged(self,price):
		count = self.ui.spinBox.value()#spinBox是数量的spin框的名称
		self.ui.doubleSpinBox_2.setValue(count*price)


	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyDialog()
	form.show()

	sys.exit(app.exec_())