import turtle
from turtle import *
import pandas as pd
image = "blank_states_img.gif"
screen=Screen()
screen.addshape(image)
turtle.shape(image)
guessed_state=[]
c = pd.read_csv("./50_states.csv")
l = c["state"].to_list()
while len(guessed_state)<len(l):
    answer_state = screen.textinput(title="Guess the place", prompt="what's another state name?").title()
    if answer_state == "Exit":
        missing_state = [state for state in l if state not in guessed_state]
        new_data= pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in l:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = c[c.state == answer_state]
        guessed_state.append(answer_state)
        t.goto(int(state.x.iloc[0]), int(state.y.iloc[0]))
        t.write(answer_state)


screen.exitonclick()