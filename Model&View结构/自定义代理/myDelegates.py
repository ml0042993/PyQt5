from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtWidgets import QDoubleSpinBox,QComboBox
from PyQt5.QtCore import Qt

##=====================基于QDoubleSpinbox的代理组件=============================
class QmyFloatSpinDelegate(QStyledItemDelegate):
	def __init__(self,minV=0,maxV=10000,digi=2,parent=None):
		super().__init__(parent)
		self.__min=minV
		self.__max=maxV
		self.__decimals=digi

	def createEditor(self, parent, option, index):
		editor = QDoubleSpinBox(parent)
		editor.setFrame(False)
		editor.setRange(self.__min,self.__max)
		editor.setDecimals(self.__decimals)
		return editor

	def setEditorData(self, editor, index):
		model = index.model()
		text = model.data(index,Qt.EditRole)
		editor.setValue(float(text))

	def setModelData(self, editor, model, index):
		value = editor.value()
		model.setData(index, value, Qt.EditRole)

	def updateEditorGeometry(self, editor, option, index):
		editor.setGeometry(option.rect)
