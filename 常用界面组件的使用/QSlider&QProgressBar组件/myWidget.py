import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtGui import
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

		self.ui.slider.setMaximum(200)#设置输入的最大范围，setMinimum是最小范围
		self.ui.scrollBar.setMaximum(200)
		self.ui.progressBar.setMaximum(200)
		self.ui.slider.valueChanged.connect(self.do_valueChanged)#自定义连接
		self.ui.scrollBar.valueChanged.connect(self.do_valueChanged)
	##==========自定义功能函数==========
	def do_valueChanged(self,value):
		self.ui.progressBar.setValue(value)

	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====
	def on_radio_Percent_clicked(self):#显示百分比
		self.ui.progressBar.setFormat('%p%')

	def on_radio_Value_clicked(self):
		self.ui.progressBar.setFormat('%v')
	@pyqtSlot(bool)
	def on_chkBox_Visible_clicked(self,checked):
		self.ui.progressBar.setTextVisible(checked)

	@pyqtSlot(bool)
	def on_chkBox_Inverted_clicked(self,checked):
		self.ui.progressBar.setInvertedAppearance(checked)


	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyWidget()
	form.show()

	sys.exit(app.exec_())