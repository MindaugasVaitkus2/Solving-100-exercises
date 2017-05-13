# Create an English to Portuguese translation program.

#The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

#d = dict(weather = "clima", earth = "terra", rain = "chuva") 

d = dict(weather = "clima", earth = "terra", rain = "chuva")
# print d.keys()
# print d.values()
# while True:
#     palavra = raw_input('Enter word: ')
#     for key in d:
#         if palavra in key:
#             print d[key]
#             break
#     else:
#         print 'This word does not exist in the dictionary!'
#         break

### or ###

def EngPtDict():
    while True:
        palavra = raw_input('Enter word: ')
        for key in d:
            if palavra in key:
                print d[key]
                break
        else:
            print 'This word does not exist in the dictionary!'
            break
EngPtDict()


# how he did 
# d = dict(weather = "clima", earth = "terra", rain = "chuva")
# def vocabulary(word):
#     return d[word]
 
# word = input("Enter word: ")
# print(vocabulary(word))