#Create a program that asks the user to submit text repeatedly
#The program saves the changes when the user submits SAVE, but does't close
#The program saves the changes and closes when the user submits CLOSE

with open('../inputs&outputs/usr_data_Ex97.txt', 'a+') as file:
    while True:
        usr_inp = raw_input('Please enter text: ')
        if usr_inp == 'CLOSE':
            file.close()
            break
        if usr_inp == 'SAVE':
            file.close()
            usr_inp = usr_inp.split()
            for i in usr_inp[:-1]:
                file.write(i+'\n')
                
        else:
            usr_inp = usr_inp.split()
            for i in usr_inp:
                file.write(i+'\n')


# how he did inputs
# file = open("user_data_save_close.txt", 'a+')

# while True:
#     line = input("Write a value: ")
#     if line == "SAVE":
#         file.close()
#         file = open("user_data_save_close.txt", 'a+')
#     elif line == "CLOSE":
#         file.close()
#         break
#     else:
#         file.write(line + "\n")