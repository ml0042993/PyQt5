import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileSystemModel,QLabel
from PyQt5.QtCore import QDir
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
		self.LabPath = QLabel(self)
		self.ui.statusBar.addWidget(self.LabPath)
		self.__buildModelView()
	##==========自定义功能函数==========
	def __buildModelView(self):

		self.model = QFileSystemModel(self)#定义数据模型
		self.model.setRootPath(QDir.currentPath())#获取当前路径,并设置为model的根目录
		self.ui.treeView.setModel(self.model)#将self.model设置为自己的数据模型
		self.ui.listView.setModel(self.model)
		self.ui.tableView.setModel(self.model)
		#将treeView的cilcked信号与listView与tableView的槽函数setRootIndex相关联
		self.ui.treeView.clicked.connect(self.ui.listView.setRootIndex)
		self.ui.treeView.clicked.connect(self.ui.tableView.setRootIndex)
	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====
	def on_treeView_clicked(self,index):#index是模型索引
		print(index)
		self.ui.checkBox.setChecked(self.model.isDir(index))
		self.LabPath.setText(self.model.filePath(index))
		self.ui.LabType.setText(self.model.type(index))
		self.ui.LabFileName.setText(self.model.fileName(index))

		fileSize = self.model.size(index)/1024
		# print(fileSize)
		if fileSize<1024:
			self.ui.LabFileSize.setText("%d KB"%fileSize)
		else:
			self.ui.LabFileSize.setText(".2f MB"% (fileSize/1024.0))

	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())