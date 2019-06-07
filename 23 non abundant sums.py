#function to find abundant numbers. returns list

def abun(x):
	listofnums=[]
	for i in range(x):
		sum=0
		for y in range (1,i):
			if i%y == 0:
				sum=sum+y
		else:
			if sum > i:
				listofnums.append(i)
	return listofnums
			

#function to search for numbers that are a produxt of sum of abundant numbers. one optimization is to check if the i in listofnums is higher than x, then add to sum and break. could probably be optimized further.
def search(listofnums):
	check=0
	sum=0
	for x in range(28124):
		for i in listofnums:
			check=x-i
			if check in listofnums:
				break
			elif i>check:
				sum = sum+x
				print(sum)
				break
		else:
			sum=sum+x
	
	return sum
			
				
			

print(search(abun(28124)))
			
