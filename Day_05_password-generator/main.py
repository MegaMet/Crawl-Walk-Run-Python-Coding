#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Select the requested amount of charaters from each list
list_of_letters = ""
for i in range(1, nr_letters + 1):
    list_of_letters += letters[random.randint(0, len(letters) - 1)]

list_of_symbols = ""
for i in range(1, nr_symbols + 1):
    list_of_symbols += symbols[random.randint(0, len(symbols) - 1)]

list_of_numbers = ""
for i in range(1, nr_numbers + 1):
    list_of_numbers += numbers[random.randint(0, len(numbers) - 1)]

#combine the 3 list of strings into 1 string.
combined = list_of_letters + list_of_symbols + list_of_numbers

#randomize the characters in 'combined and output the resutl'
randomized_combined = "".join(random.sample(combined,len(combined)))
print(f"Your new password is: {randomized_combined}")