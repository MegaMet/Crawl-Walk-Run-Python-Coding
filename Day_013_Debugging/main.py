############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 21): #The end of the range is 20 so the look never gets to 20; end of the range should be at least 21
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) #The the start of the range is 1 and the end fo the range is up to 6; so "❶" is never selected a index 0 and 6 is beyond the length of dice_imgs
print(dice_imgs[6])

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994: #Nothing happens if you put in 1994 becaause "1994" is not included in the range
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# Fix the Errors
age = input("How old are you?")
if age > 18:
    print(f"You can drive at age {age}.") #The 'f' is missing ahead of the f-string and this line is missing an indent, so it will not execute.

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) #'==' incorrectly used to assign value from input and leaving 'words_per_pages' as 0
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) #This line has not been indented to append the 'new_item' to the new list
  print(b_list)

mutate([1,2,3,5,8,13])