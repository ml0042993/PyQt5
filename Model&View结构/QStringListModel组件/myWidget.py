import sys
from PyQt5.QtWidgets import QApplication,QWidget,QAbstractItemView
from PyQt5.QtCore import QStringListModel
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

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyWidget()
	form.show()

	sys.exit(app.exec_())