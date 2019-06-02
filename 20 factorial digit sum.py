def fact(x):
	prod=1
	while x > 1:
		prod = prod*x
		x=x-1
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

print(splitsum(fact(100)))



