DATA_PATH = "CSVs/50_states.csv"

import  turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(DATA_PATH)
list_of_states = data["state"].to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What is the name of a state").title();

    if answer_state == "Exit":
        missing_states = [s for s in list_of_states if s not in guessed_states]

        # missing_states = []
        # for s in list_of_states:
        #     if s not in guessed_states:
        #         missing_states.append(s)

        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("CSVs/States_To_Learn.csv")
        break
    if answer_state in list_of_states:
        state_data = data[data["state"] == answer_state]
        state_name = state_data["state"].item()
        if state_name not in guessed_states:
            guessed_states.append(state_name)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.setposition(int(state_data["x"]), int(state_data["y"]))
        t.write(state_name)

