import re
import xlrd
import os

TYPE = ['单选题','多选题','判断题']
TIT_WORD = re.compile(r'第\s*\d+\s*题')
KEY_WORD = re.compile(r'.+(?=A\.)')#选取A.前面的内容
INI_WORD = re.compile(r'A\.')
REP_WORD = re.compile(r'A.\s+')#A.后面若干空格
FILE_PATH = os.getcwd()+"\File\exam_bat"#格式化后的文件路径
TEMP_PATH = os.getcwd()+"\File\exam_tmp"#临时文件路径
def ini_File():
	'''
	初始化文档,令A.选项进入下一行
	:return:
	'''
	with open(FILE_PATH, 'w', encoding='utf-8') as f:
		with open ('./File/exam.txt','r' , encoding='utf8') as ef:
			lines = ef.readlines()
			for line in lines:
				anchor = INI_WORD.search(line)
				if anchor:
					result = re.sub("A.","\n       A.",line)#令A选项格式化到下一行,并和B选项对齐
					line = result
				f.write(line)
	with open(TEMP_PATH,'w',encoding="utf-8") as nf:
		with open(FILE_PATH,'r',encoding="utf-8") as f:
			lines = f.readlines()#按行读取文件,返回的是一个列表
			for i in range(len(lines)):
				if lines[i]=='\n':#列表元素为空则不进行判断,进入下一行遍历
					continue
				anchor = REP_WORD.search(lines[i])
				if anchor:
					result = re.sub('A.\s+',"A.  ",lines[i])#格式化A.选项,令其后只有两个空格
					lines[i] = result#替换当前元素
				nf.write(lines[i])
	os.remove(FILE_PATH)
	os.rename(TEMP_PATH,FILE_PATH)

def Ini_Model_Data():
	'''
	格式化文档，将题目和选项放入一个列表内，合并为一个二维列表
	:return:
	'''
	Model_Data=[]
	with open(FILE_PATH,'r',encoding="utf-8") as f:
		Start = 0
		End = 0
		lines = f.readlines()
		for i in range(len(lines)):
			title_Num = TIT_WORD.search(lines[i])
			lines[i]=lines[i].replace(" ","")#去除空格
			lines[i]=lines[i].replace("\n","")#去除换行符
			if title_Num:
				lines[i]=title_Num.group()#更换题号为第 XX 题
				Model_Data.append(lines[Start:i])#将lines切片添加到列表中，说明Start初始为0，当title_num匹配后i=2，之后再修改Start=i即为2
				Start = i#切片后再修改行号，否则切片使用的锚点会一样，切片为空列表
			End=i#拿到文档的最后一行行号
		# 遍历中切片的最后一个lines[Start:i]的锚点分别为第99题的行号Start和第100题的行号i，当Start=i以后title_Num条件无法达成，不会对100题内容进行切片
		Model_Data.append(lines[Start:End])
	return Model_Data
def excle_answer():
	read_answer = xlrd.open_workbook('./File/exam_excle.xls')
	sheet = read_answer.sheet_by_index(0)
	print(sheet)
	for i in range(sheet.nrows):
		rows = sheet.row_values(i)
		if TYPE.__contains__(rows[5]):
			rows = rows[5:9]
			try:
				rows[1] = rows[1].replace(' ','')
				rows[1] = rows[1].replace('（）','()')
				rows[2] = rows[2].split('$;$')

			except Exception as e:
				print(e)
			yield rows

def judge(args):
	answer = []
	args[3] = args[3].replace('A','0')
	args[3] = args[3].replace('B','1')
	args[3] = args[3].replace('C','2')
	args[3] = args[3].replace('D','3')
	args[3] = args[3].replace('E','4')
	args[3] = args[3].replace('F','5')
	args[3] = args[3].replace('G','6')
	# print(args)
	for num in  args[3]:
		answer.append(args[2][int(num)])
	return answer
if __name__ == '__main__':
	Ini_Model_Data()