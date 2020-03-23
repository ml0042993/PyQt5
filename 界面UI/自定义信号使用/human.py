import sys
from PyQt5.QtCore import QObject,pyqtSlot,pyqtSignal

class Human(QObject):
    '''
    定义两个信号,定义为类属性,
    nameChanged信号带有str类型参数的信号
    ageChanged信号带有[int][str]两个参数类型,是overload型信号

    信号的发射通过emit()函数;在类的某个状态发生变化,需要通知外部发生了这种变化时,发射相应信号.如果关联了 槽函数,就会执行槽函数
    '''
    #定义一个带str类型参数的信号
    nameChanged = pyqtSignal(str)
    #overload型信号有两种参数，一个是int，一个是str
    # overload型信号的第一个参数是默认值
    ageChanged = pyqtSignal([int],[str])

    def __init__(self,name='Mike',age=10,parent=None):
        super().__init__(parent)
        self.setAge(age)
        self.setName(name)

    def setAge(self,age):
        self.__age = age
        self.ageChanged.emit(self.__age)#第一次发射ageChanged信号,int参数信号
        if age<=18:
            ageInfo = '你是少年'
        elif (18<age<=35):
            ageInfo = '你是年轻人'
        elif (35<age<=55):
            ageInfo = '你是中年人'
        elif (55<age<=80):
            ageInfo = '你是老人'
        else:
            ageInfo = '您是 寿星'
        self.ageChanged[str].emit(ageInfo)#第二次发射ageChanged信号,str参数信号
    def setName(self,name):
        self.__name = name
        #当self.__name发生变化时发射nameChanged信号,并传递参数self.__name,关联的槽函数可以从参数中获得当前信号的名称
        self.nameChanged.emit(self.__name)
class Responsor(QObject):
    '''
    定义三个函数用于和Human类实例对象的信号建立关联
    由于ageChanged有两个类型,所以需要定义两个槽函数
    @pyqtSlot用于声明槽函数的参数类型,
    下面的3个槽函数都可以去掉该修饰符,原因是因为overload型信号的两个槽函数名称不同,在建立连接是也指定了参数类型
    '''
    @pyqtSlot(int)
    def do_ageChanged_int(self,age):
        print('你的年龄是: '+str(age))
    @pyqtSlot(str)
    def do_ageChanged_str(self,ageInfo):
        print(ageInfo)
    @pyqtSlot(str)
    def do_nameChanged(self,name):
        print('Hello,'+name)

if __name__ == '__main__':
    '''
    先创建类的实例,再进行信号与槽的关联
    创建连接时会发射信号,但由于未建立连接,所以无响应
    '''
    print('**创建对象时**')
    boy = Human("boy",16)#创建实例
    resp = Responsor()#创建实例
    #如果一个信号的名称是唯一的,即不是overload型,则关联时无需列出信号的参数
    boy.nameChanged.connect(resp.do_nameChanged)
    #overload型信号的第一个参数是默认值,如果关联的是第一个参数类型的信号,则无需说明
    boy.ageChanged.connect(resp.do_ageChanged_int)
    #overload对于非默认参数,必须在信号关联时在信号中注明参数
    boy.ageChanged[str].connect(resp.do_ageChanged_str)

    print('\n **建立关联后**')
    # 建立连接后,三个信号关联的槽函数也进行了响应
    boy.setAge(35)
    boy.setName('Jack')

    boy.ageChanged[str].disconnect(resp.do_ageChanged_str)
    print('\n **断开 ageChanged[str]的关联后**')
    #断开后关联槽函数无响应
    boy.setAge(10)

