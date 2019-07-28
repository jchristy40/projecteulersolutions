'''
this one has a lot going on, but its not too difficult overall.
first we have a function to check if numbers are prime.
we will use this to generate a list of primes and a list of odd composite numbers
we will also create a dictionary for 2*(n**2) so that we can check twice squared numbers
finally, we loop through our list of odd composite numbers, and check if they are the sum of a prime and a 2*(n**2) number
if we loop through and dont find that our prime number can be summed in that way, we have our answer.
note of minor interest: we also quickly find another odd composite number that doesnt qualify, but do not find any more in a fairly large range above that 
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
		
twosqd={}
for i in range(1,10000):
	i=i**2
	i=2*i
	twosqd[i]=1

primes=[]
comps=[]
for j in range(3,20000,2):
	if isprime(j):
		primes.append(j)
	else:
		comps.append(j)
	
for num in comps:
	for prime in primes:
		if prime>num:
			print('not here, comp is ', num)
			break
		z=0
		z=num-prime
		if z in twosqd:
			 break
	else:
		print(comp)
