'''
heres another problem simplified by our old buddy string - 
first we have a basic function to check for primes.
then we build a list of n-digit pandigital numbers by concatenating strings and following certain rules
finally we filter the non-primes out of our list amd we are left with only pandigital primes
strangely enough, it seems that pandigital primes are either 4 or 7 digits long
'''

def isprime(x):
	if x==1:
		return False
	for i in range(2,x):
		if x%2==0:
			return False
		elif x%i==0:
			return False
		elif i*i>x:
			return True
	else:
		return True



pans=[]
for i in range(10000000):
	builder=''
	i=str(i)
	for c in i:
		c=int(c)
		if c==0:
			break
		elif c < (len(i) +1):
			c=str(c)
		else:
			break
		if c not in builder:
			builder+=c
		else:
			break
	else:
		pans.append(builder)

primes=[]
for num in pans:
	num=int(num)
	if isprime(num):
		primes.append(num)

print(primes)
	
