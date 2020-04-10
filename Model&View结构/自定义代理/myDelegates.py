from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtWidgets import QDoubleSpinBox,QComboBox
from PyQt5.QtCore import Qt

##=====================基于QDoubleSpinbox的代理组件=============================
class QmyFloatSpinDelegate(QStyledItemDelegate):
	def __init__(self,minV=0,maxV=10000,digi=2,parent=None):
		super().__init__(parent)
		self.__min=minV#最小值
		self.__max=maxV#最大值
		self.__decimals=digi#小数位数

	def createEditor(self, parent, option, index):
		'''
		创建需要的编辑器组件,并作为函数的返回值,双击单元格进入编辑状态时,会调用此函数创建一个QDoubleSpinBox组件并显示在单元格里
		:param parent: 代理组件的父容器对象
		:param option: QStyleOptionViewItem类型变量,可对创建的编辑器组件的效果做高级设置
		:param index: QModelIndex变量,关联数据项的模型索引,通过index.model()可以获取关联的数据模型
		:return:
		'''
		editor = QDoubleSpinBox(parent)#实例一个QDoubleSpinBox组件
		editor.setFrame(False)
		editor.setRange(self.__min,self.__max)#设置数值范围
		editor.setDecimals(self.__decimals)#设置精度
		return editor

	def setEditorData(self, editor, index):
		'''
		从数据模型获取数据,供widget组件进行编辑,双击进入编辑状态时会调用
		:param editor:Widget组件
		:param index:QModelIndex变量,关联数据项的模型索引,通过index.model()可以获取关联的数据模型
		:return:
		'''
		model = index.model()#获取关联的数据模型
		text = model.data(index,Qt.EditRole)#获取 单元格文字
		editor.setValue(float(text))#将text转化问浮点型.在赋值为代理组件的显示值

	def setModelData(self, editor, model, index):
		'''
		用于将代理编辑器上的值更新到数据模型,在界面上完成编辑时会自动调用此函数
		:param editor:
		:param model:
		:param index:
		:return:
		'''
		value = editor.value()
		model.setData(index, value, Qt.EditRole)

	def updateEditorGeometry(self, editor, option, index):
		'''
		用于为代理组件editor的显示效果进行设置
		:param editor:
		:param option: 是QStyleOptionViewItem类型变量,rect属性定义了单元格适合显示代理组件的大小
		:param index:
		:return:
		'''
		editor.setGeometry(option.rect)
