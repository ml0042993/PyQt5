#应用程序主程序文件
#GUI应用程序主程序

import sys
from PyQt5.QtWidgets import QApplication
from myDialog import QmyDialog

app = QApplication(sys.argv)

mainform = QmyDialog()
mainform.show()
sys.exit(app.exec_())
