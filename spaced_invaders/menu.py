import pygame
import turtle
import os
import time

pygame.init()

 


window = turtle.Screen()
window.bgcolor("black")
window.bgpic("lights.gif")
window.title("Spaced Invaders")

def app_quit():
    pygame.quit()

turtle.listen() 
turtle.onkey(app_quit,  "q")
turtle.onkey(app_quit, "Escape")


intro = True
while intro:

   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
            if event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                run  = False
            if event.key == pygame.K_q:
                pygame.quit()
                run  = False  



delay = input("Press Enter To Finish")
pygame.quit()