# Give a greeeting to introduce the program.
print("Welcome to the tip calculator.")
# Have the user input the bill amount and store it in a variable.
bill = int(input("What was the total bill? "))
# Have the user input the percentage that they would like to tip and store it in a variable.
percent = int(input("What percentage tip would you like to give? I.E. 10, 12, 15? "))
# Have the user input the number of people that are splitting the bill and store it in a variable.
people_num = int(input("How many people to split the bill? "))
# Calculate the total bill with tip.
bill_with_tip = bill * (1 + (percent / 100))
# Calulate the value that each person would have to pay and round to the second decimal.
amount_to_pay = round(bill_with_tip / people_num, 2)
# Give the final amount that each person will be pay.
print(f"Each person should pay: ${amount_to_pay:.2f}")