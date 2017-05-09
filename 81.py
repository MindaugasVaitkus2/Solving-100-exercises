# Create a script that lets the user submit a password until they have satisfied 3 conditions:
#1. Password contains ate least one number
#2. Contains one uppercase letter
#3. It is at least 5 char long
# Give the exact reason why the user has not created a correct password
# Before asking for password, ask for username

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

def CreateUsername():
    while True:
        user_name = raw_input('Please enter username: ')
        fhand = open('./user_data_commas.txt')
        inp = fhand.read().split()
        if user_name in inp:
            print ('Username already exists. Please try again')
            continue
        else:
            print ('Username created.')
            break
    return user_name       


def PasswordChecker():
    while True:
        
        password = raw_input('Please enter password: ')
        CheckLen(password)
        FindNumber(password)
        CheckUpper(password)
        if LenRes and NumRes and UppRes is True:
            print 'Password succesfully created!'
            break
        else:
            print ('Please try again.')

CreateUsername()
PasswordChecker()

# how he did
# while True:
#     usr = input("Enter username: ")
#     with open("users.txt", "r") as file:
#         users = file.readlines()
#         users = [i.strip("\n") for i in users]
#     if usr in users:
#         print("Username exists")
#         continue
#     else:
#         print("Username is fine")
#         break

# while True:
#     notes = []
#     psw = input("Enter password: ")
#     if not any(i.isdigit() for i in psw):
#         notes.append("You need at least one number")
#     if not any(i.isupper() for i in psw):
#         notes.append("You need at least one uppercase letter")
#     if len(psw) < 5:
#         notes.append("You need at least 5 characters")
#     if len(notes) == 0:
#         print("Password is fine")
#         break
#     else:
#         print("Please check the following: ")
#         for note in notes:
#             print(note)
