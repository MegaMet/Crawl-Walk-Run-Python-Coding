#function that calculates how many cans of paint is needed to paint a wall.
import math

test_h = int(input("What is the height (m) that you are painting?: ")) #Height of the wall (m)
test_w = int(input("What is the width (m) that you are painting?: ")) #width of the wall (m)
coverage = 5

#calculation
def paint_calc(height, width, coverage):
    num_of_cans = int(math.ceil((height * width) / coverage))
    print(f"You'll need {num_of_cans} cans of paint.")

paint_calc(height=test_h, width=test_w, coverage=coverage)

