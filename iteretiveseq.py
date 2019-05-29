n = 0
list = []

def iterate(n):
	list=[]
	while n != 1:
		list.append(n)
		if n%2==0:
			n = n//2
		else:
			n = 3*n+1
	else:
		list.append(n)
		return list
	

max=0

def listmax():
	max=0
	for x in range(1,1000000):
		list=iterate(x)
		if len(list) > max:
			max=len(list)
			print(max)
			print(x)
	else:
		return max
	


print(listmax())

