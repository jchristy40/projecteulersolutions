##first break the numbers into strings
##raise each number to the fifth power and sum
##if the sum of numbers is the original number, append to list the original number
##finally calculate the final sum by iterating over our list

breaker=''
sum=0
list=[]
for i in range(2,1000000):
	sum=0
	breaker=str(i)
	for x in breaker:
		x=int(x)
		x=x**5
		sum=sum+x
	else:
		if i==sum:
			list.append(i)


finalsum=0
for z in list:
	finalsum+=z

print(list)
print(finalsum)


		
	
