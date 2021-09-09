#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
#monocle 
turtle.penup()
turtle.goto(-20,95)
turtle.width(2)
turtle.pendown()
turtle.color(0,0,0)
turtle.circle(20)

#staff
turtle.setheading(0)
turtle.penup()
turtle.goto(20,-65)
turtle.left(75)
turtle.pendown()
turtle.width(5)
turtle.color("DarkGoldenrod1")
turtle.begin_fill()
turtle.forward(250)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(240)

turtle.penup()
turtle.goto(0,-150)
turtle.pendown()
turtle.begin_fill()
turtle.forward(300)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(310)


#crown Line
turtle.penup()
turtle.goto(-100,185)
turtle.setheading(0)
turtle.pendown()
turtle.forward(150)
turtle.left(90)
turtle.forward(75)
turtle.left(135)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(135)
turtle.forward(75)

#staff jewel
turtle.penup()
turtle.goto(20,-65)
turtle.setheading(0)
turtle.left(75)
turtle.forward(250)
turtle.right(90)
turtle.forward(30)
turtle.pendown()
turtle.color("MediumBlue")

turtle.circle(75)
turtle.end_fill()









#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
