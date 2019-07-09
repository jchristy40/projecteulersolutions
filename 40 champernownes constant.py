'''
this one is really simple!
first build a string of length one million by concatenating the numbers, starting with 1 and counting up by 1
then create a list of the first, tenth, hundredth ... millionth number
then find the product of these numbers
'''

builder=''
x=1
while len(builder) < 1000000:
	x=str(x)
	builder=builder+x
	x=int(x)
	x+=1

list=[]
list.append(builder[0])
list.append(builder[9])
list.append(builder[99])
list.append(builder[999])
list.append(builder[9999])
list.append(builder[99999])
list.append(builder[999999])
product=1

for i in list:
	i=int(i)
	product*=i

print(product)
