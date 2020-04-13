import re
import xlrd

TYPE = ['单选题','多选题','判断题']
# SORT = [('单选题',1),('多选题',2),('判断题',3)]

def question_num():
	question_num=[]
	num_word = re.compile(r'第\s*\d+\s*题')
	with open ('./File/exam.txt','r' , encoding='utf8') as ef:
		lines = ef.readlines()
		# flag_num = 0
		for line in lines:
			num_question = num_word.search(line)
			if num_question:
				num = num_question.group()
				question_number = re.sub('\s+','',num)
				question_num.append(question_number)
	return question_num
def question_tit():
	question_tit=[]
	key_word = re.compile(r'.+(?=A\.)')
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
	read_answer = xlrd.open_workbook('./flie/exam_excle.xls')
	sheet = read_answer.sheet_by_index(0)
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
	# for question_number,question_title in question():
	# 	for contrast in excle_answer():
	# 		if question == contrast[1]:
	# 			print(question_number,contrast[1],judge(contrast))
	# 			break
	# 		else:
	# 			print("can't find it")
	for i in question():
		print(i)
	print(len(question_tit()))