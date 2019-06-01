def convert3(x):
	x =str(x)
	chars=''
	if len(x)==3:
		x=int(x)
		if x==100:
			chars='onehundred'
			return chars
		elif x==200:
			chars='twohundred'
			return chars
		elif x==300:
			chars='threehundred'
			return chars
		elif x==400:
			chars='fourhundred'
			return chars
		elif x==500:
			chars='fivehundred'
			return chars
		elif x==600:
			chars='sixhundred'
			return chars
		elif x==700:
			chars='sevenhundred'
			return chars
		elif x==800:
			chars='eighthundred'
			return chars
		elif x==900:
			chars='ninehundred'
			return chars
		else:
			x=str(x)
			first=x[0]+'00'
			second=x[1]+x[2]
			second=int(second)
			if second < 10:
				second=str(second)
				chars=convert3(first)+'and'+convert1(second)
			else:
				second=str(second)
				chars=convert3(first)+'and'+convert2(second)
			print(chars)
			return chars

def convert2(x):
	x=str(x)
	chars=""
	if len(x)==2:
		x=int(x)
		if x==10:
			chars="ten"
			return chars
		elif x==20:
			chars='twenty'
			return chars
		elif x==30:
			chars='thirty'
			return chars
		elif x==40:
			chars='forty'
			return chars
		elif x==50:
			chars='fifty'
			return chars
		elif x==60:
			chars='sixty'
			return chars
		elif x==70:
			chars='seventy'
			return chars
		elif x==80:
			chars='eighty'
			return chars
		elif x==90:
			chars='ninety'
			return chars
		elif x==11:
			chars='eleven'
			return chars
		elif x==12:
			chars='twelve'
			return chars
		elif x==13:
			chars='thirteen'
			return chars
		elif x==14:
			chars='fourteen'
			return chars
		elif x==15:
			chars='fifteen'
			return chars
		elif x==16:
			chars='sixteen'
			return chars
		elif x==17:
			chars='seventeen'
			return chars
		elif x==18:
			chars='eighteen'
			return chars
		elif x==19:
			chars='nineteen'
			return chars
		else:
			x = str(x)
			first = x[0]+'0'
			second = x[1]
			chars=convert2(first)+convert1(second)
			return chars
			
			
			

def convert1(x):
	x = str(x)
	chars=""
	if len(x)==1:
		x = int(x)
		if x==1:
			chars="one"
			return chars
		elif x==2:
			chars="two"
			return chars
		elif x==3:
			chars="three"
			return chars
		elif x==4:
			chars="four"
			return chars
		elif x==5:
			chars="five"
			return chars
		elif x==6:
			chars="six"
			return chars
		elif x==7:
			chars="seven"
			return chars
		elif x==8:
			chars="eight"
			return chars
		elif x==9:
			chars="nine"
			return chars

sum=0

for x in range(1,1001):
	numcount=0
	if x < 10:
		chars=convert1(x)
		numcount=len(chars)
		sum=sum+numcount
	elif x < 100:
		chars = convert2(x)
		numcount=len(chars)
		sum=sum+numcount
	elif x < 1000:
		chars=convert3(x)
		numcount=len(chars)
		sum=sum+numcount
	elif x==1000:
		sum=sum+11


print(sum)
	
