import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
it=type(2)
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    
    # if((char == " ")):
    #     print(char)
    #     end_text+=char
    #     continue
    if(char not in alphabet):
        end_text+=char
    else:
		
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")
  response=input("Do you want to continues then type yes if not then no \n").lower()
  if(response=="no"):
	  
    return "False"

# Import and print the logo from art.py when the program starts.
print(art.logo)
#  figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
cond="True"
while(cond=="True"):
	
	direction = input("Type 'encode' to encrypt, type 'decode' to 	decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	
	#What if the user enters a shift that is greater than the number of letters in the alphabet?
	shift1=0
	while(shift>26):
		shift=shift-26
	#Try running the program and entering a shift number of 45.
	#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
	
	ponse=caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
	if(ponse=="False"):
		print("bye")
		break

