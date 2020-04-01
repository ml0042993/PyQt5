import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDockWidget,QTreeWidgetItem,QFileDialog
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt,QDir
from PyQt5.QtGui import QPixmap,QIcon
from enum import Enum#枚举类型
# from PyQt5.QtWidgets import
# from PyQt5.QtSql import
# from PyQt5.QtMultimedia import
# from PyQt5.QtMultimediaWidgets import

from ui_MainWindow import Ui_MainWindow

class TreeItemType(Enum):#设定节点类型的枚举类型
	'''
	QTreeWidgetItem(type: int = QTreeWidgetItem.Type)
	其类型为枚举类型QTreeWidgetItem.ItemType，树型部件中的标准QTreeWidgetItem项对应的取值为QTreeWidgetItem.Type（对应整数0），
	如果开发者需要从QTreeWidgetItem派生自定义项，则需要使用项的Type值大于等于QTreeWidgetItem.UserType（对应整型1000）的值，
	使用不同的type值的目的是为了提供给开发者对自定义项进行诸如排序等特殊处理
	'''
	itTopItem = 1001    #顶层节点
	itGroupItem = 1002  #分组节点
	itImageItem =1003   #图片文件节点
class TreeColNum(Enum): #目录树的列号的枚举类型
	colItem = 0         #分组/文件名列
	colItemType = 1     #节点类型列

class QmyMainWindow(QMainWindow):
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建窗体
		self.ui = Ui_MainWindow()#创建Ui对象
		self.ui.setupUi(self)#构造UI

		self.curPixmap = QPixmap()#用于存储当前显示的原始图片,放大缩小是基于原始图片的
		self.pixRation = 1 #显示比例,1表示原始大小
		#设置节点的属性,可选/
		'''
		ItemIsUserCheckable 项目上是否有复选框
		ItemIsEnabled 项目上是否没有被禁用（Enabled可用/Disabled禁用）
		ItemIsSelectable 项目是否可以选中
		ItemIsAutoTristate 允许Check的第三种状态
		'''
		self.itemFlags = (Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled|Qt.ItemIsAutoTristate)

		self.setCentralWidget(self.ui.scrollArea)#设置scrollArea为中心窗口,设置后可随窗口大小进行缩放

		self.__iniTree()#初始化节点函数
		'''
		DockWidget的主要属性有两个:
		1.allowedAreas属性,设置允许停靠区域,可以设置在窗口的四个方向停靠/所有区域可靠或者不可停靠
		2.features属性,设置停靠区组件的特性;a.QDockWidget.DockWidgetClosable    停靠区可关闭
										b.QDockWidget.DockWidgetMovable     停靠区可移动
										c.QDockWidget.DockWidgetFloatable   停靠区可浮动
										d.QDockWidget.DockWidgetVerticalTitleBar   在停靠区左侧显示垂直标题栏
										e.QDockWidget.AllDockWidgetFeatures  上述所有特征
										f.QDockWidget.NoDockWidgetFeatures  不能停靠/移动/关闭
		'''
		self.ui.dockWidget.setFeatures(QDockWidget.AllDockWidgetFeatures)
		self.ui.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)#允许左右停靠
		self.ui.scrollArea.setWidgetResizable(True)#scrollArea,可自动调整内部组件大小
		self.ui.scrollArea.setAlignment(Qt.AlignCenter)
		self.ui.LabPicture.setAlignment(Qt.AlignCenter)

	##==========自定义功能函数==========

	def __iniTree(self):
		'''
		初始化目录树
		QTreeWidget的每个节点是一个QTreeWidgetItem类对象,添加一个节点需要先创建节点
		:return:
		'''
		self.ui.treeFiles.clear()
		icon = QIcon(':/icons/images/15.ico')

		item = QTreeWidgetItem(TreeItemType.itTopItem.value)#创建节点
		'''
		setIcon()/setText()为节点的某一列设置图标和文件,需要传递一个列号作为参数,
		TreeColNum.colItem.value的值为0,表示目录树的第一列
		'''
		item.setIcon(TreeColNum.colItem.value,icon)
		item.setText(TreeColNum.colItem.value,"图片文件")

		item.setFlags(self.itemFlags)#设置节点属性
		item.setCheckState(TreeColNum.colItem.value,Qt.Checked)#设置勾选状态,状态有三种,包括部分勾选
		'''
		setData():为节点的某一列设置一个角色数据,原型为setData(self,column,role,value)
		column:列号
		role:角色的值
		value:任意类型的数据
		'''
		item.setData(TreeColNum.colItem.value,Qt.UserRole,"")
		self.ui.treeFiles.addTopLevelItem(item)#将设置完成的节点作为顶层节点添加到目录树
	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====

	@pyqtSlot()
	def on_actTree_AddFolder_triggered(self):
		'''
		向顶层节点内添加分组节点,分组节点的具体方式是文件夹
		:return:
		'''
		dirStr = QFileDialog.getExistingDirectory()#选择需要添加的目录，值是选择的文件夹的路径

		# if dirStr == "":#是否选择路径,如果没有选中则系统默认选中程序所在的根目录
		# 	return#从程序运行结果来看,该语句多余
		parItem = self.ui.treeFiles.currentItem()#获得当前节点(选中的节点),选中则是PyQt5.QtWidgets.QTreeWidgetItem类型,未选中则为None

		if parItem == None:#如果没有选中节点,即鼠标未点击界面中的目录层级,则令程序选中最顶层节点
			parItem = self.ui.treeFiles.topLevelItem(0)#1001


		icon = QIcon(":/icons/images/open3.bmp")

		dirObj = QDir(dirStr)
		nodeText = dirObj.dirName()#最后一级目录的名称
		'''
		item = QTreeWidgetItem(TreeItemType.itGroupItem.value)
		参数值为1002,即添加的是一个分组节点,这样设置的结果会导致在顶层节点下添加节点时,
		无论选中哪一级的节点添加的都是1002参数的分组节点,即全部都是文件夹类型
		
		item = QTreeWidgetItem(parItem.type()+1)
		'''
		item = QTreeWidgetItem(TreeItemType.itGroupItem.value)

		item.setFlags(self.itemFlags)#设置状态
		item.setIcon(TreeColNum.colItem.value,icon)#给节点列(第一列)添加图标
		item.setIcon(TreeColNum.colItemType.value,icon)#给节点列(第一列)添加图标
		item.setText(TreeColNum.colItem.value,nodeText)#给节点列添加名称
		item.setText(TreeColNum.colItemType.value,"Group")#给节点类型列添加名称
		item.setCheckState(TreeColNum.colItem.value,Qt.Checked)#添加一个多选框
		item.setData(TreeColNum.colItem.value,Qt.UserRole,dirStr)

		parItem.addChild(item)#添加子节点
		parItem.setExpanded(True)#展开模式


	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())