# Author: IBN (AMDG) 3/17/2022

import turtle

window = turtle.Screen()
turt = turtle.Turtle()

window.setup(500, 500) # setup of window
window.screensize(400, 400)
window.title("Lab 2")

turt.right(60) # directions of turtle
turt.forward(100)
turt.right(120)
turt.forward(100)
turt.right(120)
turt.forward(100)

window.mainloop()
