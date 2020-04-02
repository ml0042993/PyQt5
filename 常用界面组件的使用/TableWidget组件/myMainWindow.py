import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QTableWidgetItem
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt,QDate
from enum import Enum
from PyQt5.QtGui import QBrush,QIcon
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
	colParthM = 4
	colScore = 5

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
		self.ui.chkBoxRowColor.setChecked(True)#设置chkBoxRowColor默认状态为选中
	##==========自定义功能函数==========
	##==========事件处理函数===========
	def __createItemARow(self,rowNo,name,sex,birth,nation,isParty,score):
		StudID = 201805000+rowNo
		#姓名
		item = QTableWidgetItem(name,CellType.ctName.value)#实例一个有姓名的单元格,
		item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)#水平+垂直居中
		font = item.font()
		font.setBold(True)
		item.setFont(font)
		item.setData(Qt.UserRole,StudID)#设置自定义数据,将学生ID存入,该数据不会显示在界面
		self.ui.tableInfo.setItem(rowNo,FieldColNum.colName.value,item)#第1(0)行1(0)列,设置item单元格
		#性别
		if sex == '男':
			icon = QIcon(":/icons/images/boy.ico")
		else:
			icon = QIcon(":/icons/images/girl.ico")

		item = QTableWidgetItem(sex,CellType.ctSex.value)
		item.setIcon(icon)#设置图标
		item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
		self.ui.tableInfo.setItem(rowNo,FieldColNum.colSex.value,item)
		#出生日期
		strBirth = birth.toString('yyyy-MM-dd')
		item = QTableWidgetItem(strBirth,CellType.ctBirth.value)
		item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
		self.ui.tableInfo.setItem(rowNo,FieldColNum.colBirth.value,item)
		#民族
		item = QTableWidgetItem(nation,CellType.cnNation.value)
		item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		if nation != '汉族':
			item.setForeground(QBrush(Qt.blue))#设置文字颜色为蓝色
		self.ui.tableInfo.setItem(rowNo,FieldColNum.colNation.value,item)
		#党员
		item = QTableWidgetItem("党员",CellType.ctPartyM.value)
		item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		if  isParty == True:
			item.setCheckState(Qt.Checked)#选中
		else:
			item.setCheckState(Qt.Unchecked)#不选择
		item.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsUserCheckable)#可选,能被选(锁定),可被复选(为True带有复选框)
		item.setBackground(QBrush(Qt.yellow))
		self.ui.tableInfo.setItem(rowNo,FieldColNum.colParthM.value,item)
		#分数
		strScore = str(score)
		item = QTableWidgetItem(strScore,CellType.cnScore.value)
		item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
		self.ui.tableInfo.setItem(rowNo,FieldColNum.colScore.value,item)


	##==========由connectSlotsByName()自动关联的槽函数====
	@pyqtSlot()
	def on_btnSetHeader_clicked(self):
		'''
		设置表头
		表内的每个单元格都是一个QTableWidgetItem对象
		QTableWidgetItem对象实例化一共有4种方式
		    QTableWidgetItem(type: int = QTableWidgetItem.ItemType.Type):构建一个空项
		        type:默认是0
            QTableWidgetItem(str, type: int = QTableWidgetItem.ItemType.Type):构建一个带文本的项
                str:字符串
                type:是一个int,系统(Qt)保留0~1000,用户自定义需要从1001开始
            QTableWidgetItem(QIcon, str, type: int = QTableWidgetItem.ItemType.Type):构建一个带图标和文本的项
                QIcon:图标,str:字符串,
            QTableWidgetItem(QTableWidgetItem):从other复制项的内容构建一个新项

		type 参数主要为为了派生类使用，其类型为枚举类型QTableWidgetItem.ItemType，QTableWidgetItem创建的项使用缺省值QTreeWidgetItem.Type（值为0）。
		如果要从QTableWidgetItem派生子类以为应用提供自定义项时，可以为子类定义新类型，以便可以将它们与QTableWidgetItem项区分开来。
		需要此功能的子类的构造函数需要使用等于或大于QTableWidgetItem.UserType（对应整型1000）的新类型值。



		:return:
		'''
		headerText = ['姓名','性别','出生日期','民族','是否党员','分数']
		self.ui.tableInfo.setColumnCount(len(headerText))#设置列数
		for i in range(len(headerText)):
			headerItem = QTableWidgetItem(headerText[i])#实例化一个单元格,参数为单元格名称
			# print(headerItem.type())
			font = headerItem.font()#获取该单元格字体状态
			font.setPointSize(11)#为字体设置字号
			headerItem.setFont(font)#将字号大小绑定给该单元格
			headerItem.setForeground(QBrush(Qt.red))#设置单元格前景色,文字颜色
			#将该单元格设置为第i列的表头
			self.ui.tableInfo.setHorizontalHeaderItem(i,headerItem)
	@pyqtSlot()
	def on_btnSetRows_clicked(self):
		'''
		按照spinRowCount的数字设置行数
		:return:
		'''

		row = self.ui.spinRowCount.value()#获取行数

		self.ui.tableInfo.setRowCount(row)#设置tableInfo组件的行数
		self.ui.tableInfo.setAlternatingRowColors(self.ui.chkBoxRowColor.isChecked())#设置交替行背景颜色,参数为bool型,当前为True
	@pyqtSlot()
	def on_btnIniData_clicked(self):
		'''
		初始化表格,根据表格行数,生成数据填充表格,为每个单元格对象设置属性
		:return:
		'''

		self.ui.tableInfo.clearContents()#清除表格内容,不包括表头
		# self.ui.tableInfo.clear()#清除包括表头

		birth = QDate(1998,6,23)
		isParth = True
		nation = '汉族'
		score= 70

		rowCount = self.ui.tableInfo.rowCount()#获取表格行数
		for i in range(rowCount):
			strName = '学生%d'%i
			if (i%2)==0:
				strSex = '男'
			else:
				strSex = '女'
			self.__createItemARow(i,strName,strSex,birth,nation,isParth,score)
			birth = birth.addDays(20)
			isParth = not isParth
		self.__tableInitialized = True


	@pyqtSlot(int,int,int,int)
	def on_tableInfo_currentCellChangded(self,currentRow,currentColumn,previousRow,previousColumn):
		if self.__tableInitialized == False:
			return
		item = self.ui.tableInfo.item(currentRow,currentColumn)
		if item==None:
			return

		self.LabCellIndex.setText("当前单元格: %d行, %d 列" %(currentRow,currentColumn))
		itemCellType = item.type()
		self.LabCellType.setText("当前单元格类型: %d"%itemCellType)

		item2 = self.ui.tableInfo.item(currentRow,FieldColNum.colName.value)
		studID = item2.data(Qt.UserRole)
		self.LabStudID.setText("学生ID: %d"%studID)

	@pyqtSlot()
	def on_btnInsertRow_clicked(self):
		curRow = self.ui.tableInfo.currentRow()
		self.ui.tableInfo.insertRow(curRow)
		birth = QDate.fromString("1998-4-5","yyyy-M-d")
		self.__createItemARow(curRow,"新学生","男",birth,"苗族",True,65)

	@pyqtSlot()
	def on_btnAppendRow_clicked(self):
		curRow = self.ui.tableInfo.rowCount()
		self.ui.tableInfo.insertRow(curRow)
		birth = QDate.fromString("1999-1-10","yyyy-M-d")
		self.__createItemARow(curRow,"新生","女",birth,"土家族",False,85)
	@pyqtSlot()
	def on_btnDelCurRow_clicked(self):
		curRow = self.ui.tableInfo.currentRow()
		self.ui.tableInfo.removeRow(curRow)
	@pyqtSlot()
	def on_btnClearContents_clicked(self):
		self.ui.tableInfo.clearContents()
	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())