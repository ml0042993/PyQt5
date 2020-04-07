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
		self.itemModel = QStandardItemModel(5,self.__ColCount,self)#创建QStandardItemModel类型的数据模型,指定行列值
		'''
		setSelectionBehavior()
		此属性保存视图使用的选择行为。
		此属性保存选择是根据单个项目，行还是列进行的

		#QItemSelectionModel()
		此属性保存视图在哪种选择模式下运行。
		#此属性控制用户是否可以选择一个或多个项目，并且在多个项目选择中控制选择是否必须是连续范围的项目
		'''
		self.selectionModel = QItemSelectionModel(self.itemModel)

		self.selectionModel.currentChanged.connect(self.do_curChanged)#单元格选择发生变化时会发射此信号
		self.__lastColumnTitle = "测井取样"
		self.__lastColumnFlags = (Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
	#设置tableView属性
		self.ui.tableView.setModel(self.itemModel)#数据模型
		self.ui.tableView.setSelectionModel(self.selectionModel)#选择模型
		oneOrMore = QAbstractItemView.ExtendedSelection#选择模式->多选模式
		self.ui.tableView.setSelectionMode(oneOrMore)#多选模式
		itemOrRow = QAbstractItemView.SelectItems#项选择模式->单元格选择
		self.ui.tableView.setSelectionBehavior(itemOrRow)#单元格选择
		self.ui.tableView.verticalHeader().setDefaultSectionSize(22)
		self.ui.tableView.setAlternatingRowColors(True)#交替行颜色
		self.ui.tableView.setEnabled(False)#设置默认禁用tabelView

		# self.setCentralWidget(self.ui.splitter)
		self.__buildStatusBar()

	##==========自定义功能函数==========
	def __buildStatusBar(self):
		'''
		设置状态栏ui组件
		:return:
		'''
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
		'''
		设置状态栏组件显示内容
		:param current:
		:param previous:
		:return:
		'''
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