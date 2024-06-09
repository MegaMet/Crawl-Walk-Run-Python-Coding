list_of_strings = input("please enter a list of number separated by ','\n").split(',')
list_of_num = [int(n) for n in list_of_strings]
even_number = [n for n in list_of_num if n%2 == 0]

print(even_number)