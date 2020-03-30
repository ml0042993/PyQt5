#将myDialog.py中的窗体测试部分单独拿出来作为一个文件,在具有多个窗体的GUI项目里,appMain文件创建主窗体然后运行应用程序

import sys
from PyQt5.QtWidgets import QApplication
from myMainWindow import QmyMainWindow

app = QApplication(sys.argv)

mainform = QmyMainWindow()
mainform.show()
sys.exit(app.exec_())
