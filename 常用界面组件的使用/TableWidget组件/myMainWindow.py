import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt
from enum import Enum
from PyQt5.QtGui import QBrush
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
	@pyqtSlot()
	def on_btnSetHeader_clicked(self):
		'''
		设置表头
		表内的每个单元格都是一个QTableWidgetItem对象
		:return:
		'''
		headerText = ['姓名','性别','出生日期','民族','分数','是否党员']
		self.ui.tableInfo.setColumnCount(len(headerText))#设置列数
		for i in range(len(headerText)):
			headerItem = QTableWidgetItem(headerText[i])#实例化一个单元格,参数为单元格名称
			font = headerItem.font()#获取该单元格字体状态
			font.setPointSize(11)#为字体设置字号
			headerItem.setFont(font)#将字号大小绑定给该单元格
			headerItem.setForeground(QBrush(Qt.red))#设置单元格前景色,文字颜色
			#将该单元格设置为第i列的表头
			self.ui.tableInfo.setHorizontalHeaderItem(i,headerItem)

	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())