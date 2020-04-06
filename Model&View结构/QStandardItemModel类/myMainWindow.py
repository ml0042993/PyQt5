import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAbstractItemView,QLabel
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt,QItemSelectionModel
from PyQt5.QtGui import QStandardItemModel
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

		self.__ColCount = 6
		self.itemModel = QStandardItemModel(5,self.__ColCount,self)
		self.selectionModel = QItemSelectionModel(self.itemModel)

		self.selectionModel.currentChanged.connect(self.do_curChanged)
		self.__lastColumnTitle = "测井取样"
		self.__lastColumnFlags = (Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)

		self.ui.tableView.setModel(self.itemModel)
		self.ui.tableView.setSelectionModel(self.selectionModel)
		oneOrMore = QAbstractItemView.ExtendedSelection
		self.ui.tableView.setSelectionMode(oneOrMore)
		itemOrRow = QAbstractItemView.SelectItems
		self.ui.tableView.setSelectionBehavior(itemOrRow)
		self.ui.tableView.verticalHeader().setDefaultSectionSize(22)
		self.ui.tableView.setAlternatingRowColors(True)
		self.ui.tableView.setEnabled(False)

		self.setCentralWidget(self.ui.splitter)
		self.__buildStatusBar()

	##==========自定义功能函数==========
	def __buildStatusBar(self):
		self.LabCellPos = QLabel("当前单元格：",self)
		self.LabCellPos.setMinimumWidth(180)
		self.ui.statusBar.addWidget(self.LabCellPos)

		self.LabCellText = QLabel("单元格内容：",self)
		self.LabCellText.setMinimumWidth(150)
		self.ui.statusBar.addWidget(self.LabCellText)

		self.LabCurFile = QLabel("当前文件：",self)
		self.ui.statusBar.addWidget(self.LabCurFile)

	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====

	##=========自定义槽函数============
	def do_curChanged(self,current,previous):
		if current != None:
			text = " 当前单元格： %d行，%d列"%(current.row(),current.column())
			self.LabCellPos.setText(text)
			item = self.itemModel.itemFromIndex(current)
			self.LabCellText.setText("单元格内容："+ item.text())

			font = item.font()
			self.ui.actFontBold.setChecked(font.bold())
	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())