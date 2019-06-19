##first generate a list with all terms
##sort the list. then remove duplicates. 

def combo():
	list=[]
	temp=0
	for a in range(2,101):
		for b in range(2,101):
			temp=0
			temp=a**b
			list.append(temp)
	else:
		return list


def sortdupe(list):
	list.sort()
	newlist=[]
	for i in list:
		if i not in newlist:
			newlist.append(i)
	else:
		print(len(newlist))
		

sortdupe(combo())


