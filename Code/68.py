# Create an English to Portuguese translation program.

#The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. In addition, return the message "We couldn't find that word!" when the user enters a word that is not in the dictionary. Also, make the program non case-sensitive meaning that for example, both earth and Earth should return the translation correctly for that word.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

def EngPtDict (palavra):
    try:
        return d[palavra]
    except KeyError:
        return "We couldn't find that word!"

word = raw_input('Enter word: ').lower()
print (EngPtDict(word))