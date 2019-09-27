'''simple and fast - multiply x many times, convert to strings, check if the sorted versions are equal'''

for x in range(1000000):
	x2=str(x*2)
	x3=str(x*3)
	x4=str(x*4)
	x5=str(x*5)
	x6=str(x*6)
	x=str(x)
	if sorted(x)==sorted(x2) and sorted(x)==sorted(x3) and sorted(x)==sorted(x4) and sorted(x)==sorted(x5) and sorted(x)==sorted(x6):
		print(x)
	
	

