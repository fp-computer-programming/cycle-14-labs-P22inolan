# Author: IBN (AMDG) 3/17/2022

import turtle

window = turtle.Screen()
turt = turtle.Turtle()

window.setup(1000, 1000) # setup of window
window.screensize(500, 500)
window.title("Lab 1")

turt.forward(250) # directions for turtle
turt.right(90)
turt.forward(100)
turt.right(90)
turt.forward(250)
turt.right(90)
turt.forward(100)
turt.right(90)

window.mainloop()