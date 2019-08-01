'''count the number of 2s that occur in a range of numbers'''

def count2(x):
	counter=0
	for i in range(x):
		i=str(i)
		for char in i:
			if char=='2':
				counter+=1
	return counter
			
print(count2(50))
	
'''
count=0
for a in range(26):
	a=str(a)
	for char in a:
		if char=='2':
			count+=1

print(count)'''
