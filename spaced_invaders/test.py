import turtle
import os
import math
import random
import pygame
import pickle
import sys

FPS = 60
ANIMATION_SPEED = 0.18

pygame.init()

lasersound = pygame.mixer.Sound("laser.wav")
explosion = pygame.mixer.Sound("explosion.wav")
bombesound = pygame.mixer.Sound("Bomb+2.wav")
pygame.mixer.music.load("laserattack.wav")
pygame.mixer.music.play(-1)

#Screen
window = turtle.Screen()
window.bgcolor("black")
window.bgpic("lights.gif")
window.title("Spaced Invaders")
window.setup(width = 800, height = 800)

#register shapesize
turtle.register_shape("alienship.gif")
turtle.register_shape("ship1.gif")
turtle.register_shape("laser.gif")
turtle.register_shape("bomb.gif")
turtle.register_shape("life.gif")

#border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-360,-360)
border_pen.pendown()
border_pen.pensize(3)
for side in range (4):
    border_pen.fd(720)
    border_pen.lt(90)
border_pen.hideturtle()

#score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-375, 375)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#life
number_of_lives = 3
lives= []

for i in range(number_of_lives):
	lives.append(turtle.Turtle())

	life_pen = turtle.Turtle()
	life_pen.speed(0)
	life_pen.color("white")
	life_pen.penup()
	life_pen.setposition(360, 380)
	lifestring = "Lives: %l" %lives
	life_pen.write(lifetring, False, align="left", font=("Arial", 14, "normal"))
	life_pen.hideturtle()

#player
player = turtle.Turtle()
player.color("blue")
player.shape("ship1.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 60

#move left or right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -340:
        x = -340
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > +340:
        x = +340
    player.setx(x)

#def collision
def iscollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 50:
        return True

#make invaders
number_of_invaders = 5
invaders = []
for i in range(number_of_invaders):
    invaders.append(turtle.Turtle())

for invader in invaders:
    invader.color("red")
    invader.shape("alienship.gif")
    invader.penup()
    invader.speed(0)
    x = random.randint(-300, 300)
    y = random.randint(100, 300)
    invader.setposition(x, y)

invaderspeed = 5

#bombspeed
bombstate = "ready"

#for invader in invaders:
bomb = turtle.Turtle()
bomb.color("red")
bomb.shape("bomb.gif")
bomb.penup()
bomb.speed(0)
bomb.setheading(-90)
bomb.shapesize(1, 1)
bomb.hideturtle()

def drop_bomb():
    global bombstate
    if bombstate == "ready":
        x = invader.xcor()
        y = invader.ycor() - 15
        bomb.setposition(x,y)
        bomb.showturtle()
        bombstate = "fire"
        bombesound.play()
bombspeed = 25
bombstate = "ready"

#players laser
laser = turtle.Turtle()
laser.color("red")
laser.shape("laser.gif")
laser.penup()
laser.speed(0)
laser.setheading(90)
laser.shapesize(2, 2)
laser.hideturtle()

laserspeed = 120

laserstate = "ready"

def fire_laser():
    global laserstate
    if laserstate == "ready":
        x = player.xcor()
        y = player.ycor() + 15
        laser.setposition(x,y)
        laser.showturtle()
        laserstate = "fire"
        lasersound.play()

#keyboard bindings

turtle.listen()
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")

turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

turtle.onkey(fire_laser, "space")

turtle.onkey(drop_bomb,  "1")

#game loop
while True:

#move invader
    for invader in invaders:
        x = invader.xcor()
        x += invaderspeed
        invader.setx(x)

        if invader.xcor() > 340:
            for e in invaders:
                y = e.ycor()
                y -= 40
                invaderspeed *= -1
                e.sety(y)
        if invader.xcor() < -340:
            for e in invaders:
                y = e.ycor()
                y -= 40
                invaderspeed *= -1
                e.sety(y)

#collision check
        if iscollision(laser, invader):
            laser.hideturtle()
            laserstate = "ready"
            laser.setposition(0,-400)
            x = random.randint(-300, 300)
            y = random.randint(100, 300)
            invader.setposition(x, y)
            explosion.play()
                        
            #update score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if iscollision(player, invader):
            player.hideturtle()
            invader.hideturtle()
            explosion.play()
            game_overpen = turtle.Turtle()
            game_overpen.speed(0)
            game_overpen.color("white")
            game_overpen.penup()
            game_overpen.setposition(-100, 100)
                   
	 #update life
            life -= 1
            lifestring = "Lives: %l" %lives
            life_pen.clear()
            life_pen.write(lifestring, False, align="left", font=("Arial", 14, "normal"))

        
            print ("Game Over")

        if iscollision(bomb, player):
            player.hideturtle()
            bomb.hideturtle()
            explosion.play()
            game_overpen = turtle.Turtle()
            game_overpen.speed(0)
            game_overpen.color("white")
            game_overpen.penup()
            game_overpen.setposition(-100, 100)
            game_overpen.write("GAME OVER", False, align="left", font=("Arial", 30, "bold"))
            game_overpen.hideturtle()
            pygame.mixer.music.stop()
            print ("Game Over")

#move laser
    if laserstate == "fire":
        y = laser.ycor()
        y += laserspeed
        laser.sety(y)

    if laser.ycor( ) > 340:
        laser.hideturtle()
        laserstate = "ready"
#move bomb
    if bombstate == "fire":
        y = bomb.ycor()
        y -= bombspeed
        bomb.sety(y)

    if bomb.ycor( ) < -340:
        bomb.hideturtle()
        bombstate = "ready"

#if invader gets past you
    if invader.ycor() < -340:
        explosion.play()
        game_overpen = turtle.Turtle()
        game_overpen.speed(0)
        game_overpen.color("white")
        game_overpen.penup()
        game_overpen.setposition(-100, 100)
        game_overpen.write("GAME OVER", False, align="left", font=("Arial", 30, "bold"))
        game_overpen.hideturtle()
        pygame.mixer.music.stop()
        print ("Game Over")


delay = input("Press Enter To Finish")

