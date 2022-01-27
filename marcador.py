from turtle import Turtle

class Marcador(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p_izq = 0
        self.p_der = 0
        
    def cargar(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.p_izq, align="center", font=("Robota",40,"normal"))
        self.goto(100,200)
        self.write(self.p_der, align="center", font=("Robota",40,"normal"))
        
    def marca_izq(self):
        self.p_izq +=1
        self.cargar()
            
    def marca_der(self):
        self.p_der +=1
        self.cargar()
            
            