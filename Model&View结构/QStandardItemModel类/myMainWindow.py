import sys,os
from PyQt5.QtWidgets import QApplication,QMainWindow,QAbstractItemView,QLabel,QFileDialog
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt,QItemSelectionModel
from PyQt5.QtGui import QStandardItemModel,QStandardItem,QFont
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

		self.__ColCount = 6#列数
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
		self.ui.actFontBold.setCheckable(False)
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
			# print(i)
			lineText = allLines[i+1].strip()#去除换行符,不包括表头
			strList = lineText.split("\t")#按制表符生成列表
			for j in range(self.__ColCount-1):#不包括最后一列
				'''
				QStandardItem是一个数据结构，他可以存储一个cell的各种信息，比如文本、图标、是否可选、字体、别景色、前景色等等。
				并且QStandardItem可以有孩子和兄弟，他是为model提供数据存储的节点。
				QTableView：作为表格cell时，有一个作为根节点的QStandardItem，其他节点都是QStandardItem节点的孩子节点，并且都是兄弟节点(这里暂时不考虑多列的情况)。
				QTreeView：作为树节点cell时，有一个作为根节点的QStandardItem，其他节点都是他的孩子节点，但是其他节点也可以作为父节点存在(这里暂时不考虑多列的情况)。
				'''
				item = QStandardItem(strList[j])
				self.itemModel.setItem(i,j,item)
			#设置最后一行
			# print(self.__lastColumnTitle)
			item = QStandardItem(self.__lastColumnTitle)#将最后一行的表头
			item.setFlags(self.__lastColumnFlags)
			item.setCheckable(True)
			# print(strList[lastColNo])
			if strList[lastColNo] == '0':#对比文本内的数值进行设定,类型是字符串
				item.setCheckState(Qt.Unchecked)
			else:
				item.setCheckState(Qt.Checked)
			self.itemModel.setItem(i,lastColNo,item)
	def __setCellAlignment(self,align=Qt.AlignHCenter):
		if not self.selectionModel.hasSelection():
			return
		'''
		selectedIndexes()返回一个元素为QModelIndex类型的列表,包括所有被选中的单元格的模型索引
		'''
		selectdIndex = self.selectionModel.selectedIndexes()
		# print(selectdIndex)
		count = len(selectdIndex)
		for i in range(count):
			index = selectdIndex[i]
			'''
			itemFromIndex(index)返回的是模型索引为index的QStandardItem对象
			'''
			item = self.itemModel.itemFromIndex(index)
			item.setTextAlignment(align)
	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====
	@pyqtSlot()
	def on_actOpenFile_triggered(self):

		curPath = os.getcwd()#获取当前路径
		# print(curPath)?
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
		self.ui.actFontBold.setCheckable(True)#设置加粗可用

	@pyqtSlot()
	def on_actAppend_triggered(self):
		itemlist = []
		for i in range(self.__ColCount-1):#循环一行中的各个列,不包括最后一列
			item = QStandardItem("0")#添加0到数据结构中
			itemlist.append(item)

		item = QStandardItem(self.__lastColumnTitle)#将最后一行的表头添加入数据结构
		item.setCheckable(True)#可选
		item.setFlags(self.__lastColumnFlags)
		itemlist.append(item)#添加到itemlist内(添加到最后一个)

		self.itemModel.appendRow(itemlist)

		curIndex = self.itemModel.index(self.itemModel.rowCount()-1,0)#获取最后一行第一个单元格的模型索引
		self.selectionModel.clearSelection()#清除选择
		self.selectionModel.setCurrentIndex(curIndex,QItemSelectionModel.Select)#设置在添加后自动选择添加行的第一个单元格(可从状态栏确认)
	@pyqtSlot()
	def on_actInsert_triggered(self):
		'''
		插入行
		:return:
		'''
		itemlist = []
		for i in range(self.__ColCount-1):
			item = QStandardItem("0")
			itemlist.append(item)

		item = QStandardItem(self.__lastColumnTitle)
		item.setFlags(self.__lastColumnFlags)
		item.setCheckable(False)#是否可以修改选择
		item.setCheckState(Qt.Checked)#是否选中
		itemlist.append(item)

		curIndex = self.selectionModel.currentIndex()#选中项的模型索引,包括行列等其他信息
		self.itemModel.insertRow(curIndex.row(),itemlist)

		self.selectionModel.clearSelection()
		self.selectionModel.setCurrentIndex(curIndex,QItemSelectionModel.Select)
	@pyqtSlot()
	def on_actDel_triggered(self):
		'''
		删除行
		:return:
		'''
		curIndex = self.selectionModel.currentIndex()
		self.itemModel.removeRow(curIndex.row())


	@pyqtSlot()
	def on_actAlignLeft_triggered(self):
		self.__setCellAlignment(Qt.AlignLeft|Qt.AlignVCenter)
	@pyqtSlot()
	def on_actAlignCenter_triggered(self):
		self.__setCellAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
	@pyqtSlot()
	def on_actAlignRight_triggered(self):
		self.__setCellAlignment(Qt.AlignRight|Qt.AlignVCenter)

	@pyqtSlot(bool)
	def on_actFontBold_triggered(self,checked):
		print("1,checked",checked)
		if not self.selectionModel.hasSelection():
			return
		selectIndex = self.selectionModel.selectedIndexes()
		for i in range(len(selectIndex)):
			index = selectIndex[i]
			item = self.itemModel.itemFromIndex(index)
			font = item.font()
			font.setBold(checked)
			item.setFont(font)
	##=========自定义槽函数============
	def do_curChanged(self,current,previous):
		'''
		设置状态栏组件显示内容
		:param current:
		:param previous:
		:return:
		'''
		if current != None:
			text = " 当前单元格： %d行，%d列"%(current.row()+1,current.column()+1)
			self.LabCellPos.setText(text)
			item = self.itemModel.itemFromIndex(current)
			self.LabCellText.setText("单元格内容："+ item.text())

			font = item.font()
			self.ui.actFontBold.setChecked(font.bold())#设置按钮按下,当font.Bold的值大于50式font.blod()会为True
			print(font.bold())


	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())