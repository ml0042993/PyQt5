import sys
from PyQt5.QtWidgets import QApplication,QWidget,QAbstractItemView,QTreeWidgetItem,QListWidget,QTreeWidget,QTableWidget
from PyQt5.QtCore import pyqtSlot,Qt,QEvent
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

		self.ui.listSource.installEventFilter(self)#listSource组件将窗体注册为事件监测者,self是指的QWidget窗口
		self.ui.listWidget.installEventFilter(self)
		self.ui.treeWidget.installEventFilter(self)
		self.ui.tableWidget.installEventFilter(self)
		'''
		任何一个节目组件都是QWidget的子类,通过调用setAcceptDrops(True)函数,可以使组件作为drop site接收放置操作
		'''
		self.ui.listSource.setAcceptDrops(True)#设置允许放置操作
		self.ui.listSource.setDragDropMode(QAbstractItemView.DragDrop)#设置拖放操作的模式,QAbstractItemView定义了拖放操作的各种函数
		self.ui.listSource.setDragEnabled(True)#
		self.ui.listSource.setDefaultDropAction(Qt.CopyAction)

		self.ui.listWidget.setAcceptDrops(True)
		self.ui.listWidget.setDragDropMode(QAbstractItemView.DragDrop)
		self.ui.listWidget.setDragEnabled(True)
		self.ui.listWidget.setDefaultDropAction(Qt.MoveAction)

		self.ui.treeWidget.setAcceptDrops(True)
		self.ui.treeWidget.setDragDropMode(QAbstractItemView.DragDrop)
		self.ui.treeWidget.setDragEnabled(True)
		self.ui.treeWidget.setDefaultDropAction(Qt.MoveAction)

		self.ui.tableWidget.setAcceptDrops(True)
		self.ui.tableWidget.setDragDropMode(QAbstractItemView.DragDrop)
		self.ui.tableWidget.setDragEnabled(True)
		self.ui.tableWidget.setDefaultDropAction(Qt.MoveAction)

	##==========自定义功能函数==========
	def __refreshToUI(self):
		'''
		acceptDrops()返回bool值，表示组件是否可以作为drop site接受放置操作
		dragEnabled()返回bool值，表示组件是否可以作为drag site启动拖放操作
		dragDropMode()返回枚举类型 QAbstractItemView.DragDropMode，表示拖放操作模式
		defaultDropAction()返回枚举类型 Qt.DrapAction 当组件作为drap site时，它表示在完成拖放操作时drag site组件的数据操作模式
		:return:
		'''
		self.ui.chkBox_AcceptDrops.setChecked(self.__itemView.acceptDrops())
		print(self.__itemView.dragDropMode())
		print(self.__itemView.defaultDropAction())
		self.ui.chkBox_DragEnabled.setChecked(self.__itemView.dragEnabled())
		self.ui.combo_Mode.setCurrentIndex(self.__itemView.dragDropMode())
		index = self.__getDropActionIndex(self.__itemView.defaultDropAction())
		self.ui.combo_DefaultAction.setCurrentIndex(index)

	def __getDropActionIndex(self,actionType):
		print(actionType)
		if actionType==Qt.CopyAction:
			return 0
		elif actionType == Qt.MoveAction:
			return 1
		elif actionType ==Qt.LinkAction:
			return 2
		elif actionType == Qt.IgnoreAction:
			return 3
		else:
			return 0

	def __getDropActionType(self,index):
		if index == 0:
			return Qt.CopyAction
		elif index == 1:
			return Qt.MoveAction
		elif index == 2:
			return Qt.LinkAction
		elif index == 3:
			return Qt.IgnoreAction
		else:
			return Qt.CopyAction


	##==========事件处理函数===========
	def eventFilter(self, watched, event):
		if event.type() == QEvent.KeyPress and event.key()==Qt.Key_Delete:
			if watched == self.ui.listSource:
				self.ui.listSource.takeItem(self.ui.listSource.currentRow())
			elif watched == self.ui.listWidget:
				self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
			elif watched == self.ui.treeWidget:
				curItem = self.ui.treeWidget.currentItem()
				if curItem.parent() != None:
					parItem = curItem.parent()
					parItem.removeChild(curItem)
				else:
					index = self.ui.treeWidget.indexOfTopLevelItem(curItem)
					self.ui.treeWidget.takeTopLevelItem(index)
			elif watched == self.ui.tableWidget:
				self.ui.tableWidget.takeItem(self.ui.tableWidget.currentRow(),
											 self.ui.tableWidget.currentColumn())
		return super().eventFilter(watched,event)

	##==========由connectSlotsByName()自动关联的槽函数====
	@pyqtSlot()
	def on_radio_Source_clicked(self):
		self.__itemView = self.ui.listSource
		self.__refreshToUI()

	@pyqtSlot()
	def on_radio_List_clicked(self):
		self.__itemView = self.ui.listWidget
		self.__refreshToUI()
	@pyqtSlot()
	def on_radio_Tree_clicked(self):
		self.__itemView = self.ui.treeWidget
		self.__refreshToUI()
	@pyqtSlot()
	def on_radio_Table_clicked(self):
		self.__itemView = self.ui.tableWidget
		self.__refreshToUI()

	@pyqtSlot(bool)
	def on_chkBox_AcceptDrops_clicked(self,checked):
		self.__itemView.setAcceptDrops(checked)
	@pyqtSlot(bool)
	def on_chkBox_DragEnabled_clicked(self,checked):
		self.__itemView.setDragEnabled(checked)
	@pyqtSlot(int)
	def on_combo_Mode_currentIndexChanged(self,index):
		mode = QAbstractItemView.DragDropMode(index)
		self.__itemView.setAcceptDrops(mode)
	@pyqtSlot(bool)
	def on_combo_DefaultAction_currentIndexChanged(self,index):
		actionType = self.__getDropActionType(index)
		self.__itemView.setDefaultDropAction(actionType)

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyWidget()
	form.show()

	sys.exit(app.exec_())