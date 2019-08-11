'''
this one isnt conceptually too difficult, but it caused me to finally attempt to code the sieve of eratosthenes.
we are looking for the first four consecutive numbers that each have 4 or more prime factors
first we have a function to find primes
then we generate a list of primes with the sieve of eratosthenes.
then we have a fairly simple algorithm.
we have two counters - first, a variable to count the number of prime factors
then we have a counter variable that increases in case a number has four or more prime factors; this variable resets to zero if the 'next' number does not have four or more prime factors; this is how we find the consecutive numbers that meet our condition
finally, once we have found the numbers thet meet our conditions, we print the first number in that series

'''


def isprime(x):
	if x==1:
		return False
	if x==2:
		return True
	for i in range(3,x,2):
		if x%2==0:
			return False
		elif x%i==0:
			return False
		elif i*i>x:
			return True
	else:
		return True

z=list(range(2,22000))

a=0
'''multiply the prime as many times as necessary to remove the multiples'''

for y in z:
	if isprime(y):
		a=0
		multiplier=2
		while a<z[-1]:
			a=y*multiplier
			multiplier+=1
			try:
				z.remove(a)
			except:
				continue



consec=0
for i in range(1,150000):
	counter=0
	for j in z:
		if i%j==0 and i!=j:
			counter+=1
		if j>i:
			if counter>=4:
				consec+=1
			else:
				consec=0
			if consec>=4:
				print(i-3)
			break
	else:
		if counter>=4:
			consec+=1
		else:
			consec=0
		if consec>=4:
			print(i-3)

'''
consec=0
for i in range(1,21):
	counter=0
	for j in z:
		if i%j==0 and i!=j:
			counter+=1
		if j>i:
			if counter>=2:
				consec+=1
			else:
				consec=0
			if consec>=2:
				print(i)
			break
	else:
		if counter>=2:
			consec+=1
		else:
			consec=0
		if consec>=2:
			print(i)
		
		
'''




'''g=[]
for c in range(2,100):
	if isprime(c):
		g.append(c)
		
print(z)
print(g)
'''
