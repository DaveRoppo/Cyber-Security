import time
#Define function for encryption
def encrypt(text):
    result = ""
    # Go through each character of the text in this for loop
    for i in range(len(text)):
        # Obtain the ASCII value
        char_pos = ord(text[i])
        # Substract 97 to have a character from 1 to 26
        char_pos = char_pos - 97
        new_pos = char_pos + key 
        # Make sure that the position does not surpass 26(wrap around)
        new_pos = new_pos % 26
        # Convert back to ASCII
        new_pos = new_pos + 97
        # Convert ASCII to character and concatenate it to result
        result = result + chr(new_pos)
        time.sleep(.5)
        print(result)
    return result
#Define funciton for decryption 
def decrypt(cipher_text):
    result = ""
    # Go through each character of the text in this for loop
    for i in range(len(cipher_text)):
        # Obtain the ASCII value
        char_pos = ord(cipher_text[i])
        # Substract 97 to have a character from 1 to 26
        char_pos = char_pos - 97
        new_pos = char_pos - key
        # Make sure that the position does not surpass 26 (wrap around)
        new_pos = new_pos % 26
        # Convert back to ASCII
        new_pos = new_pos + 97
        # Convert ASCII to character and concatenate it to result
        result = result + chr(new_pos)
        time.sleep(.5)
        print(result)
    return result
#Ask user what to encrypt
text = (input("Enter the word you would like to encrypt:"))
#Ask user for key (which position)
key = int(input("Choose a key 1-26:"))
time.sleep(.5)
print(f"Plain Text: {text}")
cipher_text = encrypt(text)
print(f"Encrypted: {cipher_text}")
print(f"Decrypted: {decrypt(cipher_text)}")
time.sleep(5)
