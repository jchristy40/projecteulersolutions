x = 2**1000
splitsum = str(x)
print(splitsum)


list = []
sum = 0
for anum in splitsum:
	char = int(anum)
	sum = sum + char

print(sum)
