'''this one reuses a function from an earlier problem in order to find permutations of an array.
all we need to do to solve this problem is check each permutation 
we break out substrings and then see if theyre divisible by the increasing primes
if the number checks all the right boxes, we write it to a new list, then simply sum the list'''

def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    
    return True

arr=[0,1,2,3,4,5,6,7,8,9]
list=[]
while arr != [9,8,7,6,5,4,3,2,1,0]:
	s=''
	for i in arr:
		i=str(i)
		s+=i
	a,b,c,d,e,f,g,=s[1:4],s[2:5],s[3:6],s[4:7],s[5:8],s[6:9],s[7:10]
	a,b,c,d,e,f,g=int(a),int(b),int(c),int(d),int(e),int(f),int(g)
	if a%2==0 and b%3==0 and c%5==0 and d%7==0 and e%11==0 and f%13==0 and g%17==0:
		print(arr)
		list.append(s)
	next_permutation(arr)
sum=0
for num in list:
	num=int(num)
	sum+=num
	
print(list)
print(sum)
