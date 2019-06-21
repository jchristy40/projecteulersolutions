##we are building strings and enforcing the pandigital idea as we go
##once we find the pandigital numbers, we manipulate the strings and find the sum of pandigital numbers

list=[]
a=''
b=''
c=''
final=[]
for x in range(1,10000):
	for y in range(1,1000):
		a=str(x)
		list=[]
		boot=''
		b=str(y)
		z=0
		for d in a:
			if d=='0':
				list=[]
				break
			if d in list:
				list=[]
				break
			if d not in list:
				list.append(d)
		for e in b:
			if e=='0':
				list=[]
				break
			if e in list:
				list=[]
				break
			if e not in list:
				list.append(e)
		z=x*y
		c=str(z)
		if len(list)>5:
			break
		if len(c)==4 or len(c)==5:
			for f in c:
				if f=='0':
					list=[]
					break
				if f in list:
					list=[]
					break
				if f not in list:
					list.append(f)
		if len(list)==9:
			print(list)
			for i in list:
				boot=boot+i
			final.append(boot)
			
penultimate=[]
for g in final:
	g=g[5:9]
	penultimate.append(g)

print(penultimate)

ultimate=[]
for h in penultimate:
	if h not in ultimate:
		ultimate.append(h)

print(ultimate)

sum=0
for nums in ultimate:
	nums=int(nums)
	sum+=nums

print(sum)

			


