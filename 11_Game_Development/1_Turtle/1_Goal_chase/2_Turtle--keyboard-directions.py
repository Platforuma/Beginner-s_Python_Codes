'''
Generating Screen
Keyboard direction
'''

import turtle

#setup Screen
window = turtle.Screen()
window.bgcolor('lightgreen')

#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

#set speed variable
speed = 0.5

#Define Function
def turn_left():
    player.left(30)

#turn_left = lambda : player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 0.5

def decrease_speed():
    global speed
    speed -= 0.5 

#Set keyboard bindings
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")
turtle.onkey(decrease_speed, "Down")

while True:
    player.forward(speed)

delay = input('Please Press Enter: ')

