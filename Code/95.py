#Create a program that asks the user to input values separated by commas and those values will be stored in a separate line each in a text file

inp = raw_input('Please input values separated by commas: ')
usr_inp = inp.split()
with open('../inputs&outputs/data_comma_Ex95.txt', 'w+') as file:
    for i in usr_inp:
        file.write(i+'\n')

# his answer:
# line = input("Enter values: ")
# line_list = line.split(",")
# with open("user_data_commas.txt", "a+") as file:
#     for i in line_list:
#         file.write(i + "\n")