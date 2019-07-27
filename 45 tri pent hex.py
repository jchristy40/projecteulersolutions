'''
this one is fairly straightforward.
we are looking for triangular numbers that are also pentagonal and hexagonal.
so we want to generate a dictionary for hex and pent numbers - for fast lookup
and a list of triangular numbers.
then we check our triangular numbers and just print the ones that are in both dictionaries

##tri = x*(x+1)/2
##pent = x*(3*x-1)/2
##hex = x*(2*x-1)

some improvements could be made. we could reduce the solution space; we could test that our math equations are actually working since we are putting a lot of faith in correct calculations; we could put our number generators in functions so that they could be reused
'''

pentd={}

for x in range(1,500000):
	pent=0
	pent=x*(3*x-1)/2
	pentd[pent]=x
	
	
trilist=[]

for y in range(1,500000):
	tri=0
	tri=y*(y+1)/2
	trilist.append(tri)

hexd={}
for z in range(1,500000):
	hex=0
	hex=z*(2*z-1)
	hexd[hex]=z


for i in trilist:
	if i in hexd and i in pentd:
		print(i)


