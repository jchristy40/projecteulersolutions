y = 0
for x in range(1000):
	if x % 15 == 0:
		print('fitzlebusze')
		y = y + x
	elif x % 3 == 0:
		print('fitz')
		y = y + x
	elif x % 5 == 0:
		print('butzsle')
		y = y + x
	else:
		print(x)
		
print('the sum of all fizzes and buzzes is: ',y)
print('thats all dude')
