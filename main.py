from turtle import *

def house():
    #house
    speed(10)
    penup()
    goto(-130, -89)
    pendown()
    color("brown")
    begin_fill()
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    end_fill()

    #window
    color("lightblue")
    penup()
    goto(-95, -20)
    pendown()
    begin_fill()
    forward(35)
    left(90)
    forward(35)
    left(90)
    forward(35)
    left(90)
    forward(35)
    end_fill()

    #roof
    penup()
    goto(-30, 12)
    pendown()
    color("red")
    begin_fill()
    for i in range(3):
        forward(100)
        right(120)
    end_fill()
    



def background():
    #grass
    speed(10)
    penup()
    goto(-250,-90)
    pendown()
    color("green")
    begin_fill()
    for i in range(4):
        forward(500)
        right(90)
    end_fill()

    #sky
    penup()
    goto(-250, -89)
    pendown()
    color("cyan")
    begin_fill()
    for i in range(4):
        forward(500)
        left(90)
    end_fill()


def sun():
    color('yellow')
    penup()
    goto(140, 140)
    pendown()
    pensize(2)
    for i in range(3):
        speed(30)
        forward(45)
        left(120)





background()
house()
sun()
speed(100)
for i in range(30):
    left(20)
    sun()

speed(10)
hideturtle()
exitonclick()
