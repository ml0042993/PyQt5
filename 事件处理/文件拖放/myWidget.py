import sys,os
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt,QSize
from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import
# from PyQt5.QtSql import
# from PyQt5.QtMultimedia import
# from PyQt5.QtMultimediaWidgets import

from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建窗体
		self.ui = Ui_Widget()#创建Ui对象
		self.ui.setupUi(self)#构造UI
		'''
		setAcceptDrops()是QWidget类定义的函数
		用于设置窗体组件是否可以接收放置操作
		可以重新定义dragEnterEvent（）和dropEvent（）等事件函数实现特定操作
		'''
		self.setAcceptDrops(True)#设置全局允许拖放
		self.ui.label.setAcceptDrops(False)#设置允许接收
		self.ui.plainTextEdit.setAcceptDrops(False)
		self.ui.label.setScaledContents(True)#适应label大小
		self.__SetSizeLabel()

	##==========自定义功能函数==========
	def __SetSizeLabel(self):
		'''
		设置label的大小
		:return:
		'''
		print(self.ui.label.size())
		QWidget_size_width = super().width()
		QWidget_size_height = super().height()
		plainTextEdit_width =self.ui.plainTextEdit.size().width()
		plainTextEdit_height = self.ui.plainTextEdit.size().height()

		width = QWidget_size_width-plainTextEdit_width
		height = QWidget_size_height-plainTextEdit_height

		rect = self.ui.label.geometry()
		self.ui.label.setGeometry(rect.left(),rect.top(),width,height)
		print(self.ui.label.size())
	##==========事件处理函数===========

	def dragEnterEvent(self,event):
		'''
		dragEnterEvent() 事件函数在拖动进入组件上方时触发
		主要功能一般是通过读取拖动文件的mimeData属性的内容，
			判断是否是所需要的拖动来源，以决定是否允许此拖动被放置
		:param event: QDragEnterEvent类型
		event.mimeData()函数返回一个QMimeData对象，此对象内封装了拖动操作数据源的关键信息
		QMimeData类对MIME数据的封装，拖放操作和剪切板操作中都用QMimeData类描述传输的数据
		QMimeData对象可能用多张格式存储同一数据
		:return:
		'''
		print(event)
		self.ui.plainTextEdit.clear()
		self.ui.plainTextEdit.appendPlainText('dragEnterEvent 事件 mimeData().formats()')

		for strLine in event.mimeData().formats():#mimeData().formats()返回对象支持的MIME格式的字符串列表
			'''
			此例子的MIME数据格式是text/uri-list，可以用QMimeData的urls()函数获取一个列表
			text/uri-list表示URL网址或者本机上的文件来源
			由于是接收的一个Window资源管理器拖动的Jpg文件，所以有text/uri-list
			'''

			self.ui.plainTextEdit.appendPlainText(strLine)
		self.ui.plainTextEdit.appendPlainText(
			"\ndragEnterEvent 事件 mimeData().urls()")
		for url in event.mimeData().urls():#用QMimeData的urls()函数获取一个列表
			#QUrl.path()返回URL路径，是带有文件路径的文件名，windows上会在开头多一个“/”
			self.ui.plainTextEdit.appendPlainText(url.path())

		if event.mimeData().hasUrls():
			'''
			hasUrls()函数判断QMimeData的MIME格式是否是text/uri-list
			urls（）获取函数，setUrls（）设置函数
			'''
			filename = event.mimeData().urls()[0].fileName()#带格式的文件名
			print(filename)
			basename,ext = os.path.splitext(filename)#将文件**.jpg分割为两个部分
			print(basename,ext)
			ext= ext.upper()#文件类型.jpg

			if ext == ".bmp":
				event.acceptProposedAction()#接受拖动操作，允许后续的放置操作
			else:
				event.ignore()

	def dropEvent(self, event):
		'''
		在dragEnterEvent()事件函数中被接受的拖动操作在放置时才会触发dropEvent()事件函数
		因此不需要再进行MIME格式判断
		关键是获取拖动操作的源文件的完整文件名
		:param event:
		:return:
		'''
		print(event)
		filename = event.mimeData().urls()[0].path()
		print(event.mimeData().urls()[0])
		cnt = len(filename)
		realname = filename[1:cnt]

		pixmap = QPixmap(realname)
		self.ui.label.setPixmap(pixmap)

		event.accept()


	##==========由connectSlotsByName()自动关联的槽函数====

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyWidget()
	form.show()

	sys.exit(app.exec_())