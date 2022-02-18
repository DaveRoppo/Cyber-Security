import random 
import time

x = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
xx = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
xxx = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','^','&','*','(',')']

nums = [0,1,2,3,4,5,6,7,8,9]
spec = ['!','@','#','$','%','^','&','*','(',')']


print("Please enter the minimum required length of your password with the number pad and hit enter.")
length = input("> ")
print("Does your password require capital letters? Type y or n and hit enter.")
resp1 = input("> ")
print("Does your password require numbers? Type y or n and hit enter.")
resp2 = input("> ")
print("Does your password require special characters? Type y or n and hit enter.")
resp3 = input("> ")
print("Generating unique password...")
time.sleep(2)

def generate1():
	pw = []
	n = 0
	while  n < int(length):
		y = random.choice(x)
		pw.append(y)
		n = n + 1
		x.remove(y)
	for i in pw:
		print(i)
		
def generate2():
	pw = []
	n = 0
	while  n < int(length):
		y = random.choice(xx)
		pw.append(y)
		n = n + 1
		xx.remove(y)
	pw.append(random.choice(nums))
	for i in pw:
		print(i)
	
def generate3():
	pw = []
	n = 0
	while  n < int(length):
		y = random.choice(xxx)
		pw.append(y)
		n = n + 1
		xxx.remove(y)
	pw.append(random.choice(nums))
	pw.append(random.choice(spec))
	for i in pw:
		print(i)
	
if resp1 and resp2 and resp3 == "y":
	generate3()
elif resp1 and resp2 == "y" and resp3 == "n":
	generate2()
else:
	generate1()

time.sleep(30)
