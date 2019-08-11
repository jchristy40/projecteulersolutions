'''this one is so simple, im not sure how it ended up as problem 48
we declare two variables, one a temporary variable to hold our derived numbers, and another to sum and receive our answer.
we run a loop and sum all our self powered numbers
then convert to a string and find the last ten digits for our answer
'''

sum=0
power=0

for i in range(1,1001):
	power=i**i
	sum+=power




sum=str(sum)

print(sum[-10:])
