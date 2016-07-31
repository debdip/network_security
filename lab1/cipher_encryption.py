#!/usr/bin/env python
#simple cipher encryption program only consider upper case
def cipher_encryption(alpha,key):
	cipher=''
	for i in range(len(alpha)):
		old_char=(ord(alpha[i])-65+key)%26 # convert char to ascii, add the key 
		cipher+=chr(old_char+65)		# convert to char
	print(cipher)	 

plain_txt=raw_input('Enter Plain text to encode ') #input from terminal
key=int(raw_input('Enter key ')) 
cipher_encryption(plain_txt,key) 
