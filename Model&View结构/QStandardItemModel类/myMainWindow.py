import sys,os
from PyQt5.QtWidgets import QApplication,QMainWindow,QAbstractItemView,QLabel,QFileDialog
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt,QItemSelectionModel
from PyQt5.QtGui import QStandardItemModel,QStandardItem
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
		self.__lastColumnTitle = ""#设置最后一列的标题，可以是空
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

		self.setCentralWidget(self.ui.splitter)#设置中心组件
		# self.setCentralWidget(self.ui.tableView)
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
	def __iniModelFromStringList(self,allLines):
		rowCnt = len(allLines)#获取总行数
		self.itemModel.setRowCount(rowCnt-1)#除去表头的数据行数
		headerText = allLines[0].strip()#表头去除换行符，文件呢的空格使用Tab代替
		headerList = headerText.split("\t")#按照制表符转化为列表
		self.itemModel.setHorizontalHeaderLabels(headerList)#设置表头标题
		# print(headerList)
		self.__lastColumnTitle = headerList[len(headerList)-1]#最后一列的标题
		lastColNo = self.__ColCount-1#最后一列的列号

		for i in range(rowCnt-1):#除去表头的数据行数
			lineText = allLines[i+1].strip()#去除换行符
			strList = lineText.split("\t")#按制表符生成列表
			for j in range(self.__ColCount-1):
				'''
				QStandardItem是一个数据结构，他可以存储一个cell的各种信息，比如文本、图标、是否可选、字体、别景色、前景色等等。
				并且QStandardItem可以有孩子和兄弟，他是为model提供数据存储的节点。
				QTableView：作为表格cell时，有一个作为根节点的QStandardItem，其他节点都是QStandardItem节点的孩子节点，并且都是兄弟节点(这里暂时不考虑多列的情况)。
				QTreeView：作为树节点cell时，有一个作为根节点的QStandardItem，其他节点都是他的孩子节点，但是其他节点也可以作为父节点存在(这里暂时不考虑多列的情况)。
				'''
				item = QStandardItem(strList[j])
				self.itemModel.setItem(i,j,item)
			item = QStandardItem(self.__lastColumnTitle)
			item.setFlags(self.__lastColumnFlags)
			item.setCheckable(True)
			if  strList[lastColNo] == 0:
				item.setCheckState(Qt.Unchecked)
			else:
				item.setCheckState(Qt.Checked)
			self.itemModel.setItem(i,lastColNo,item)
	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====
	@pyqtSlot()
	def on_actOpenFile_triggered(self):

		curPath = os.getcwd()#获取当前路径
		print(curPath)
		#flt是文件过滤器
		filename,flt = QFileDialog.getOpenFileName(self,"打开一个文件",curPath,"井斜数据文件(*.txt);;所有文件(*.*)")
		if filename =="":
			return
		self.LabCurFile.setText(("当前文件: " + filename))#设置状态栏文本
		self.ui.plainTextEdit.clear()
		aFile = open(filename,"r")
		allLines = aFile.readlines()
		aFile.close()
		for strLine in allLines:
			self.ui.plainTextEdit.appendPlainText(strLine.strip())#按照行添加到plainTextEdit中
		self.__iniModelFromStringList(allLines)
		#设置激活状态
		self.ui.tableView.setEnabled(True)
		self.ui.actAppend.setEnabled(True)
		self.ui.actInsert.setEnabled(True)
		self.ui.actDel.setEnabled(True)
		self.ui.actSaveFile.setEnabled(True)
		self.ui.actModelData.setEnabled(True)
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