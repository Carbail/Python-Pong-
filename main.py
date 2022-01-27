from turtle import Screen, Turtle
from pala import *
from bola import *
from marcador import *
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Python Pong")
screen.tracer(0)

palaD = Pala((350,0))
palaI = Pala((-350,0))
pelota = Bola()
marcador = Marcador()
marcador.cargar()



screen.listen()

screen.onkey(palaD.sube, "Up")
screen.onkey(palaD.baja, "Down")

screen.onkey(palaI.sube, "w")
screen.onkey(palaI.baja, "s")

juegoOn = True

while juegoOn:
    time.sleep(pelota.velocidad)
    screen.update()
    pelota.mueve()
    
    #Detección de colisión muros superiores
    if pelota.ycor()>280 or pelota.ycor()<-270:
        pelota.rebotaY()
    
    #Detecta colisión palas
    if pelota.distance(palaD)< 50 and pelota.xcor()>320 or pelota.distance(palaI)< 50 and pelota.xcor()<-320 :
        pelota.rebotaX()
        
    #Detección gol a favor izquierda
    if pelota.xcor() > 380:
        marcador.marca_izq()
        pelota.reset_pos()
        
    
     #Detección gol a favor derecha
    if pelota.xcor() < -380:
        marcador.marca_der()
        pelota.reset_pos()
    
        



screen.exitonclick()