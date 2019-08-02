'''
takes input and determines if two strings are permutations of one another
from cracking the coding interview
some minir modifications could be done to check strings in a file, or so on
'''

def checkperm(a,b):
	
	
	if type(a) is not str or type(b) is not str:
		return 'wrong types'
	if len(a) != len(b):
		return False
	
	a=sorted(a)
	b=sorted(b)
	if a==b:
		return True
	else:
		return False

print(checkperm(input('first str? '),input('second str? ')))
	

