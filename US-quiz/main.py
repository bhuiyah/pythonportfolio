import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("U.S.A States Game")
states = pandas.read_csv("50_states.csv")
screen.setup(800, 600)
all_states = states.state.to_list()
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)
guessed_states = []

while len(guessed_states) <= 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "Guess the States One at a Time").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_chosen = states[states.state == answer_state]
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto((int(state_chosen.x), int(state_chosen.y)))
        state_name.write(answer_state)
        
states_to_learn = [s for s in all_states if s not in guessed_states] 
    
pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
    



