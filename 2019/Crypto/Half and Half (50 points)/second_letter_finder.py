# Example:
# ciphertext is = \x15\x02\x07\x12\x1e\x100\x01\t\n\x01"
# we know these:    a   c   t    f  {    ..  .  . .  . .
# unkown_letters:   .   .   .    .  .    ..  .  . .  . }

# So here we know 'a' and the result which is in hex x15 
# We will see that the a has to be xored with t to get 0x15 so put it in it's possition.

# !!! Cearful because ciphertext has at the end this character " !!! This is NOT hex,so you have to convert it !!! " in hex is 22 so at known_hex_result put x22

# ciphertext is = \x15\x02\x07\x12\x1e\x100\x01\t\n\x01"
# we know these:    a   c   t    f  {    ..  .  . .  . _
# unkown_letters:   t   a   s    t  e    ..  .  . .  . }

# And so on...


known_letter_1 = 'j'
known_hex_result = "x35".replace('x0','x') # We need to remove the first zero after x. So for example 0x02 --> 0x2 . This is for the if result problem
known_hex_result = ''.join(('0',known_hex_result)) # add zero at the beginning x15 --> 0x15


unknown_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '`', '~', '/', ',', '.', '<', '>', '?', '[', ']', ':', "'", '"', '{', '\\', '}']

for letter_2 in unknown_letter:

	binary1 = ' '.join(format(ord(known_letter_1), 'b') for x in known_letter_1)
	binary2 = ' '.join(format(ord(letter_2), 'b') for x in letter_2)

	length = len(binary1)


	binary1 = list(binary1)
	binary2 = list(binary2)

	xor_result = ''

	try:
		for i in range(0,7):
			if (binary1[i] == '1') and (binary2[i] == '1'):
				xor_result += '0'
			elif (binary1[i] == '0') and (binary2[i] == '1'):
				xor_result += '1'
			elif (binary1[i] == '1') and (binary2[i] == '0'):
				xor_result += '1'
			elif (binary1[i] == '0') and (binary2[i] == '0'):
				xor_result += '0'



		if hex(int(xor_result, 2)) == known_hex_result: # Put here the hex known number!!!
			print("The other half text is:",letter_2)
		#print(known_letter_1,"^",letter_2,"=",hex(int(xor_result, 2))) # this will show all results
	except:
		pass

############### Useful sources for this script ###############
# https://github.com/quintuplecs/angstromctf2019/blob/master/crypto/Half-and-Half.md
