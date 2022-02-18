#My Take on the Vigenere Cypher
#Add Encrypt vs decrypt option
#Add User Keyword choice
#5 subkeys = 5 letter keyword
#Add key number to origanl message number to get encrypted number 
#Convert encyphered numbers to alphabet to get encrypted message
#Add Dictionary with key

key = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19,
       "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

key2 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: 'm', 14: 'n', 15: 'o', 16: 'p',
17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: 'a', 28: 'b', 29: 'c', 30: 'd', 31: 'e', 32: 'f', 
33: 'g', 34: 'h', 35: 'i', 36: 'j', 37: 'k', 38: 'l', 39: 'm', 40: 'n', 41: 'o', 42: 'p', 43: 'q', 44: 'r', 45: 's', 46: 't', 47: 'u', 48: 'v', 
49: 'w', 50: 'x', 51: 'y', 52: "z"}

dkey1 = {"a": 27, "b": 28, "c": 29, "d": 30, "e": 31, "f": 32, "g": 33, "h": 34, "i": 35, "j": 36, "k": 37, "l": 38, "m": 39, "n": 40, "o": 41, "p": 42, "q": 43, "r": 44, "s": 45,
       "t": 46, "u": 47, "v": 48, "w": 49, "x": 50, "y": 51, "z": 52}


encryptword = []
encryptpass = []
encryption = []
decryptword = []
decryptpass = []
decryption = []
import time

def start():
	print("Would you like to encrypt or decrypt?")
	choice = input("> ")
	if choice == "encrypt":
		encrypt()
	elif choice == "decrypt":
		decrypt()
	else:
		print("Please type either 'encrypt' or 'decrypt'")
		start()
		
def encrypt():		
	print("\nEnter the word you would like to encrypt..")
	word = input("> ")
	time.sleep(.5)
	print("\nChoose a keyword..")
	passphrase = input("> ")
	if len(passphrase) < len(word):
		print("\nERROR: Please choose a keyword that is longer than the word you wish to encrypt.")
		passphrase = input("> ")
	time.sleep(.5)

	for letter in word:
		if letter in key:
			encryptword.append((key[letter]))

	for letter in passphrase:
		if letter in key:
			encryptpass.append((key[letter]))
			if len(encryptpass) == len(encryptword):
				break

	try:
		if encryptword[0]:
			encryption.append(int(encryptword[0]) + int(encryptpass[0]))
		if encryptword[1]:
			encryption.append(int(encryptword[1]) + int(encryptpass[1]))
		if encryptword[2]:
			encryption.append(int(encryptword[2]) + int(encryptpass[2]))
		if encryptword[3]:
			encryption.append(int(encryptword[3]) + int(encryptpass[3]))
		if encryptword[4]:
			encryption.append(int(encryptword[4]) + int(encryptpass[4]))
		if encryptword[5]:
			encryption.append(int(encryptword[5]) + int(encryptpass[5]))
		if encryptword[6]:
			encryption.append(int(encryptword[6]) + int(encryptpass[6]))
		if encryptword[7]:
			encryption.append(int(encryptword[7]) + int(encryptpass[7]))
		if encryptword[8]:
			encryption.append(int(encryptword[8]) + int(encryptpass[8]))
		if encryptword[9]:
			encryption.append(int(encryptword[9]) + int(encryptpass[9]))
		if encryptword[10]:
			encryption.append(int(encryptword[10]) + int(encryptpass[10]))
	except IndexError:
		pass
	
	print("\n encrypting..\n")
	time.sleep(2)
	for num in encryption:
		if num in key2:
			print((key2[num]))
			time.sleep(.5)
			
	print("\n")		


def decrypt():
	print("\nWhat would you like to decrypt?")
	word = input(" >")
	time.sleep(1)

	print("\nWhat is the keyword?")
	passphrase = input("> ")
	time.sleep(1)

	for letter in word:
		if letter in dkey1:
			decryptword.append((dkey1[letter]))
		
	
	for letter in passphrase:
		if letter in key:
			decryptpass.append((key[letter]))
			if len(decryptpass) == len(decryptword):
				break

	try:
		if decryptword[0]:
			decryption.append(int(decryptword[0]) - int(decryptpass[0]))
		if decryptword[1]:
			decryption.append(int(decryptword[1]) - int(decryptpass[1]))
		if decryptword[2]:
			decryption.append(int(decryptword[2]) - int(decryptpass[2]))
		if decryptword[3]:
			decryption.append(int(decryptword[3]) - int(decryptpass[3]))
		if decryptword[4]:
			decryption.append(int(decryptword[4]) - int(decryptpass[4]))
		if decryptword[5]:
			decryption.append(int(decryptword[5]) - int(decryptpass[5]))
		if decryptword[6]:
			decryption.append(int(decryptword[6]) - int(decryptpass[6]))
		if decryptword[7]:
			decryption.append(int(decryptword[7]) - int(decryptpass[7]))
		if decryptword[8]:
			decryption.append(int(decryptword[8]) - int(decryptpass[8]))
		if decryptword[9]:
			decryption.append(int(decryptword[9]) - int(decryptpass[9]))
		if decryptword[10]:
			decryption.append(int(decryptword[10]) - int(decryptpass[10]))
	except IndexError:
		pass
	
	print("\nDecrypting...\n")
	time.sleep(1)

	for num in decryption:
		if num in key2:
			print((key2[num]))
			time.sleep(.5)
	print("\n")		
	start()

start()
