import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import QDateTime,QDate,QTime
# from PyQt5.QtGui import
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
	##==========自定义功能函数==========

	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====
	def on_btnGetTime_clicked(self):
		'''
		curDateTime获取系统时间,值为PyQt5.QtCore.QDateTime(2020, 3, 25, 15, 48, 17, 173)
		curDateTime.time()/curDateTime.date()是QDateTime中的时间部分和日期部分
		curDateTime.toString()是将QDateTime时间格式

		:return:
		'''
		curDateTime = QDateTime.currentDateTime()
		print(curDateTime)
		self.ui.timeEdit.setTime(curDateTime.time())
		self.ui.editTime.setText(curDateTime.toString("hh:mm:ss"))#设置字符串显示格式

		self.ui.dateEdit.setDate(curDateTime.date())
		self.ui.editDate.setText(curDateTime.toString("yyyy-MM-dd"))#设置字符串显示格式

		self.ui.dateTimeEdit.setDateTime(curDateTime)
		self.ui.editDateTime.setText(curDateTime.toString("yyyy-MM-dd hh:mm:ss"))#设置字符串显示格式
	def on_calendarWidget_selectionChanged(self):
		'''
		设置日历组件
		data类型是PyQt5.QtCore.QDate(2020, 3, 3)
		:return:
		'''
		data = self.ui.calendarWidget.selectedDate()
		print(data)
		self.ui.editCalendar.setText(data.toString("yyyy年MM月dd日"))#设置字符串在QLineEdit组件中的显示格式

	def on_btnSetTime_clicked(self):
		tmStr = self.ui.editTime.text()#得到的是一个字符串
		#fromString(str, str)
		#fromString(str, format: Qt.DateFormat = Qt.TextDate)
		tm = QTime.fromString(tmStr,"hh:mm:ss")#格式化获取的QlineEdit中的时间,格式要与目标函数的格式一致
		self.ui.timeEdit.setTime(tm)

	def on_btnSetDate_clicked(self):
		dtStr = self.ui.editDate.text()
		dt = QDate.fromString(dtStr,"yyyy-MM-dd")
		self.ui.dateEdit.setDate(dt)

	def on_btnSetDateTime_clicked(self):
		dttmStr = self.ui.editDateTime.text()
		dttm = QDateTime.fromString(dttmStr,"yyyy-MM-dd hh:mm:ss")
		self.ui.dateTimeEdit.setDateTime(dttm)


	##=========自定义槽函数============

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyWidget()
	form.show()

	sys.exit(app.exec_())