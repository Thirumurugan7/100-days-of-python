alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
ciphered_text = ""


def encrypt(text, shift):
    text1 = []
    cipher_text = ""
    for i in text:
        #print(i)
        text1 += i

    #print(text1)
    for i in text1:
        #print(i)
        search_index = alphabet.index(i)

        #print(search_index)
        if (search_index + shift >= 26):
            search_index_value = (search_index + shift) - 26
            #print(search_index_value)
        else:
            search_index_value = search_index + shift
        cipher_value = alphabet[search_index_value]
        cipher_text += cipher_value
        ciphered_text = cipher_text
    print(f"Decoded text: {cipher_text}")
    
    #print(ciphered_text)


if(direction == "encode"):
	encrypt(text, shift)






def dcrypt(text, shift):
   
    deciphered_text = ""
    for i in text:
        search_index = alphabet.index(i)

        decipher_value = alphabet[search_index - shift]
        deciphered_text += decipher_value
    print(f"Encoded Text: {deciphered_text}")


if(direction == "decode"):
	dcrypt(text, shift)