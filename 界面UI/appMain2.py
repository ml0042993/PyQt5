#appMain1只适合于测试单个窗体的UI效果,由于是一个过程化程序,难以实现业务逻辑功能的封装

#多继承方法编写

import sys
from PyQt5.QtWidgets import QWidget,QApplication
from ui_FormHello import Ui_FormHello

#定义类,其为窗体的业务逻辑类
class QmyWidget(QWidget,Ui_FormHello):

	def __init__(self,parent=None):
		#创建QWidget窗体,相当于main1中的QtWidgets.QWidget(),这个指向的是__init__方法
		super().__init__(parent)#执行后self成为一个QWidget对象

		self.Lab = "多继承的QmyWidget"
		'''
		setupUi()是Ui_FormHello的函数
		由于setupUi需要一个容器窗体,而super().__init__(parent)执行后self成为一个QWidget对象,这时可将self传入作为组件的窗体容器
		将窗体QWidget(即self)作为参数传给setupUi()
		相当于ui.setupUi(QtWidgets.QWidget())
		'''
		self.setupUi(self)
		#elf.labelHello是窗体上的对象,而self.Lab是QmyWidget上的新属性
		#多继承方式容易出现混乱
		self.labelHello.setText(self.Lab)
		'''
		通过多继承Ui_FormHello类定义的窗体上的组件对象成为QmyWidget的公共属性,可直接访问界面组件
		但同时当组件过多时容易出现新旧无法区分的混乱
		'''
if __name__ == '__main__':
	app = QApplication(sys.argv)

	myWidget = QmyWidget()
	myWidget.show()
	myWidget.btnClose.setText('不关闭')
	sys.exit(app.exec_())
