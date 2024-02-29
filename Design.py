from turtle import *
setup(1000,1000)
speed(0)

#danger
def curveLeft(x):
    #setting up

    penup()
    setheading(0)
    setheading(0 * x)
    back(100 * x)
    pencolor("red")
    pendown()
    width(15 * x)

    #triangle

    forward(200 * x)
    setheading(120)
    forward(200 * x)
    setheading(240)
    forward(200 * x)

    #Curvy guy

    penup()
    color("black")
    setheading(0)
    forward((125) * x)
    setheading(90)
    forward(30 * x)
    pencolor("black")
    width(1)
    setheading(0)
    forward(10)
    pendown()
    begin_fill()
    setheading(90)
    pos = position()
    circle(50,90)
    setheading(180+45)
    forward(20)
    setheading(360-45)
    forward(20)
    pos2 = position()
    setheading(360)
    penup()
    goto(pos)
    setheading(90+45)
    pendown()
    forward(20)
    setheading(270-45)
    forward(20)
    setheading(90)
    circle(25, 90)
    end_fill()
    penup()
    forward(200)
#curveLeft(1)



def railroad():
    penup()
    goto(-700,-400)
    pencolor("gray")
    width(10)
    setheading(90)
    forward(1000)
    penup()
    setheading(0)
    forward(100)
    setheading(270)
    pendown()
    forward(100)
    penup()
    goto(-700, -400)
    setheading(90)
    forward(30)
    penup()
    setheading(0)
    back(30)
    for i in range (0, (20)):
        setheading(0)
        pos = position()
        pendown()
        forward(130)
        penup()
        goto(pos)
        setheading(90)
        forward(50)

#railroad()
