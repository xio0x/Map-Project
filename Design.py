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

    #stop
    
    pendown()
    color('white')
    fillcolor('red')
    begin_fill()
    for i in range(8):
            left(45)
            forward(50)
    end_fill()
    penup()
    goto(-38,-8)
    right(120)
    left(70)
    forward(-55)
    backward(5)
    color('white')
    write('STOP', font=('Arial', 40, 'normal', 'bold'))
    hideturtle()
    
    #circle
    
    y = 50
    pendown()
    pensize(3)
    color('#FFD700')
    fillcolor('#228B22')
    begin_fill()
    circle(x)
    end_fill()
    penup()
    goto(0,20)
    pendown()
    color('#FFD700')
    fillcolor('#FFD700')
    begin_fill()
    circle(y)
    end_fill()
    penup()
    hideturtle()
    goto(-31,19)
    color('#228B22')
    write('H', font=('Arial', 90, 'normal'))

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

def no_vehicles(x):
    # draws a circle for the sign and fills it in
    speed(0)
    goto(0, -50 * (2 * x))
    pensize(30 * x)
    pendown()
    color("#c1111b", "white")
    begin_fill()
    circle(radius=100 * x, extent=None, steps=200 * x)
    end_fill()

#no_vehicles(3)

def railroad_crossing():
    speed(4)

    def sign_background():
        # code for the background and border of the sign
        penup()
        goto(-50, -50)
        pendown()
        color("black", "white")
        begin_fill()
        pensize(5)
        forward(100)
        left(90)
        forward(350)
        left(90)
        forward(100)
        left(90)
        forward(350)
        end_fill()

    def red_strip():
        # code for the red strip and fills it in
        penup()
        color("#c1111b", "#c1111b")
        begin_fill()
        goto(-50, 40)
        pendown()
        goto(50, 90)
        left(180)
        forward(40)
        goto(-50, 80)
        right(180)
        forward(40)
        end_fill()

        # code that outlines the shape in a black line to make it neater
        penup()
        goto(-50, -50)
        left(90)
        pendown()
        color("black")
        pensize(5)
        forward(100)
        left(90)
        forward(350)
        left(90)
        forward(100)
        left(90)
        forward(350)

    def writing():
        #   code for the 50 m writing
        penup()
        color("black")
        goto(0, 255)
        write("50", True, align="center", font=("Lexend", 30, "normal"))
        goto(0, 230)
        write(arg="m", move=True, align="center", font=("Lexend", 30, "normal"))

    sign_background()
    red_strip()
    writing()
    ht()
#railroad_crossing():

#    Code for the map

setup(1500,1000)
screensize(None, None, "#4ce32d")
speed(0)


def map_design():

    def railroad():
        # code for the rungs

        penup()
        goto(-700, -400)
        pencolor("brown")
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
        for i in range(0, 16):
            setheading(0)
            pos = position()
            pendown()
            forward(130)
            penup()
            goto(pos)
            setheading(90)
            forward(50)

        # code for the railroad
        pensize(8)
        pencolor("grey")
        penup()
        goto(-700,-400)
        pendown()
        forward(800)
        penup()
        goto(-620, -400)
        pendown()
        forward(800)

    railroad()

    #   function to make roads/rectangles

    def road_rectangle(l, w):
        color("light gray")
        begin_fill()
        forward(w)
        left(90)
        forward(l)
        left(90)
        forward(w)
        left(90)
        forward(l)
        end_fill()
    #   Making the roads
    left(180)
    forward(200)
    road_rectangle(700, 60)
    back(700)
    left(90)
    road_rectangle(60, 600)
    teleport(-250,440)
    road_rectangle(500, 60)
    back(500)
    right(90)
    road_rectangle(60, 330)
    teleport(-620, -250)
    road_rectangle(1500, 60)
    teleport(120,169)
    pensize(70)
    right(180)
    circle(300, 90)
    ht()

    railroad()


#map_design()
