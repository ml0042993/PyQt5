import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolButton,QMenu
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt
# from PyQt5.QtGui import
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

		self.__setActionsForButton()
		self.__createSelectionPopMenu()
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

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())