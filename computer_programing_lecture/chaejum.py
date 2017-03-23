#made by dongdongju

import sys

# Student 정보 class
class Student:
	def __init__(self,name,score,time):
		self.name=name
		self.score=score
		self.time=time
		self.rank=-1
		self.cal_score=0
	
	def CalculateScore(self):
		self.cal_score=100-(self.rank*2)
	def print_rank(self):
		print(self.rank)

	def print_all(self):
		print(self.name,self.score,self.time,self.rank)

	@staticmethod
	def key_by_score(student):
		return -student.score

	@staticmethod
	def key_by_time(student):
		return student.time

# 한분반  class

class Students:
	def __init__(self,data):
		self.students=[]
		for line in data:
			try: # 모든 데이터가 잘 들어올 경우
				name,score,time=line.split()
				self.students.append(Student(name,int(score),int(time)))
			except: 
				name=line.rstrip()
				self.students.append(Student(name,-2,-2))
		self.max_score=-2
		self.max_score=self.findMaxScore()
		self.max_people=len(self.students)


	def print_students(self):
		for i in self.students:
			i.print_all()

	
	def findMaxScore(self):
		max_score=-2
		for i in self.students:
			if i.score > max_score:
				max_score=i.score
		return max_score

# 데이터 path 로 부터 읽어옴
# return : matrix
def getDataFromText(path):
	data_array=[]
	f=open(path,"r")
	lines = f.readlines()
	for line in lines:
		data_array.append(line) 
	f.close()
	return data_array

def exportDataToFile(data,path):
	write_path=path.split(".")[0]
	f=open(write_path+"_result.txt","w")
	f.write("name\t\tscore\ttime\trank\tcal_score\n")
	for line in data:
		f.write(line.name+"\t"+str(line.score)+"\t"+str(line.time)+"\t"+str(line.rank)+"\t"+str(line.cal_score)+"\n")
	f.close()

def calculateRank(sts):
	ranked_students=[]
	sts.students.sort(key=Student.key_by_score)

	for x in range(sts.max_score+1,1,-1): # X~1 까지
		part_student=[]
		for i in sts.students:
			if i.score == x:
				part_student.append(i)
		if len(part_student) == 0:
			continue
		part_student.sort(key=Student.key_by_time)
		for t in part_student:
			ranked_students.append(t)	
	rank=1
	for i in range(len(ranked_students)):
		try: #다음 인자가 없을떄까지
			if(ranked_students[i].time == ranked_students[i+1].time):
				ranked_students[i].rank=rank
				continue
			else:
				ranked_students[i].rank=rank
				rank=rank+1
				continue
		except:
			ranked_students[i].rank=rank
			break
	sts.students=ranked_students
	for x in sts.students:
		x.CalculateScore()

			
		
def _main():
	path=sys.argv[1]
	meta=getDataFromText(path)	
	sts=Students(meta)
	calculateRank(sts)
	exportDataToFile(sts.students,path)

if __name__=="__main__":
	_main()
