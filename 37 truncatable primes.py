##define a function to check if a number is prime
##then run two separate functions to check if the numbers are truncatable from both left and right
##sum the truncatable primes weve found

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
		



def truncleft(z):
	while isprime(z):
		z=str(z)
		if len(z)==1:
			z=int(z)
			if isprime(z):
				return True
			else:
				return False
		z=z[1:]
		z=int(z)
	else:
		return False

def truncright(z):
	while isprime(z):
		z=str(z)
		if len(z)==1:
			z=int(z)
			if isprime(z):
				return True
			else:
				return False
		z=z[0:(len(z)-1)]
		z=int(z)
	else:
		return False

v=3797
sum=0

for x in range(10,1000000):
	if isprime(x):
		if truncleft(x) and truncright(x):
			print('gallelujah,',x,' is a truncker')
			sum+=x
else:
	print(sum)
