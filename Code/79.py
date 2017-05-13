#Create a script that lets the user submit a password until they have satisfied three conditions:
#1. Password contains at least one number
#2. Contains one uppercase letter
#3. It is at least 5 chars long
#Print out message "Passowrd is not fine" if the user didn't create a correct password


# def CheckLen (password):
#     if len(password) >= 5:
# 		global LenRes
# 		LenRes = True
# 		print ('Password length is good.')
# 		return (LenRes)
#     else:
# 		LenRes = False
# 		print ('Password is too short.')
# 		return (LenRes)
#
# def FindNumber(password):
#     if any (char.isdigit() for char in password):
# 		global NumRes
# 		NumRes = True
# 		print ('Password has at least one digit.')
# 		return (NumRes)
#     else:
# 		NumRes = False
# 		print ('Password must have at least one digit.')
# 		return (NumRes)
#
# def CheckUpper(password):
# 	if any (char.isupper() for char in password):
# 		global UppRes
# 		UppRes = True
# 		print ('Password has at least one uppercase letter.')
# 		return (UppRes)
# 	else:
# 		UppRes = False
# 		print ('Password must have at least one uppercase letter.')
# 		return (UppRes)
#
#
# def PasswordChecker():
# 	while True:
# 		password = raw_input('Please enter password: ')
# 		CheckLen(password)
# 		FindNumber(password)
# 		CheckUpper(password)
# 		if LenRes and NumRes and UppRes is True:
# 			print 'Password succesfully created!'
# 			break
# 		else:
# 			print ('Please try again.')
#
# PasswordChecker()

# or

import getpass

def CheckLen (password):
    if len(password) >= 5:
		global LenRes
		LenRes = True
		print ('Password length is good.')
		return (LenRes)
    else:
		LenRes = False
		print ('Password is too short.')
		return (LenRes)

def FindNumber(password):
    if any (char.isdigit() for char in password):
		global NumRes
		NumRes = True
		print ('Password has at least one digit.')
		return (NumRes)
    else:
		NumRes = False
		print ('Password must have at least one digit.')
		return (NumRes)

def CheckUpper(password):
	if any (char.isupper() for char in password):
		global UppRes
		UppRes = True
		print ('Password has at least one uppercase letter.')
		return (UppRes)
	else:
		UppRes = False
		print ('Password must have at least one uppercase letter.')
		return (UppRes)


def PasswordChecker():
	while True:
		password = getpass.getpass('Please enter password: ')
		CheckLen(password)
		FindNumber(password)
		CheckUpper(password)
		if LenRes and NumRes and UppRes is True:
			print 'Password succesfully created!'
			break
		else:
			print ('Please try again.')

PasswordChecker()


#how he did it:
# while True:
#     psw = raw_input("Enter new password: ")
#     if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
#         print("Password is fine")
#         break
#     else:
#         print("Passowrd is not fine")
