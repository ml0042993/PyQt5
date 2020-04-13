import sys,os,re,xlrd
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QAbstractItemView
from PyQt5.QtCore import pyqtSlot,Qt,QStringListModel
# from PyQt5.QtGui import
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
		self.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.__question_txt = []
		self.__question_excle = []
	##==========自定义功能函数==========
	def __question_num(self):
		question_num = []
		num_word = re.compile(r'第\s*\d+\s*题')
		with open(self.FileName, 'r', encoding='utf8') as ef:
			lines = ef.readlines()
			for line in lines:
				num_question = num_word.search(line)
				if num_question:
					num = num_question.group()
					question_number = re.sub('\s+', '', num)
					question_num.append(question_number)
		return question_num

	def __question_tit(self):
		question_tit = []
		key_word = re.compile(r'.+(?=A\.)')
		with open(self.FileName, 'r', encoding='utf8') as ef:
			lines = ef.readlines()
			for line in lines:
				anchor = key_word.search(line)
				if anchor:
					message = anchor.group()
					result = re.sub('\s+', '', message)
					question_title = re.sub('（）', '()', result)
					question_tit.append(question_title)
		return question_tit

	def __question(self):
		self.question = []
		for i in range(len(self.__question_num())):
			self.question.append(self.__question_num()[i]+','+self.__question_tit()[i])
		return self.question


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