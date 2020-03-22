import sys
from PyQt5.QtCore import QObject,pyqtSlot,pyqtSignal

class Human(QObject):
    #定义一个带str类型参数的信号
    nameChange = pyqtSignal(str)
    #overload型信号有两种参数，一个是int，一个是str
    ageChange = pyqtSignal([int],[str])

    def __init__(self,name='Mike',age=10,parent=None):
        super().__init__(parent)
        self.setAge(age)
        self.setName(name)

    def setAge(self,age):
        self.__age = age
        self.ageChange.emit(self.__age)
        if age<=18;

