
	
def fact(z):
	prod=1
	while z > 1:
		prod=prod*z
		z=z-1
	return prod
		

for i in range(1000000):
	sum=0
	i=str(i)
	for j in i:
		j=int(j)
		sum=sum+fact(j)
	i=int(i)
	if sum==i:
		print(i)
		


	

