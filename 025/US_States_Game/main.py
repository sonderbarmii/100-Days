import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "025/US_States_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

data = pandas.read_csv("025/US_States_Game/50_states.csv")
states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states)} States correct",prompt="What's another state's name?").title() # convert the guess to Title case = done

    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)      
        new_data.to_csv("025/US_States_Game/missing_states.csv")
        break
    elif answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        x = int(data[data.state == answer_state].x)
        y = int(data[data.state == answer_state].y)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x,y)
        writer.write(answer_state, align="center")

    


turtle.mainloop() # alternative to exitonclick, but since we need to click on the img, we do not want it to exit


# Angelas Solution Pt.1

# score = 0

# data = pandas.read_csv("025/US_States_Game/50_states.csv")
# states = data.state.to_list()
# guessed_states = []

# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",prompt="What's another state's name?").title() # convert the guess to Title case = done

# # If answer_state is one of the states in all the states of the 50_states.csv
#     if answer_state == "Exit":
#        break
#     elif answer_state in states:
#         guessed_state.append(answer_state)
#         # if they got it right:
#         # create a turtle to write the name of the state at the state's x and y coordinate
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))
#         t.write(answer_state)

