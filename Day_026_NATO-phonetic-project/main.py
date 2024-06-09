#TODO 1. Create a dictionary in the forllow format:
#{"A" : "Alpha", "B" : "Bravo"}
#TODO 2. Create a list of phonetic code words from a word that the user inputs:
#{"Cat" = "Charlie","Alfa", "Tango"}

DATA_PATH = "nato_phonetic_alphabet.csv"

import pandas

nato_phonetic_alphabet_data = pandas.read_csv(DATA_PATH)
nato_phonetic_alphabet_dic = {row.letter : row.code for (index, row) in nato_phonetic_alphabet_data.iterrows()}

# for (index, row) in nato_phonetic_alphabet_data.iterrows():
#     nato_phonetic_alphabet_dic[row.letter] = row.code

word = input("Enter a word: ").upper()
word_list = [nato_phonetic_alphabet_dic[l] for l in word]

print(word_list)
