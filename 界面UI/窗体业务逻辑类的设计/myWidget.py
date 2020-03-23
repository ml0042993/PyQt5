import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

from Widget import Ui_Widget
from human import Human
#窗体业务逻辑类设计
class QmyWidget(QWidget):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Widget()
		self.ui.setupUi(self)

		self.boy = Human("Boy",16)
		#创建三个连接,将实例中的三个信号与3个自定义槽函数关联
		self.boy.nameChanged.connect(self.do_nameChanged)
		self.boy.ageChanged.connect(self.do_ageChanged_int)
		self.boy.ageChanged[str].connect(self.do_ageChanged_str)

##===========由connectSoltByName()自动与组件的信号关联的槽函数=======
	def on_sliderSetAge_valueChanged(self,value):
		#注意自动关联的槽函数的书写格式,不能随意改变
		self.boy.setAge(value)

	def on_btnSetName_clicked(self):
		hisName = self.ui.editNameInput.text()
		self.boy.setName(hisName)

##=======自定义槽函数======

	def do_nameChanged(self,name):
		self.ui.editNameHello.setText("Hello," +name)

	@pyqtSlot(int)
	def do_ageChanged_int(self,age):
		self.ui.editAgeInt.setText(str(age))
	@pyqtSlot(str)
	def do_ageChanged_str(self,info):
		self.ui.editAgeStr.setText(info)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	#为应用程序设置图标
	icon = QIcon(":/icons/images/close")
	app.setWindowIcon(icon)
	form = QmyWidget()
	form.show()
	sys.exit(app.exec_())