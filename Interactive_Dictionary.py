# Dictionary
# 1. Finds meaning of word
# 2. Suggests similar words if mis-spelt
# 3. After giving output meaning enter new word


import json
from difflib import get_close_matches

data = json.load(open("D:\San\data.json" , "r"))

def translate(w):
    w = w.lower()                       # Converts input word to lower case
    if w in data:
        return data[w]
    elif w.title() in data:             # Converts first letter of input word to Uppercase eg. goa to Goa
        return data[w.title()]
    elif w.upper() in data:             # In case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead , Enter 'y' for YES and 'n' for NO:  " % get_close_matches(w, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            word = input("The word dosen\'t exist. Please recheck it. \nEnter a word:  ")
            return translate(word)
        else:
            print( "Wrong Entry. Should press 'y' or 'n'. Re-enter the Word:  ")
            word = input("Enter your word:  ")
            return translate(word)
    else:
        return "The word dosen\'t exist. Please check it"

word = input("Enter your word:  ")

output = translate(word)
while type(output) == list:
    if type(output) == list:
        for item in output:
            print(item)
        print("**************************************************************")
        new_word = input("'Press Enter' to EXIT    or    \nEnter new word:  ")
        output = translate(new_word)
    else:
        print(output)

print(output)


    
