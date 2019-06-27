#binary is a function to convert decimal numbers to binary numbers.
#then we check for numbers that are palindromic by reversing the string.
# if the number is a palindrome, convert it to binary and then check if that too is a palindrome
# append double base palindromes to a list and sum them

def binary(x):
	built=''
	while x != 0:
		built=str(x%2)+built
		x=x//2
	return built
	


y=''
build=''
rev=''
list=[]
for x in range(1,1000000):
	x=str(x)
	y=x[::-1]
	if y==x:
		x=int(x)
		build=binary(x)
		rev=build[::-1]
		if rev==build:
			list.append(x)

print(list)

sum=0
for i in list:
	sum+=i

print(sum)
		
