import sys,os,re,xlrd
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QAbstractItemView,QDialog
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtGui import QStandardItemModel,QStandardItem,QFont
from PyQt5.QtWidgets import QCheckBox
# from PyQt5.QtSql import
# from PyQt5.QtMultimedia import
# from PyQt5.QtMultimediaWidgets import
from enum import Enum
from ui_MainWindow import Ui_MainWindow

class Key_Word(Enum):
	TIT_WORD = re.compile(r'第\s*\d+\s*题')
	KEY_WORD = re.compile(r'\s+')
	INI_WORD = re.compile(r'A\.')
	REP_WORD = re.compile(r'A.\s+')  # A.后面若干空格

	TYPE = ['单选题', '多选题', '判断题']

	FILE_PATH = os.getcwd() + "\File\exam_bat"  # 格式化后的文件路径
	TEMP_PATH = os.getcwd() + "\File\exam_tmp"  # 临时文件路径


class QmyMainWindow(QMainWindow):
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建窗体
		self.ui = Ui_MainWindow()#创建Ui对象
		self.ui.setupUi(self)#构造UI
		self.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.itemModel = QStandardItemModel(self)
		self.ui.listView.setModel(self.itemModel)
		self.__CheckedFlags = Qt.Checked
		self.ui.btnInit.setEnabled(False)
		self.ui.btnNext.setEnabled(False)
		self.ui.btnPrevious.setEnabled(False)
		self.ui.spinBox.setEnabled(False)
	##==========自定义功能函数==========
	def __ini_File(self,FileName):
		'''
		初始化文档,令A.选项进入下一行
		:return:
		'''
		with open(Key_Word.FILE_PATH.value, 'w', encoding='utf-8') as f:
			with open(FileName, 'r', encoding='utf8') as ef:
				lines = ef.readlines()
				for line in lines:
					line = line.strip(" ")
					line = line.replace(' ', '')
					line = line.replace('\u3000', "")
					line = line.replace('（', "(")
					line = line.replace('）', ")")
					line = line.replace('《', "<")
					line = line.replace('》', ">")

					anchor = Key_Word.INI_WORD.value.search(line)
					if anchor:
						result = re.sub("A.", "\nA.", line)  # 令A选项格式化到下一行,并和B选项对齐
						line = result
					elif line =='一、单选题\n' or line =='二、多选题\n' or line =='三、判断题\n':
						continue
					f.write(line)
		with open(Key_Word.TEMP_PATH.value, 'w', encoding="utf-8") as nf:
			with open(Key_Word.FILE_PATH.value, 'r', encoding="utf-8") as f:
				lines = f.readlines()  # 按行读取文件,返回的是一个列表
				for i in range(len(lines)):
					if lines[i] =='\n':  # 列表元素为空则不进行判断,进入下一行遍历
						continue
					anchor = Key_Word.REP_WORD.value.search(lines[i])
					if anchor:
						result = re.sub('A.\s+', "A.", lines[i])  # 格式化A.选项,令其后只有两个空格
						lines[i] = result  # 替换当前元素
					nf.write(lines[i])
		os.remove(Key_Word.FILE_PATH.value)
		os.rename(Key_Word.TEMP_PATH.value, Key_Word.FILE_PATH.value)

	def __Ini_Model_Data(self):
		'''
		格式化文档，将题目和选项放入一个列表内，合并为一个二维列表
		:return:
		'''
		self.Model_Data = []
		with open(Key_Word.FILE_PATH.value, 'r', encoding="utf-8") as f:
			Start = 0
			End = 0
			lines = f.readlines()
			num = len(lines)
			for i in range(num):
				title_Num = Key_Word.TIT_WORD.value.search(lines[i])
				lines[i] = lines[i].replace(" ", "")  # 去除空格
				lines[i] = lines[i].replace("\n", "")  # 去除换行符
				if title_Num and lines[i]!="\n":
					lines[i] = title_Num.group()  # 更换题号为第 XX 题
					self.Model_Data.append(lines[Start:i])  # 将lines切片添加到列表中，说明Start初始为0，当title_num匹配后i=2，之后再修改Start=i即为2
					Start = i  # 切片后再修改行号，否则切片使用的锚点会一样，切片为空列表
				End = i  # 拿到文档的最后一行行号
			# 遍历中切片的最后一个lines[Start:i]的锚点分别为第99题的行号Start和第100题的行号i，当Start=i以后title_Num条件无法达成，不会对100题内容进行切片
			# self.Model_Data.append(lines[Start:End])
			self.Model_Data.append(lines[Start:Start+4])
	def __InitModelFormList(self,Model_Data):
		Count_Row = len(Model_Data)
		for i in range(Count_Row):
			if len(Model_Data[i]) > 3:
				Count_Col = len(Model_Data[i])#Count_Col是二维列表内的列表的长度
				for j in range(Count_Col):
					item = QStandardItem(Model_Data[i][j])
					self.itemModel.setItem(i,j,item)
			# print(Model_Data[i])
	def __CreateChecked(self,checkName,checkText):
		'''
		创建复选框
		:param checkName: 复选框的objectName
		:param checkText: 复选框的文本内容
		:return:
		'''
		self.chk = QCheckBox(self.ui.groupBox_2)#在groupBox_2内实例化复选框
		self.chk.setObjectName(checkName)#设置名称
		self.ui.verticalLayout_3.addWidget(self.chk)#添加复选框到布局管理器内，必要的，否则无法正常显示
		self.chk.setText(checkText)#设置文本内容

	def __IntiExcleFile(self,FileName):
		'''
		初始化Excle文档,生成匹配列表
		:param FileName: Excle文档的位置
		:return:
		'''
		self.Excle_List = []#二维列表,选取excle中的特定列作为别匹配对象,包括题型/题目/选项/答案四个元素,其中选项是二级列表
		read_answer = xlrd.open_workbook(FileName)
		sheet = read_answer.sheet_by_index(0)#第一个sheet页
		for i in range(sheet.nrows):#按行读取
			rows = sheet.row_values(i)#按照每个列为一个元素组成一个列表
			if Key_Word.TYPE.value.__contains__(rows[5]):#按照题目类型进行匹配
				rows = rows[5:9]
				try:#格式化列表内的元素
					print(rows)
					rows[1] = rows[1].replace(' ', '')
					rows[1] = rows[1].replace('（', "(")
					rows[1] = rows[1].replace('）', ")")
					rows[1] = rows[1].replace('《', "<")
					rows[1] = rows[1].replace('》', ">")
					rows[2] = rows[2].replace(' ', '')
					rows[2] = rows[2].replace('（', "(")
					rows[2] = rows[2].replace('）', ")")
					rows[2] = rows[2].replace('《', "<")
					rows[2] = rows[2].replace('》', ">")

					rows[2] = rows[2].split('$;$')
					rows[-1] = rows[-1].replace('A', '0')
					rows[-1] = rows[-1].replace('B', '1')
					rows[-1] = rows[-1].replace('C', '2')
					rows[-1] = rows[-1].replace('D', '3')
					rows[-1] = rows[-1].replace('E', '4')
					rows[-1] = rows[-1].replace('F', '5')
					rows[-1] = rows[-1].replace('G', '6')
					rows[-1] = rows[-1].replace('H', '7')
					rows[-1] = rows[-1].replace('I', '8')

					self.Excle_List.append(rows)
				except Exception as e:
					print(e)

	def __SelectAnswer(self):
		self.__Result=[]
		for rows_Content in self.Excle_List:
			# print(rows_Content)
			if rows_Content[1].__contains__(self.__Title):#rows_Content[1]题目存储的元素位置
				# print(rows_Content[2],rows_Content[3])
				if rows_Content[0] == '判断题':
					if rows_Content[3] == "0":
						self.__Result.append('A.对')
					else:
						self.__Result.append('B.错')
				else:
					for i in rows_Content[3]:#遍历答案,i是按照ABCD转换的int型数字01234,数字作为选项列表的索引号使用
						i=int(i)
						self.__Result.append(rows_Content[2][i])

	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====
	@pyqtSlot()
	def on_actOpen_File_triggered(self):
		'''
		打开文件按钮
		:return:
		'''
		self.__FileName,self.flt = QFileDialog.getOpenFileName(self,"打开一个文件",Key_Word.FILE_PATH.value,"exam(*.txt);;excle(*.xls)")
		if self.__FileName == "":
			return

		elif self.flt == "exam(*.txt)":#如果打开的是txt文档
			self.ui.btnInit.setEnabled(True)#打开初始化按钮
			self.File_path=self.__FileName#获取文件路径
		elif self.flt == "excle(*.xls)":
			self.File_Exc_path = self.__FileName  # 获取文件路径
			self.__IntiExcleFile(self.File_Exc_path)#获得self.Excle_List列表
			# print(self.Excle_List)
	def on_listView_clicked(self,index):
		'''
		index.row()是行号
		:param index:
		:return:
		'''
		self.ui.lineEdit.clear()
		self.__Signal = index.row()
		for i in self.ui.groupBox_2.children():
			if type(i) == QCheckBox:
				i.deleteLater()#删除checkBox组件
		item = self.itemModel.item(self.__Signal,1)#获取题目的单元格的QStandardItem对象
		self.__Title = item.text()#
		self.ui.lineEdit.setText(self.__Title)#给文本框设置文字

		Column = self.itemModel.columnCount()#获取二维列表的长度
		for i in range(2,Column):
			item = self.itemModel.item(self.__Signal,i)#遍历二级列表内的元素
			try:
				anchor = item.text()
				checkName = "chk_{}_{}".format(self.__Signal,i)
				self.__CreateChecked(checkName,anchor)#按照选项个数动态生成生成复选框
			except AttributeError:
				break
		self.__SelectAnswer()
		for text in self.__Result:#正确答案的列表
			for chkBox in self.ui.groupBox_2.children():#遍历groupBox_2组件下的子组件
				if type(chkBox) == QCheckBox and text in chkBox.text():#条件组件事checkBox并且正确答案的文本在组件文本内能找到
					if isinstance(chkBox,QCheckBox):
						chkBox.setChecked(self.__CheckedFlags)#设置选中状态
						# background-color:rgb(255, 132, 139)	控件颜色
						# border-radius: 3px					圆角效果
						# color: rgb(255, 255, 255)				字体颜色
						chkBox.setStyleSheet("background-color:rgb(255, 132, 139);border-radius: 3px;color: rgb(255, 255, 255);")
						break


		# print(self.__Result)
	@pyqtSlot()
	def on_btnInit_clicked(self):
		'''
		初始化按钮
		:return:
		'''
		self.__ini_File(self.File_path)
		self.__Ini_Model_Data()
		self.__InitModelFormList(self.Model_Data)

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())