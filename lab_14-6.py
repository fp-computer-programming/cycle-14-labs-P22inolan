# Author: IBN (AMDG) 3/23/2022

import turtle

window = turtle.Screen()
turt = turtle.Turtle()

color = window.textinput("Color", "Choose a color. ") # inputs for turtle
size = window.numinput("Size", "Choose a size.", 1, 1, 5)

turt.color(color) # using inputs to create turtle
turt.shapesize(size)

turt.begin_fill() # start of square directions
turt.forward(100)
turt.right(90)
turt.forward(100)
turt.right(90)
turt.forward(100)
turt.right(90)
turt.forward(100)
turt.right(90)
turt.end_fill()

window.mainloop()