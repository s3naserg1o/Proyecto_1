import turtle 
import random
ventana = turtle.Screen()
t= turtle.Turtle()
t.shape("turtle")
t.color("red")
t.width(2)
t.speed(2)
t = turtle.Turtle()
turtle.colormode(255)  
while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.pencolor(r, g, b)

    distancia = random.randint(10, 100)
    t.forward(distancia)

    angulo = random.randint(0, 360)
    t.right(angulo)
    
turtle.done