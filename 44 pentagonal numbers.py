'''
this one is weird and easy
we are provided with the equation to calculate pentagonal numbers, so the first step is to generate a list of pentagonal numbers
note also that we are generating a dictionary with the same numbers
the dictionary lets us look up the sums and differences very quickly for the second stage
then we iterate through our list of pentagonal numbers, checking if both the sum and difference are in the dictionary
'''
pents=[]
dict={}
for x in range(1,5000):
	pent=0
	pent=x*(3*x-1)/2
	pents.append(pent)
	dict[pent]=x
	

 	
x=0
z=0
for i in pents:
	for j in pents:
		if j>i:
			break
		x=i+j
		z=i-j
		if x in dict and z in dict:
			print(i,j, ' both here and their difference is: ',(i-j))
	##	else:
		##	print('no')
