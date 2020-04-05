import sys
from PyQt5.QtWidgets import QApplication,QWidget,QAbstractItemView
from PyQt5.QtCore import QStringListModel,Qt,pyqtSlot
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

		self.__provinces=['北京','上海','天津','河北','山东','四川','重庆','广东','河南']

		self.model = QStringListModel(self)
		self.model.setStringList(self.__provinces)

		self.ui.listView.setModel(self.model)
		#设置QListView的项是否可以编辑，以及如何进入编辑状态
		self.ui.listView.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.SelectedClicked)#设置编辑模式

	##==========自定义功能函数==========

	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====
	@pyqtSlot()
	def on_btnAdd_clicked(self):
		self.row = self.model.rowCount()#行数
		print(self.row)
		self.model.insertRow(self.row)#在行尾加入一个空行，没有文字
		index = self.model.index(self.row,0)#0是列，获取最后一行的modelIndex
		print(index)
		self.model.setData(index,"new item",Qt.DisplayRole)#添加名称，设置项的角色
		self.ui.listView.setCurrentIndex(index)#选择当前行

	@pyqtSlot()
	def on_btnInsert_clicked(self):
		'''
		插入行
		:return:
		'''
		index = self.ui.listView.currentIndex()
		self.model.insertRow(index.row())
		self.model.setData(index,"insert item",Qt.DisplayRole)
		self.ui.listView.setCurrentIndex(index)

	@pyqtSlot()
	def on_btnDel_clicked(self):
		'''
		删除行
		:return:
		'''
		index = self.ui.listView.currentIndex()
		self.model.removeRow(index.row())

	@pyqtSlot()
	def on_btnClear_clicked(self):
		'''
		清除列表
		removeRows()从行号row开始删除count（几）行
		:return:
		'''
		count = self.model.rowCount()
		self.model.removeRows(0,count)

	@pyqtSlot()
	def on_btnStringList_clicked(self):
		strlist = self.model.stringList()
		self.ui.plainTextEdit.clear()
		for strline in strlist:
			self.ui.plainTextEdit.appendPlainText(strline)

	def on_listView_clicked(self,index):
		self.ui.label.setText("当前项 index: row = %d, column = %d"%(index.row(),index.column()))
	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyWidget()
	form.show()

	sys.exit(app.exec_())