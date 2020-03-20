import sys
from PyQt5 import QtWidgets

import ui_Dome

app = QtWidgets.QApplication(sys.argv)#使用QApplication类创建应用程序实例app

baseWidget = QtWidgets.QWidget()#创建窗体基类 QtWidgets的实例,baseWidget是基本的QWidget窗体,没有其他设置

ui = ui_Dome.Ui_MainWindow()# 使用ui_FormHello模块中的类创建对象ui

ui.setupUi(baseWidget)#setupUi在ui_FormHello中只创建窗体上的其他组件,并不是容器, 容器是外部传入的baseWidget,是将其创建的组件放入到baseWidget中

baseWidget.show()#不能使用ui.show(),ui的基类是object,不是窗体界面的类

#修改标签上的文字,不能运行,
#可能是因为setText只能由QMainWindow类调用
# ui.label.setText('Hello , 我被修改')

sys.exit(app.exec_())
