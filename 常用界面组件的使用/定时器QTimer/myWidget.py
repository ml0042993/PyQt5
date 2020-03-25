import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import QTime,QTimer
# from PyQt5.QtGui import
# from PyQt5.QtWidgets import
# from PyQt5.QtSql import
# from PyQt5.QtMultimedia import
# from PyQt5.QtMultimediaWidgets import
#QTimer是一个不可见的组件界面，在组件界面内没有它
from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建窗体
		self.ui = Ui_Widget()#创建Ui对象
		self.ui.setupUi(self)#构造UI

		self.timer = QTimer()#创建定时器
		self.timer.stop()
		self.timer.setInterval(100)#设定周期
		self.timer.timeout.connect(self.do_timer_timeout)
		self.counter = QTime()

	##==========自定义功能函数==========

	##==========事件处理函数===========

	##==========由connectSlotsByName()自动关联的槽函数====
	def on_btnStart_clicked(self):
		self.timer.start()
		self.counter.start()
		self.ui.btnStart.setEnabled(False)
		self.ui.btnStop.setEnabled(True)
		self.ui.btnSetIntv.setEnabled(False)


	def on_btnStop_clicked(self):
		self.timer.stop()
		tmMs = self.counter.elapsed()#计时器经过的时间
		ms = tmMs%1000#毫秒
		sec = tmMs/1000#秒
		timeStr = "经过的时间：{}秒，{}毫秒".format(sec,ms)
		self.ui.LabElapsedTime.setText(timeStr)
		self.ui.btnStart.setEnabled(True)
		self.ui.btnStop.setEnabled(False)
		self.ui.btnSetIntv.setEnabled(True)

	def on_btnSetIntv_clicked(self):
		self.timer.setInterval(self.ui.spinBoxIntv.value())
	##=========自定义槽函数============
	def do_timer_timeout(self,):
		curTime = QTime.currentTime()
		self.ui.LCDHour.display(curTime.hour())
		self.ui.LCDMin.display(curTime.minute())
		self.ui.LCDSec.display(curTime.second())

	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyWidget()
	form.show()

	sys.exit(app.exec_())