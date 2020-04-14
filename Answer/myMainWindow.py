import sys,os,re,xlrd
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QAbstractItemView
from PyQt5.QtCore import pyqtSlot,Qt,QStringListModel
# from PyQt5.QtGui import
# from PyQt5.QtWidgets import
# from PyQt5.QtSql import
# from PyQt5.QtMultimedia import
# from PyQt5.QtMultimediaWidgets import
from enum import Enum
from ui_MainWindow import Ui_MainWindow
class Key_Word(Enum):
	TIT_WORD = re.compile(r'第\s*\d+\s*题')
	KEY_WORD = re.compile(r'.+(?=A\.)')  # 选取A.前面的内容
	INI_WORD = re.compile(r'A\.')
	REP_WORD = re.compile(r'A.\s+')  # A.后面若干空格
	FILE_PATH = os.getcwd() + "\File\exam_bat"  # 格式化后的文件路径
	TEMP_PATH = os.getcwd() + "\File\exam_tmp"  # 临时文件路径


class QmyMainWindow(QMainWindow):
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建窗体
		self.ui = Ui_MainWindow()#创建Ui对象
		self.ui.setupUi(self)#构造UI
		self.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

	##==========自定义功能函数==========
	def __ini_File(self):
		'''
		初始化文档,令A.选项进入下一行
		:return:
		'''
		with open(Key_Word.FILE_PATH.value, 'w', encoding='utf-8') as f:
			with open('./File/exam.txt', 'r', encoding='utf8') as ef:
				lines = ef.readlines()
				for line in lines:
					anchor = Key_Word.INI_WORD.value.search(line)
					if anchor:
						result = re.sub("A.", "\n       A.", line)  # 令A选项格式化到下一行,并和B选项对齐
						line = result
					f.write(line)
		with open(Key_Word.TEMP_PATH.value, 'w', encoding="utf-8") as nf:
			with open(Key_Word.FILE_PATH.value, 'r', encoding="utf-8") as f:
				lines = f.readlines()  # 按行读取文件,返回的是一个列表
				for i in range(len(lines)):
					if lines[i] == '\n':  # 列表元素为空则不进行判断,进入下一行遍历
						continue
					anchor = Key_Word.REP_WORD.search(lines[i])
					if anchor:
						result = re.sub('A.\s+', "A.  ", lines[i])  # 格式化A.选项,令其后只有两个空格
						lines[i] = result  # 替换当前元素
					nf.write(lines[i])
		os.remove(Key_Word.FILE_PATH.value)
		os.rename(Key_Word.TEMP_PATH.value, Key_Word.FILE_PATH.value)

	def __Ini_Model_Data(self):
		'''
		格式化文档，将题目和选项放入一个列表内，合并为一个二维列表
		:return:
		'''
		Model_Data = []
		with open(Key_Word.FILE_PATH.value, 'r', encoding="utf-8") as f:
			Start = 0
			End = 0
			lines = f.readlines()
			for i in range(len(lines)):
				title_Num = Key_Word.TIT_WORD.search(lines[i])
				lines[i] = lines[i].replace(" ", "")  # 去除空格
				lines[i] = lines[i].replace("\n", "")  # 去除换行符
				if title_Num:
					lines[i] = title_Num.group()  # 更换题号为第 XX 题
					Model_Data.append(lines[Start:i])  # 将lines切片添加到列表中，说明Start初始为0，当title_num匹配后i=2，之后再修改Start=i即为2
					Start = i  # 切片后再修改行号，否则切片使用的锚点会一样，切片为空列表
				End = i  # 拿到文档的最后一行行号
			# 遍历中切片的最后一个lines[Start:i]的锚点分别为第99题的行号Start和第100题的行号i，当Start=i以后title_Num条件无法达成，不会对100题内容进行切片
			Model_Data.append(lines[Start:End])
		return Model_Data

	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====
	@pyqtSlot()
	def on_actOpen_File_triggered(self):
		curPath=os.getcwd()

		self.FileName,self.flt = QFileDialog.getOpenFileName(self,"打开一个文件",curPath,"exam(*.txt);;excle(*.xls)")
		if self.FileName == "":
			return

		elif self.flt == "exam(*.txt)":
			# print(111)
			self.__question_txt = self.__question()
			# print(self.__question_txt)
			self.model = QStringListModel(self)
			self.model.setStringList(self.__question_txt)
			self.ui.listView.setModel(self.model)
		elif self.flt == "excle(*.xls)":
			print(12)
	def on_listView_clicked(self,index):
		print(index.row())

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())