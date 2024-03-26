#input a list of students heights in cm
student_heights = input("Please enter the heights of your students in CM, separated by spaces\n").split()
sum_height = 0

#convert the string into int value and add to sum
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
    sum_height += student_heights[i]

#avgerage the height of the all the students.
average_height = sum_height / len(student_heights)
print(f"The average height of all the students in class is: {average_height:.1f}cm")