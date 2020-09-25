import random

file = open('passwordAndUse.txt', 'a')


chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@'


numOfPassword = int(input("How many passwords do you want to generate? "))




if numOfPassword == 1:
	passwordUse = raw_input("\nWhat is this password going to be used for? ")
	lengthOfPassword = int(input("\nWhat do you want the length of your password to be? "))
	for num in range(numOfPassword):
		password = ''
	for p in range(lengthOfPassword):
		password += random.choice(chars)

	num += 1
	print("\nPassword " + str(num) + " -- " + password)
	file.write("\n" + str(password) + " is used for " + str(passwordUse))
	quit()






lengthOfPassword = int(input("\nWhat do you want the length of your password to be? "))


for num in range(numOfPassword):
	password = ''
	for p in range(lengthOfPassword):
		password += random.choice(chars)

	num += 1
	print("\nPassword " + str(num) + " -- " + password)	


