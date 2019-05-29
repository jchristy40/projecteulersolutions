count = 0
y = 0
while count < 10001:
	for x in range(2, 50000000):
		if count>=10001:
			break
		for y in range(2, x):
			if x % y == 0:
				break
			elif y*y>x:
				count=count+1
				print(x)
				print(count)
				break
		else:
			count = count + 1
			
			

print(x-1)
#while count < 10001:
	#for x in range(5000):
		
		
		
		
		
	#	
	#	for y in range(2, x):
			###if x % y == 0:
			#	print(x)
			
				
#print(x)
#print(count)###
