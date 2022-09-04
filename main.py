"""
u.s. states game
"""

# import modules
from turtle import Screen, Turtle

import pandas

# set up screen
turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "C:/Users/tavish/Desktop/snek/Pandas & csv/states_game/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# create data variable by reading csv
data = pandas.read_csv(
    "C:/Users/tavish/Desktop/snek/Pandas & csv/states_game/us-states-game-start/50_states.csv"
)
# cast state column to a list
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    # user input
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

    # end the game
    if answer_state == "Exit":
        # use conditional list comprension to add missed states to list
        missing_states = [state for state in all_states if state not in guessed_states]
        # create file of states missed
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # since all_states is list, can check for membership using 'in'
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        # pull out the row where input is equal to state
        state_data = data[data.state == answer_state]
        # since this is a row, can tap into attributes using
        # names of columns, must convert str to int
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
