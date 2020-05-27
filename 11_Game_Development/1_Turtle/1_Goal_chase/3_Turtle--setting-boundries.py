'''
setting boundries
'''

import turtle

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

#Set keyboard bindings
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")
turtle.onkey(decrease_speed, "Down")

while True:
    player.forward(speed)

    #Boundary Checking
    if player.xcor()>300 or player.xcor()<-300:
        player.right(180)

    if player.ycor()>300 or player.ycor()<-300:
        player.right(180)

delay = input('Please Press Enter: ')

