import art
def add(n1,n2):
	return n1+n2
def sub(n1,n2):
	return n1-n2
def mul(n1,n2):
	return n1*n2
def div(n1,n2):
	return n1/n2
operation = {
	"+":add,
	"-":sub,
	"*":mul,
	"/":div
}
print(art.logo)
def calculator():
	n1=float(input("Enter first number: "))
	cond="True"
	while(cond=="True"):
		for key in operation:
			print(key)
		
		operation_selected=input("select one operation from above: ")
		n2=float(input("Enter Second number: "))
		calculation_selection=operation[operation_selected]
		calculation=calculation_selection(n1,n2)
		print(f"result is: {calculation}")
		res=input("Do you want to continue: yes or no \n").lower()
		if(res=="yes"):
			n1=calculation
			
		elif(res=="no"):
			print("bye")
			calculator()
		elif(res=="exit"):
			break
calculator()