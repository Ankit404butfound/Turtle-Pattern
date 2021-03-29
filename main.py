import turtle
from turtle import Screen

a=0
b=0

turtle.bgcolor("black")
turtle.speed(0)
screen=Screen()
screen.colormode(255) 
turtle.pencolor(250,0,0)
turtle.penup()
turtle.goto(0,200)
turtle.pendown()

while True:
    turtle.pencolor(250-(b),50,50+b)
    turtle.forward(a)
    turtle.right(b)

    a+=3
    b+=1

    if b==201:
        break


turtle.done()
