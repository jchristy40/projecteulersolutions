##declare the first 2 fibonacci numbers, append them to a list. then generate a list of fibonacci numbers, and break the loop when the length of the fibonacci number exceeds 1000. the length of the list is the index, since we technically are starting at 1

def fiblist():
	list=[]
	x=1
	y=1
	list.append(x)
	list.append(y)
	z=0
	for i in range(5000):
		z=x+y
		x=y
		y=z
		z=str(z)
		list.append(z)
		if len(z)>=1000:
			print(len(list))
			print('breaking')
			break
		z=int(z)
		
		


fiblist()
