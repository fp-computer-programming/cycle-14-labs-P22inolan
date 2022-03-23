# Author: IBN (AMDG) 3/23/2022

import turtle


def move_forward(): # forward function
    toby.forward(50)


def move_backward(): # backward function
    toby.backward(50)

def turn_left(): # left turn function
    toby.left(90)


def turn_right(): # right turn function
    toby.right(90)


window = turtle.Screen() # create window

toby = turtle.Turtle() # create turtle

window.onkey(move_forward, "Up") # keybinds for functions
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")
window.listen()

window.mainloop()