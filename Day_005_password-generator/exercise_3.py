#get the user's target number to calculate.
target = int(input("Please enter a number between 0 and 1000: "))
sum_of_target = 0

#loop until user requested number and add the sum of all even numbers.
for i in range(1, target + 1):
    if i % 2 == 0:
        sum_of_target += i

#print value:
print(f"The sum of all the even number up to {target} is: {sum_of_target}")