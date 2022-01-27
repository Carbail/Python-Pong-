from turtle import Turtle


#Creando clase Pala heredada de Turtle para generar las palas según posición

class Pala(Turtle):
    
    def __init__(self,pInicial):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pInicial)
        
        
    def sube(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)

    def baja(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)
    
