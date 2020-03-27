import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QActionGroup,QLabel,QProgressBar,QSpinBox,QFontComboBox
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtGui import QTextCharFormat,QFont
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

		self.__buildUI()
		self.__spinFontSize.valueChanged[int].connect(self.do_fontSize_Changed)
		self.__comboFontName.currentIndexChanged[str].connect(self.do_fontName_Changed)
		self.setCentralWidget(self.ui.textEdit)
	##==========自定义功能函数==========
	def __buildUI(self):
		self.__LabFile = QLabel(self)#QLabel组件显示信息
		self.__LabFile.setMinimumWidth(150)
		self.__LabFile.setText('文件名: ')
		self.ui.statusBar.addWidget(self.__LabFile)#添加到状态栏

		self.__progressBar1 = QProgressBar(self)#实例进度条
		self.__progressBar1.setMaximumWidth(200)#设定最大宽度
		self.__progressBar1.setMinimum(5)#设置最小值
		self.__progressBar1.setMaximum(50)#设置最大值
		sz = self.ui.textEdit.font().pointSize()
		print(sz)
		self.__progressBar1.setValue(sz)
		self.ui.statusBar.addWidget(self.__progressBar1)

		self.__LabInfo = QLabel(self)
		self.__LabInfo.setText('选择字体名称: ')
		self.ui.statusBar.addPermanentWidget(self.__LabInfo)

		actionGroup = QActionGroup(self)#定义一个组
		actionGroup.addAction(self.ui.actLang_CN)#添加两个组件到一个组内
		actionGroup.addAction(self.ui.actLang_EN)
		actionGroup.setExclusive(True)#令组内组件互斥
		self.ui.actLang_CN.setChecked(True)#设定中文按钮为默认

		self.__spinFontSize = QSpinBox(self)#设定QSpinBox组件控制字体大小
		self.__spinFontSize.setMaximum(50)#最大字体50
		self.__spinFontSize.setMinimum(5)#最小字体5
		sz = self.ui.textEdit.font().pointSize()
		self.__spinFontSize.setValue(sz)
		self.__spinFontSize.setMinimumWidth(50)
		self.ui.mainToolBar.addWidget(self.__spinFontSize)

		self.__comboFontName = QFontComboBox(self)
		self.__comboFontName.setMinimumWidth(100)
		self.ui.mainToolBar.addWidget(self.__comboFontName)

		self.ui.mainToolBar.addSeparator()
		self.ui.mainToolBar.addAction(self.ui.actClose)
	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====
	@pyqtSlot(bool)
	def on_actFont_Bold_triggered(self,checked):
		fmt = self.ui.textEdit.currentCharFormat()
		print(fmt.fontWeight())
		# print(fmt,dir(fmt))
		# print(checked)
		if (checked==True):
			# print(QFont.setItalic())
			fmt.setFontWeight(QFont.Bold)
			print(fmt.fontWeight())
		else:
			fmt.setFontWeight(QFont.Normal)
			print(fmt.fontWeight())
		self.ui.textEdit.mergeCurrentCharFormat(fmt)
		# fmt.setFontBold(checked)
		# self.ui.textEdit.currentCharFormat(fmt)

	@pyqtSlot(bool)
	def on_actFont_Italic_triggered(self,checked):
		fmt = self.ui.textEdit.currentCharFormat()
		fmt.setFontItalic(checked)
		self.ui.textEdit.mergeCurrentCharFormat(fmt)

	@pyqtSlot(bool)
	def on_actFont_UnderLine_triggered(self,checked):
		fmt = self.ui.textEdit.currentCharFormat()
		fmt.setFontUnderline(checked)
		self.ui.textEdit.mergeCurrentCharFormat(fmt)

	def on_textEdit_copyAvailable(self,avi):
		self.ui.actEdit_Cut.setEnabled(avi)
		self.ui.actEdit_Copy.setEnabled(avi)
		self.ui.actEdit_Paste.setEnabled(self.ui.textEdit.canPaste())

	def on_textEdit_selectionChanged(self):
		fmt = self.ui.textEdit.currentCharFormat()
		self.ui.actFont_Bold.setEnabled(fmt.font().bold())
		self.ui.actFont_Italic.setEnabled(fmt.fontItalic())
		self.ui.actFont_UnderLine.setEnabled(fmt.fontUnderline())

	def on_textEdit_custonContextMenuRequested(self,pos):
		popMenu = self.ui.textEdit.createStandardContextMenu()
		popMenu.exec(pos)
	##=========自定义槽函数============
	@pyqtSlot(int)
	def do_fontSize_Changed(self,fontSize):
		fmt = self.ui.textEdit.currentCharFormat()
		fmt.setFontPointSize(fontSize)
		self.ui.textEdit.mergeCurrentCharFormat(fmt)
		self.__progressBar1.setValue(fontSize)

	@pyqtSlot(str)
	def do_fontName_Changed(self,fontName):
		fmt = self.ui.textEdit.currentCharFormat()
		fmt.setFontFamily(fontName)
		self.ui.textEdit.mergeCurrentCharFormat(fmt)
		self.__LabInfo.setText("字体名称: {}".format(fontName))

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())