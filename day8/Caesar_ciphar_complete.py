alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(plain_text, shift_amount,direction):
	caeser_text=""
	for letter in plain_text:
		
		position = alphabet.index(letter)
		if(direction == "encode"):
			new_position = position + shift_amount
		elif(direction=="decode"):
			new_position = position - shift_amount
		caeser_text += alphabet[new_position]
	if(direction=="encode"):
		print(f"The encoded text is {caeser_text}")
	elif(direction=="decode"):
		print(f"The decoded text is {caeser_text}")
	



caesar(text,shift,direction)