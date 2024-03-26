#Code used to complete Reeborg's World course link below.
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#Turn robot left until it is facing right.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Repeat actions until robot reaches the goal.
while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    if front_is_clear() and wall_on_right():
        move()
    if wall_in_front() and wall_on_right():
        turn_left()
