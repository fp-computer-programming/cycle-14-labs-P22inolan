# Author: IBN (AMDG) 3/18/2022

import turtle

window = turtle.Screen()
turt = turtle.Turtle()

window.title("Lab 4")
window.colormode(255)
turt.speed(3)
turt.color(23, 173, 146)
turt.fillcolor("red")

turt.stamp()
turt.goto(100, 100)

turt.begin_fill()
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
