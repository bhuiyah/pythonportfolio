# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

play = 1
alpha = pandas.read_csv("nato_phonetic_alphabet.csv")
    
while play:
    alphabet = {word.letter:word.code for (idx, word) in alpha.iterrows()}
    word = list(input("Enter a word: ").upper())
    try:
        codes = [alphabet[w] for w in word]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
    else:
        play = 0
    

print(codes)