#  Create an English to Portuguese translation program.

#The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. In addition, try to return the message "We couldn't find that word!" when the user enters a word that is not in the dictionary.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# def EngPtDict():
#     while True:
#         palavra = raw_input('Enter word: ')
#         for key in d:
#             if palavra in key:
#                 print d[key]
#                 break
#         else:
#             print "We couldn't find that word!"
#             break 
# EngPtDict()


### or ###

def EngPtDict():
    while True:
        palavra = raw_input('Enter word: ')
        try:
            return d[palavra]
        except KeyError:
                print "We couldn't find that word!"
                break

print (EngPtDict())

# how he did
# d = dict(weather = "clima", earth = "terra", rain = "chuva")
# def vocabulary(word):
#     try:
#         return d[word]
#     except KeyError:
#         return "That word does not exist."

# word = input("Enter word: ")
# print(vocabulary(word))
