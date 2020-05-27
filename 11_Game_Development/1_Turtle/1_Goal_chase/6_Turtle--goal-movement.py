'''
Generating Screen
Developing Turtle
Moving straight
'''

import turtle
import math
import random

#setup Screen
window = turtle.Screen()
window.bgcolor('lightgreen')

#Draw border
borderpen = turtle.Turtle()
borderpen.penup()
borderpen.setposition(-300,-300)
borderpen.pendown()
borderpen.pensize(3)
for side in range(4):
    borderpen.forward(600)
    borderpen.left(90)
borderpen.hideturtle ()

#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0) #animation speed

#Create Goal
goal = turtle.Turtle()
goal.color('red')
goal.shape('circle')
goal.penup()
goal.speed(0)
goal.setposition(random.randrange(-300,300),random.randrange(-300,300))

#set speed variable
speed = 0.5

#Define Function
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 0.5

def decrease_speed():
    global speed
    speed -= 0.5

#collision function
def isCollision(t1, t2):
    d = math.sqrt(math.pow((t1.xcor()-t2.xcor()),2) + math.pow((t1.ycor()-t2.ycor()),2))
    if d < 20:
        return True
    else:
        return False

#Set keyboard bindings
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")
turtle.onkey(decrease_speed, "Down")

while True:
    player.forward(speed)

    #Boundary Checking for player
    if player.xcor()>300 or player.xcor()<-300:
        player.right(180)

    if player.ycor()>300 or player.ycor()<-300:
        player.right(180)

    #Collision Checking
    if isCollision(player, goal):
        goal.setposition(random.randrange(-300,300),random.randrange(-300,300))
        goal.right(random.randint(0,360))
        
    #Move the goal
    goal.forward(3)

    #Boundary Checking for goal
    if goal.xcor()>290 or goal.xcor()<-290:
        goal.right(180)

    if goal.ycor()>290 or goal.ycor()<-290:
        goal.right(180)

        
delay = input('Please Press Enter: ')

