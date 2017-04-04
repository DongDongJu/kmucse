def getData():
	f=open("input.txt")
	num_of_datas=int(f.readline())
	data_set=[]
	for i in range(num_of_datas):
		data=[]
		t,t1=f.readline().split()
		num_of_days,teams=int(t),int(t1)
		t2=f.readline().split()
		costs=[]
		for x in t2:
			costs.append(int(x))
		data_set.append([num_of_days,teams,costs])
	f.close()
	return num_of_datas,data_set

def subResult(costs,start,end):
	sum_=0
	for i in range(start,end+1):
		sum_=sum_+costs[i]
	return float(sum_)/(end-start+1)

def calculateMin(data_set):
	num_of_days=data_set[0]
	teams=data_set[1]
	costs=data_set[2]

	start=teams
	end=num_of_days
	min_=101
	for i in range(len(costs)):
		for x in range(start,end+1):
			if i+x > len(costs):
				continue
			t=subResult(costs,i,i+x-1)
			if min_ > t:
				min_=t
	return min_

def mainLoop(num_of_datas,data_set):
	for x in range(num_of_datas):
		print calculateMin(data_set[x])

if __name__=="__main__":
	num_of_datas,data_set=getData()
	mainLoop(num_of_datas,data_set)
