##this is hacked together a little bit. recip is a function to find the longest repeating sequence. primes finds all prime numbers not divisible by 2 or 5. recip enters an infinite loop if it has to process a non- prime number (or 5). this problem really beat me up 
def recip(nums):
	
	builder=''
	holder=0

	first=1
	max=0
	maxnum=0
	for i in nums:
		builder=''
		holder=0
		first=1
		
		
		while first!=holder:
			holder=1
			builder=builder+str(first)
			first=first*10 
			first=first%i
		else:
			if len(builder)>max:
				max=len(builder)
				maxnum=i
			print('i is ', i,' and len is ',len(builder),' and max so far is',max,' derived from ',maxnum)
	else:
		print('the highest number is ', maxnum)
	
def primes(x):
	nums=[]
	for i in range(3,x):
		for y in range(3,i):
			if i%2==0:
				break
			if i%5==0:
				break
			if i%y==0:
				break
		else:
			nums.append(i)
	else:
		return nums

recip(primes(1000))
