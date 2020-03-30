import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolButton,QMenu,QListWidgetItem
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtGui import QIcon,QCursor
# from PyQt5.QtWidgets import
# from PyQt5.QtSql import
# from PyQt5.QtMultimedia import
# from PyQt5.QtMultimediaWidgets import

from ui_MainWindow import Ui_MainWindow

class QmyMainWindow(QMainWindow):
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建窗体
		self.ui = Ui_MainWindow()#创建Ui对象
		self.ui.setupUi(self)#构造UI

		self.setCentralWidget(self.ui.splitter)

		self.__setActionsForButton()
		self.__createSelectionPopMenu()
		'''
		Qt.ItemIsSelectable:项可被选择
		Qt.ItemIsUserCheckable:项可以被复选
		Qt.ItemIsEnabled:项可以被使用
		Qt.ItemIsEditable:项可以被编辑
		'''
		self.__FlagEditable = (Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsEditable)
		self.__FlagNotEditable = (Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
	##==========自定义功能函数==========
	def __setActionsForButton(self):
		'''
		QToolButton存在一个setDefaultAction（）函数，可以使其与一个Action相关联，按钮的文字、图标、tooltip都与关联的Action一致；
		单击QToolButton会执行action的槽函数；
		主工具栏上的按钮是根据Action自动创建的QToolButton
		:return:
		'''
		self.ui.btnList_Ini.setDefaultAction(self.ui.actList_Ini)
		self.ui.btnList_Clear.setDefaultAction(self.ui.actList_Clear)
		self.ui.btnList_Insert.setDefaultAction(self.ui.actList_Insert)
		self.ui.btnList_Append.setDefaultAction(self.ui.actList_Append)
		self.ui.btnList_Delete.setDefaultAction(self.ui.actList_Delete)

		self.ui.btnSel_ALL.setDefaultAction(self.ui.actSel_All)
		self.ui.btnSel_None.setDefaultAction(self.ui.actSel_None)
		self.ui.btnSel_Invs.setDefaultAction(self.ui.actSel_Invs)

	def __createSelectionPopMenu(self):
		'''
		setMenu()可以为其设置一个下拉菜单，配合QToolButton的一些属性，可以有不同的下拉菜单效果
		:return:
		'''
		menuSelection = QMenu(self)#初始化
		#加入三个功能
		menuSelection.addAction(self.ui.actSel_All)
		menuSelection.addAction(self.ui.actSel_None)
		menuSelection.addAction(self.ui.actSel_Invs)

		self.ui.mainToolBar.addSeparator()#分割线

		# 工具栏上的下拉菜单按钮
		self.__btnSelectItems_2 = QToolButton(self)#初始化一个QToolButton按钮
		self.__btnSelectItems_2.setPopupMode(QToolButton.InstantPopup)#设置下拉菜单的弹出模式
		# self.__btnSelectItems_2.setPopupMode(QToolButton.MenuButtonPopup)#设置下拉菜单的弹出模式
		self.__btnSelectItems_2.setDefaultAction(self.ui.actSelPopMenu)#利用setDefaultAction()函数关联Action
		self.__btnSelectItems_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)#设定图标显示格式
		self.__btnSelectItems_2.setMenu(menuSelection)#为按钮__btnSelectItems_2 设置下拉菜单
		self.ui.mainToolBar.addWidget(self.__btnSelectItems_2)#将其放入工具栏

		self.ui.mainToolBar.addAction(self.ui.actQuit)#设置工具栏中的退出按钮

		#设置listWidget上的 btnSelectItem按钮
		# self.ui.btnSelectItem.setPopupMode(QToolButton.MenuButtonPopup)#下拉菜单格式已在UI组件中设置
		self.ui.btnSelectItem.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
		self.ui.btnSelectItem.setDefaultAction(self.ui.actSelPopMenu)
		self.ui.btnSelectItem.setMenu(menuSelection)

	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====
	@pyqtSlot()
	def on_actList_Ini_triggered(self):
		'''
		初始化，为控件内添加若干QListWidgetItem类型的对象
		:return:
		'''
		icon = QIcon(":/icons/images/724.bmp")
		editable = self.ui.chkBoxList_Editable.isChecked()#拿到可编辑的复选框的状态，通过该状态初始化列表
		if editable == True:
			Flag = self.__FlagEditable#按照init内的设置可以修改名称
		else:
			Flag = self.__FlagNotEditable#不可以设置名称
		self.ui.listWidget.clear()#清除listWidget内的列表框
		for i in range(10):
			itemStr = 'Item %d'%i
			aItem = QListWidgetItem()#添加的项每一个都是QListWidgetItem类型的对象
			aItem.setText(itemStr)#设置名称
			aItem.setIcon(icon)#添加图标
			'''
			setCheckState:共三种状态
			1.Unchecked 			0 	未选中
			2.PartiallyChecked 		1	部分选中，当数据分层次是，下层数据有部分选中，部分未选中，则为该状态
			3.Checked				2	选中
			'''
			aItem.setCheckState(Qt.Checked)#设置为选中状态
			aItem.setFlags(Flag)#按照Flag状态设置项(aItem)
			self.ui.listWidget.addItem(aItem)#将项放入ListWidget中

	@pyqtSlot()
	def on_actList_Insert_triggered(self):
		'''
		插入项
		插入项使用insertItem()函数，有两种函数原型：
		1.insertItem(self,row,itemText),在第row行前插入项，项的标题有itemText决定，无法设置项的属性
		2.insertItem(self,row,item)，在第row行前插入项，项需要提前设定，可以设定项的属性
		如果需要在最后一行插入，可以直接使用addItem()函数
		:return:
		'''
		icon = QIcon(':/icons/images/724.bmp')
		editable = self.ui.chkBoxList_Editable.isChecked()
		if	editable == True:
			Flag = self.__FlagEditable
		else:
			Flag = self.__FlagNotEditable
		aItem = QListWidgetItem()#添加的项每一个都是QListWidgetItem类型的对象
		aItem.setText('Inserted Item')
		aItem.setIcon(icon)
		aItem.setCheckState(Qt.Checked)
		aItem.setFlags(Flag)
		curRow = self.ui.listWidget.currentRow()#当前行，值为-1，int类型

		self.ui.listWidget.insertItem(curRow,aItem)#在第一行插入
		# self.ui.listWidget.addItem(aItem)#在最后一行插入

	@pyqtSlot()
	def on_actList_Delete_triggered(self):
		'''
		删除项
		:return:
		'''
		row = self.ui.listWidget.currentRow()#当前行
		self.ui.listWidget.takeItem(row)#删除当前项
	@pyqtSlot()
	def on_actList_Clear_triggered(self):
		self.ui.listWidget.clear()#清空类别项
	'''
	为Action绑定逻辑
	'''
	@pyqtSlot()
	def on_actSel_All_triggered(self):#全选
		# print(self.ui.listWidget.count())
		for i in range(self.ui.listWidget.count()):
			aItem = self.ui.listWidget.item(i)
			aItem.setCheckState(Qt.Checked)
		# self.ui.listWidget.selectAll()
	@pyqtSlot()
	def on_actSel_None_triggered(self):#全不选
		for i in range(self.ui.listWidget.count()):
			aItem = self.ui.listWidget.item(i)
			aItem.setCheckState(Qt.Unchecked)

	@pyqtSlot()
	def on_actSel_Invs_triggered(self):#反选
		for i in range(self.ui.listWidget.count()):
			aItem = self.ui.listWidget.item(i)
			if aItem.checkState() != Qt.Checked:
				aItem.setCheckState(Qt.Checked)
			else:
				aItem.setCheckState(Qt.Unchecked)

	def on_listWidget_currentItemChanged(self,current,previous):
		'''
		QListWidget在当前项切换时发射两个信号:
		1.currentRowChanged(int):传递当前项的行号作为参数
		2.currentRowChanged(current,previous):两个参数都是QListWidgetItem对象
		当内容发生变化时发射信号currentTextChanged(str)
		:param current: 当前项
		:param previous: 前一项
		:return:
		'''
		strInfo=""
		if current != None:
			if previous ==None:
				strInfo = "当前:" + current.text()
			else:
				strInfo = "前一项: " + previous.text() + "; 当前项" + current.text()
		self.ui.editCurItemText.setText(strInfo)

	def on_listWidget_customContextMenuRequested(self,pos):
		'''
		设置右键菜单
		:param pos:
		:return:
		'''
		menuList = QMenu(self)#创建菜单
		menuList.addAction(self.ui.actList_Ini)
		menuList.addAction(self.ui.actList_Clear)
		menuList.addAction(self.ui.actList_Insert)
		menuList.addAction(self.ui.actList_Append)
		menuList.addAction(self.ui.actList_Delete)
		menuList.addSeparator()
		menuList.addAction(self.ui.actSel_All)
		menuList.addAction(self.ui.actSel_None)
		menuList.addAction(self.ui.actSel_Invs)
		menuList.exec_(QCursor.pos())

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())