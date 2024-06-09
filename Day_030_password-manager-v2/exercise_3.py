#expansion of Day 26 NATO-phonetic-project
DATA_PATH = "nato_phonetic_alphabet.csv"

import pandas

nato_phonetic_alphabet_data = pandas.read_csv(DATA_PATH)
nato_phonetic_alphabet_dic = {row.letter : row.code for (index, row) in nato_phonetic_alphabet_data.iterrows()}

# for (index, row) in nato_phonetic_alphabet_data.iterrows():
#     nato_phonetic_alphabet_dic[row.letter] = row.code
def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        word_list = [nato_phonetic_alphabet_dic[l] for l in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(word_list)

generate_phonetic()