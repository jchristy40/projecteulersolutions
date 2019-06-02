def fact(prod,x):
	while x > 1:
		prod = prod*x
		return fact(prod,x-1)
	else:
		return prod
		
def splitsum(x):
	x=str(x)
	n=1
	sum=0
	splitter=[x[i:i+n] for i in range(0,len(x), n)]
	for y in splitter:
		y=int(y)
		sum = sum + y
	return sum

print(splitsum(fact(1,1000)))


