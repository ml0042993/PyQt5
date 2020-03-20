#单继承与界面独立封装方式

#单继承能够更好的进行界面与逻辑的分离

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from ui_FormHello import Ui_FormHello

class QmyWidget(QWidget):
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建QWidget窗体
		#selg.__ui包含了可视化设计UI窗口上的所有组件，只有通过其才能访问窗口上的组件
		self.__ui = Ui_FormHello()#创建UI对象
		#可以将ui定义为
		# self.ui = Ui_FormHello()#如果这样定义则ui为公共属性，则在外部也可调用
		self.__ui.setupUi(self)

		self.Lab = "单继承的QmyWidget"

		self.__ui.labelHello.setText(self.Lab)

	def setBtnText(self,aText):
		'''
		定义接口函数，可以使myWidget通过其访问窗口组件
		:param aText:
		:return:
		'''
		self.__ui.btnClose.setText(aText)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	#myWidget不能直接访问__ui,不能直接访问窗体组件
	myWidget = QmyWidget()
	myWidget.show()
	myWidget.setBtnText('间接设置')
	sys.exit(app.exec_())

'''
优点：
窗体对象被定义为QmyWidget类的私有属性self.ui，外部无法调用，只能通过内部接口函数实现调用（def setBtnText(self,aText):），然后在应用程序中修改（myWidget.setBtnText('间接设置')）
窗体组件不会与QmyWidget内定义的属性混淆

'''