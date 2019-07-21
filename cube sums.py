'''a**3 + b**3 =c**3 + d**3
find all integer solutions below 1000
this problem is from cracking the coding interview
this was a tough one - the problem if brute forced is O (n**4)
to get it faster, we need to store all the sums of two cubed numbers in a dictionary.
this dictionary maps cube sums to pairs of numbers
if two or more pairs of numbers share a cube sum, the dictionary maps the pairs to a list.
thus we can see which pairs of numbers map to cube sums
i commented out multiple failed attempts at accomplishing this

'''

from collections import defaultdict


stored=()
list=[]
var=0
dict={}


for a in range(1,1000):
	for b in range((a+1),1000):
		stored=(a**3)+(b**3)
		vals=(a,b)
		##map pairs to list -
		dict.setdefault(stored, []).append(vals)

print('stage 1 done')


for k,v in dict.items():
	if len(dict[k])>1:
		print(k,v)


'''
newl=[]
for k,v in dict.items():
	for k1,v1 in dict.items():
		if v==v1 and k!=k1:
			newl.append((k,k1))

print(newl)
'''
'''
for key, val in dict.items():
	for key1, val1 in dict.items():
		if val in dict.items():
			print('hey')
'''

'''complete=[]
var=0
dict={}
for x in list:
	dict[(x[0],x[1])]=x[2]

print(dict)
	'''
'''
for i in list:
	for j in list:
		if i[2]==j[2] and i!=j and i[0]!=j[1]:
			complete.append((i[0],i[1],j[0],j[1]))



final=[]

for a in complete:
	if a[1] > a[0] and a[3] >a[2]:
		final.append(a)

print(final)


'''
'''dict={}
cube=0
for x in range(100):
	cube=x**3
	dict[x]=cube





sums=[]
first=0
second=0

for i in range(100):
	first=dict[i]
	for j in range(100):
		second=dict[j]
		sums.append(first+second)

print(sums)'''
