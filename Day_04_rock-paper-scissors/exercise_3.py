#List of list representing coordinates.
line_1 = ["❏", "❏", "❏"]
line_2 = ["❏", "❏", "❏"]
line_3 = ["❏", "❏", "❏"]
map = [line_1, line_2, line_3]
poistion = input("Where do you want to put the treasure\n");

#get the letter and convert it into an index
letter = poistion[0].lower()
abc = ["a", "b", "c"]

letter_index = abc.index(letter)
number_index = int(poistion[1]) -1
#place an X in the coordinates that the user picks.
map[number_index][letter_index] = "X"

print(f"{line_1}\n{line_2}\n{line_3}")