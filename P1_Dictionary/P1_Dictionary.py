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



























# O/P
#Enter your word: dark
#Having an absolute or (more often) relative lack of light.
#Marked by difficulty of style or expression.
#Making despondent or depressive.
#Moody and melancholic.
#(For a color) Having a lower brightness.
#**************************************************************
#'Press Enter' to EXIT    or    
#Enter new word:  night
#The period between sunset and sunrise, when a location faces far away from the sun, thus when the sky is dark.
#**************************************************************
#'Press Enter' to EXIT    or    
#Enter new word:  sun
#Any star, especially when seen as the centre of any single solar system.
#The particular star at the centre of our solar system, from which the Earth gets light and heat.
#**************************************************************
#'Press Enter' to EXIT    or    
#Enter new word:  sundr
#Did you mean sundry instead , Enter 'y' for YES and 'n' for NO:  n
#The word dosen't exist. Please recheck it. 
#Enter a word:  sundy
#Did you mean sundry instead , Enter 'y' for YES and 'n' for NO:  n
#The word dosen't exist. Please recheck it. 
#Enter a word:  sunday
#The seventh day of the week in Europe and in systems using the ISO 8601 standard, or the first day of the week in the United States of America, the Sabbath for most Christians.
#**************************************************************
#'Press Enter' to EXIT    or    
#Enter new word:  ADDRT
#Did you mean art instead , Enter 'y' for YES and 'n' for NO:  y
#The creation of works of beauty or other special significance.
#The products of human creativity; works of art collectively.
#A superior skill that one can learn by study, practice, and observation.
#Photographs or other visual representations in a printed publication.
#**************************************************************
#'Press Enter' to EXIT    or    
#Enter new word:  USA
#A country and federal republic in North America located north of Mexico and south of Canada, including Alaska, Hawaii and overseas territories.
#**************************************************************
#'Press Enter' to EXIT    or    
#Enter new word:  Delhi
#The largest metropolis by area and the second-largest metropolis by population in India.
#**************************************************************
#'Press Enter' to EXIT    or    
#Enter new word: adssdsdas
#The word dosen't exist. Please check it
