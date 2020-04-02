import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt
from enum import Enum
# from PyQt5.QtGui import
# from PyQt5.QtWidgets import
# from PyQt5.QtSql import
# from PyQt5.QtMultimedia import
# from PyQt5.QtMultimediaWidgets import

from ui_MainWindow import Ui_MainWindow

class CellType(Enum):
	ctName = 1000
	ctSex = 1001
	ctBirth = 1002
	cnNation = 1003
	cnScore = 1004
	ctPartyM = 1005

class FieldColNum(Enum):
	colName = 0
	colSex = 1
	colBirth = 2
	colNation = 3
	colScore = 4
	colParthM = 5

class QmyMainWindow(QMainWindow):
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建窗体
		self.ui = Ui_MainWindow()#创建Ui对象
		self.ui.setupUi(self)#构造UI

		self.LabCellIndex = QLabel('当前单元格坐标: ',self)
		self.LabCellIndex.setMinimumWidth(250)
		self.LabCellType = QLabel('当前单元格类型: ',self)
		self.LabCellType.setMinimumWidth(200)
		self.LabStudID = QLabel('学生ID: ',self)
		self.LabStudID.setMinimumWidth(200)

		self.ui.statusBar.addWidget(self.LabCellIndex)
		self.ui.statusBar.addWidget(self.LabCellType)
		self.ui.statusBar.addWidget(self.LabStudID)

		self.ui.tableInfo.setAlternatingRowColors(True)#交替行颜色

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