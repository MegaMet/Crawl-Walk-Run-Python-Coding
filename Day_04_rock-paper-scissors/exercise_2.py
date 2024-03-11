import  random

#list of names
names = ["Angela", "Ben", "Jenny", "Michael", "Clow"]

#get the length of the list
num_items = len(names)

#randomly generate a number between 0 and the number of names in the list.
random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]
print(f"{person_who_will_pay} is going to buy the meal today")