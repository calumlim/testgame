#Space Invaders game

import turtle
import os

#set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#window border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
    border_pen.hideturtle()
#delay = input("Press enter to finish.")

#create the player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(-0,-250)
player.setheading(90)

#Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

#create the players weapon
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

#Bullet functions
#States:
#ready - ready to fire
#fire - bullet is moving
bulletstate = "ready"
bulletspeed = 20

#Player movement
playerspeed = 15
enemyspeed = 2
#left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #move the bullet to above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x,y+10)
        bullet.showturtle()
    
#create keyboard bindings
turtle.listen()
turtle.onkey(fire_bullet, "space")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")

#main game loop
while True:
    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #reverse enemy position
    if enemy.xcor() >280:
        y = enemy.ycor()
        y -=20
        enemyspeed *= -1
        enemy.sety(y)
        
    if enemy.xcor() <-280:
        y = enemy.ycor()
        y -=20
        enemyspeed*= -1
        enemy.sety(y)
    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

    #bullet border checking
    if bullet.ycor()>290:
        bullet.hideturtle()
        bulletstate = "ready"
