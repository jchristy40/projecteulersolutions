'''
we can arrive at the solution by building strings and following certain rules. 
we add our derived product to a string and return out of our function if a number repeats or if the figure becomes larger than nine.
this way, we are constrained to only building up the string if it meets the requirements of the problem, i.e. being pandigital 1-9 and being nine figures
then we loop through numbers below 10000 and the solution is in there. 
i commented out my first try at this. it needed to be in a function so that we could return from an inner loop. i also made a strange mistake where i tried to check if the derived product was in the string before breaking the serived product into single characters. that was unnecessary - only the single characters shoukd be checksd 

'''
def strbuilder(x):
	build=[]
	multiplier=1
	derived=multiplier*x
	while len(build)<9:
		derived=str(derived)
		for i in derived:
			if i == '0':
				return False
			if i not in build:
				build.append(i)
			else:
				return False
		multiplier+=1
		derived=x*multiplier
		if len(build)>9:
			return False
	else:
		return build

for y in range(10000):
	if strbuilder(y)!= False:
		print(strbuilder(y),y)
		

##build=[]
#multiplier=1
#z=488
#derived=multiplier*z
#while len(build) < 9:
#	derived=str(derived)
#	if derived not in build:
#		for i in derived:
#			if i not in build:
	#			build.append(i)
#			else:
#				break
#		multiplier+=1
#		derived=z*multiplier
#	if len(build)==9:
#		print(build)
#	if len(build)>9:
	#	print('oops')
	




