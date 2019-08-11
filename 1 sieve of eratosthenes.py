'''this is the so-called sieve of eratosthenes.
you would use this any time you need to quickly generate a list of primes.
first we need a function to determine if a number is prime or not.
then we declare a list of whatever range we so desire
next, we run through the list. if a number is prime, we remove any of its multiples from the list
we use a while loop to be sure we are only working within the bounds of our initial list
the numbers that remain are prime.

this is particularly useful when trying to generate many primes. for example, the project euler problem that asks for the 10,001st prime becomes easier using this idea; i attempted to solve it before knowing about the sieve of eratosthenes and went through a lot of pain trying to figure out how to get the loops under control
one more thing ill add is that this could potentially go faster by fully optimizing the isprime function'''

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

z=list(range(2,10000))

'''multiply the prime as many times as necessary to remove its multiples'''

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


print(z)
