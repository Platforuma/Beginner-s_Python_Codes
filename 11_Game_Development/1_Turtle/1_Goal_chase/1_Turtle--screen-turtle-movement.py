'''
Generating Screen
Developing Turtle
Moving straight
'''

import turtle

#setup Screen
window = turtle.Screen()
window.bgcolor('lightgreen')

#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
##player.penup()

#set speed variable
speed = 1

while True:
    player.forward(speed)

delay = input('Please Press Enter: ')
