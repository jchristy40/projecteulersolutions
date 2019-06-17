##this one is simpler than it seems. first define a function to check for primes
##then simply loop through all variations of a and b
##keep track of the highest count of consecutive primes and print the values for a and b

def isprime(x):
	for i in range(2,x):
		if x%2==0:
			return False
		elif x%i==0:
			return False
		elif i*i>x:
			return True
	else:
		return True

equat=0
count=0
maxcount=0
for a in range(-1000,1000):
	for b in range(-1000,1001):
		count=0
		for n in range(80):
			equat=(n**2)+(a*n)+b
			equat=abs(equat)
			if not isprime(equat):
				break
			elif isprime(equat):
				count+=1
				if count>maxcount:
					maxcount=count
					print('the new max is ',maxcount,' derived from ',a,' and ',b,)
			
	
