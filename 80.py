#Create a script that lets the user create a password until they have satisfied three conditions:
#Password contains at least one number, one uppercase letter and it is at least 5 chars long
#Give the exact reason why the user has not created a correct password

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
        password = raw_input('Please enter password: ')
        CheckLen(password)
        FindNumber(password)
        CheckUpper(password)
        if LenRes and NumRes and UppRes is True:
            print 'Password succesfully created!'
            break
        else:
            print ('Please try again.')

PasswordChecker()

# his answer
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