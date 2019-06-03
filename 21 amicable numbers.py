def finddn(nums):
	# find d(n), add it to a dictionary, and return the dictionary
	sum=0
	listofsums={}
	for x in range(nums):
		sum=0
		for y in range(1,x):
			if x%y==0:
				sum=sum+y	
		else:
			listofsums[x]=sum
	else:
		return listofsums
			
		
def inversion(listofsums):
	##my original solution attempted to invert the dictionary but that caused heinous problems. this solution still inverts the numbers, but we search in the original dictionary with the inversion being represented in the variables 
	
	##invert={}
##	for x in listofsums:
		##invert[listofsums[x]]=x
	
	
		
	sum=0
	
	for i in listofsums:
		key=listofsums[i]
		value=i
		if key in listofsums and value==listofsums[key] and key!=value:
			sum=sum+key
			print(key, value)
			
			
	return sum
	

print(inversion(finddn(10001)))


			
			
