import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDockWidget
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt
from PyQt5.QtGui import QPixmap
from enum import Enum#枚举类型
# from PyQt5.QtWidgets import
# from PyQt5.QtSql import
# from PyQt5.QtMultimedia import
# from PyQt5.QtMultimediaWidgets import

from ui_MainWindow import Ui_MainWindow

class TreeItemType(Enum):#设定节点类型的枚举类型
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

	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())