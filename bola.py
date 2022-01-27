from turtle import Turtle
from random import random



class Bola(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("square")
        self.penup()
        self.movX=10
        self.movY=10
        self.velocidad=0.1
    
    
    def mueve(self):
        nuevaX = self.xcor()+self.movX
        nuevaY = self.ycor()+self.movY
        self.goto(nuevaX,nuevaY)
        
    def rebotaY(self):
        self.movY *=-1
        
    
    def rebotaX(self):
        self.movX *=-1
        self.velocidad *=0.91
    
    
    def reset_pos(self):
        self.velocidad=0.1
        self.goto(0,0)
        self.rebotaX()
       
    
    
        