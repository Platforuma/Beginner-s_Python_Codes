'''
adding score
'''

import turtle
import math
import random
import winsound

#setup Screen
window = turtle.Screen()
window.bgcolor('lightgreen')
window.tracer(2)

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

#Adding Score
score = 0

#create goals
maxGoals = 6
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color('red')
    goals[count].shape('circle')
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randrange(-300,300),random.randrange(-300,300))

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
        
    #Move the goal
    for count in range(maxGoals):
        goals[count].forward(1)

        #Boundary Checking for goal
        if goals[count].xcor()>290 or goals[count].xcor()<-290:
            goals[count].right(180)
            winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
            
        if goals[count].ycor()>290 or goals[count].ycor()<-290:
            goals[count].right(180)
            winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
            
        #Collision Checking
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randrange(-300,300),random.randrange(-300,300))
            goals[count].right(random.randint(0,360))
            winsound.PlaySound("collision.mp3", winsound.SND_ASYNC)
            score += 1
            #print(score)
            
            #Draw the score on the screen
            borderpen.undo()
            borderpen.penup()
            borderpen.hideturtle()
            borderpen.setposition(-290,310)
            scorestring = 'Score: %s' %score
            borderpen.write(scorestring, False, align="left",font=("Arial",14,"normal"))
            

delay = input('Please Press Enter: ')

