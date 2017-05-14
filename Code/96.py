#Create a program that asks the user to submit text repeatedly
#The program closes when the user submits CLOSE

with open('../inputs&outputs/usr_data_Ex96.txt', 'a+') as file:
    while True:
        usr_inp = raw_input('Please enter text: ')
        if usr_inp == 'CLOSE':
            file.close()
            break
        else:
            usr_inp = usr_inp.split()
            for i in usr_inp:
                file.write(i+'\n')

