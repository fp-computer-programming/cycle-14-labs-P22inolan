# Author: IBN (AMDG) 3/18/2022

import turtle

window = turtle.Screen()
turt = turtle.Turtle()

window.bgcolor("grey") # setup of window
window.setup(500, 500)
window.screensize(400, 400)
window.title("Lab 3")
window.colormode(255)
turt.shape("turtle") # setup of turtle
turt.pencolor(23, 173, 131)

turt.left(180)
for x in range(3): # loop for making the triangle
    turt.forward(200)
    turt.right(120)

window.mainloop()
