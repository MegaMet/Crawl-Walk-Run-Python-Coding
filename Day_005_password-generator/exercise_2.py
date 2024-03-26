#input a list of students scores
student_scores = input("Please enter the scores of your students, separated by spaces\n").split()
highest_score = 0

#convert the string into int value and compare the value to highest
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
    if (student_scores[i] > highest_score):
        highest_score = student_scores[i]

#output the highest score.
print(f"The highest score of your students is: {highest_score}")