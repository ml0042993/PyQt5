import re
import xlrd
import os

TYPE = ['单选题','多选题','判断题']
# SORT = [('单选题',1),('多选题',2),('判断题',3)]
TIT_WORD = re.compile(r'第\s*\d+\s*题')
KEY_WORD = re.compile(r'.+(?=A\.)')#选取A.前面的内容
INI_WORD = re.compile(r'A\.')
REP_WORD = re.compile(r'A.\s+')#A.后面若干空格
FILE_PATH = os.getcwd()+"\File\exam_bat"#格式化后的文件路径
TEMP_PATH = os.getcwd()+"\File\exam_tmp"#临时文件路径
print(FILE_PATH)
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
	Model_Data=[]
	Temp_List=[]
	with open(FILE_PATH,'r',encoding="utf-8") as f:
		Start = 0
		End = 0

		lines = f.readlines()
		for i in range(len(lines)):
			title_Num = TIT_WORD.search(lines[i])
			if title_Num:
				Start=i
			End+=1
			Temp_List.append(lines[Start:End])
		print(Temp_List)
def question_num():
	question_num=[]
	with open ('./File/exam.txt','r' , encoding='utf8') as ef:
		lines = ef.readlines()
		x = None
		y = None
		for i in range(len(lines)):
			num_question = NUM_WORD.search(lines[i])
			anchor = KEY_WORD.search(lines[i])
			if num_question:
				x = i
			elif anchor :
				y = i
			if x!=None and y!=None:
				line_anchor = lines[x+1:y+1]
				x, y = None, None
				print(line_anchor)

def question_tit():
	question_tit=[]
	with open('./File/exam.txt', 'r', encoding='utf8') as ef:
		lines = ef.readlines()
		for line in lines:
			anchor = key_word.search(line)
			if anchor:
				# flag_num +=1
				message = anchor.group()
				result = re.sub('\s+', '', message)
				question_title = re.sub('（）', '()', result)
				question_tit.append(question_title)
	return question_tit

def question():
	question = []
	for i in range(len(question_num())):
		question.append([question_num()[i],question_tit()[i]])
	return question

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
	# question_num()
	Ini_Model_Data()