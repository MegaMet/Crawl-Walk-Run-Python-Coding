sentence = input("Please type out a sentence\n")
list_of_words = sentence.split()

number_of_letters = {word:len(word) for word in list_of_words}
print(number_of_letters)