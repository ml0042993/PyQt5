import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
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
	def on_btnIniItems_clicked(self):#初始化按键
		icon = QIcon(':/icons/images/aim.ico')
		self.ui.comboBox.clear()
		provinces = ["山东","河北","河南","湖北","湖南","广东",]
		for i in range(len(provinces)):
			#addItem()是一个overload型函数,用于将添加一个项到列表里,有两种原型定义:
			#addItem(self,str,userDate:Any = None)不带图标,用户数据自定
			#addItem(self,QIcon,str,userDate:Any = None)#带图标,用户数据自定
			self.ui.comboBox.addItem(icon,provinces[i])
	@pyqtSlot(bool)
	def on_chkBoxEditable_clicked(self,checked):#可编辑组件:可以在界面中添加新条目,无图标
		self.ui.comboBox.setEditable(checked)
	def on_btnClearItems_clicked(self):#清空列表
		self.ui.comboBox.clear()

	@pyqtSlot(str)
	def on_comboBox_currentIndexChanged(self,curText):
		'''
		当QComboBox组件上的选择项发生变化时会发射currentIndexChanged信号,该信号事一个overload型信号,包括:
		currentIndexChanged(int),该信号发射的是索引号
		currentIndexChanged(str).该信号发射的是当前的文字
		:param curText:
		:return:
		'''
		self.ui.lineEdit.setText(curText)

	def on_btnIni2_clicked(self):
		'''
		设置带有用户数据的列表,用户数据不会在界面组件中显示,如果需要使用需要使用currentData()函数调用
		:return:
		'''
		icon = QIcon(':/icons/images/unit.ico')
		self.ui.comboBox_2.clear()
		cities = {'北京':10,'上海':21,'天津':22,'徐州':516,'青岛':532}
		for k,v in cities.items():
			self.ui.comboBox_2.addItem(icon,k,v)

	@pyqtSlot(str)
	def on_comboBox_2_currentIndexChanged(self,curText):
		self.ui.lineEdit.setText(curText)
		zone = self.ui.comboBox_2.currentData()#zone是用户数据,可能会出现None的情况
		# print(zone)
		if zone != None:
			self.ui.lineEdit.setText(curText+':区号={}'.format(zone))
	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyWidget()
	form.show()

	sys.exit(app.exec_())