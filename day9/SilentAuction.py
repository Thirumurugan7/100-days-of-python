from replit import clear
# call clear() to clear the output in the console.
from art import logo
print(logo)
cond="True"
bidders={}
while(cond=="True"):
	name=input("Enter your name: ")
	bid_amount=int(input("Enter your bid: $"))
	bidders[name]=bid_amount
	another_bidder=input("Do we have another bidder:yes or no \n").lower()
	if(another_bidder=="yes"):
		clear()
		
	elif(another_bidder=="no"):
		clear()
		cond="False"
values=[]
for key in bidders:
	values.append(bidders[key])
max_value=max(values)
winner=""
for key in bidders:
	if(bidders[key]==max_value):
		winner=key


	
print(f"Winner is {winner}")