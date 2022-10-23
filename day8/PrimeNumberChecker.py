
def prime_checker(number):
	a=0
	for i in range(1,number+1):
		
		if((number%i != 0)):
			pass
			#print("failes")
			
		else:
			a+=1

	#print(a)
	if(a==2):
		print(f"{number} is a prime number")
	else:
		print(f"{number} is not a prime number")

n = int(input("Check this number: "))
prime_checker(n)



