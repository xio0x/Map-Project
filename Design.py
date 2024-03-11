#CMSCP 131 Project 1
#Program will allow user to show a map with signs on it, and allow the use to see each sign individually

#SETUP
import turtle
from turtle import *
setup(1500,1000)
speed(0)
global inMap
inMap = False


#DANGER SIGN
#Charlton
def danger(x):

#setting turtle

    penup()
    setheading(0*x)
    back(100*x)
    pencolor("Red")
    pendown()
    width(15*x)

#Triangle
    color("red","white")
    begin_fill()
    forward(200*x)
    setheading(120)
    forward(200*x)
    setheading(240)
    forward(200*x)
    end_fill()

#Exclamation Mark
    penup()
    setheading(0)
    forward(100*x)
    setheading(90)
    forward(30*x)
    pendown()
    pencolor("black")
    forward(1*x)
    penup()
    forward(25*x)
    pendown()
    forward(50*x)
    penup()


#END OF DANGER SIGN



#CURVELEFT SIGN
#Charlton
def curveLeft(x):
# setting up

    penup()
    setheading(0)
    setheading(0 * x)
    back(100 * x)
    pencolor("red")
    pendown()
    width(15*x)

# triangle
    color("red", "white")
    begin_fill()
    forward(200 * x)
    setheading(120)
    forward(200 * x)
    setheading(240)
    forward(200 * x)
    end_fill()

# Curvy guy

    penup()
    color("black")
    setheading(0)
    forward(125*x)
    setheading(90)
    forward(30*x)
    pencolor("black")
    width(1)
    setheading(0)
    forward(10*x)
    pendown()
    begin_fill()
    setheading(90)
    pos = position()
#determines if creating sign in or out of map
    if inMap == False:
        circle(50, 90)
    if inMap == True:
        circle(25, 90)
    setheading(180 + 45)
    forward(20*x)
    setheading(360 - 45)
    forward(20*x)
    pos2 = position()
    setheading(360)
    penup()
    goto(pos)
    setheading(90 + 45)
    pendown()
    forward(20*x)
    setheading(270 - 45)
    forward(20*x)
    setheading(90)
#the circle's radious should be altered but it isn't :(
#so the sign has the same bottom curve always since it doesn't alter the sign in any major way
    circle(25*x, 90*x)
    end_fill()
    penup()

# END OF CURVELEFT SIGN


#STOP SIGN

def stopsign(x):
    pendown()
    color('red')
    fillcolor('red')
    begin_fill()
    for i in range(8):
        left(45)
        forward(50*x)
    end_fill()
    penup()
    if inMap == False:
        goto(-38, -8)
        right(120)
        left(70)
        forward(-55)
        backward(5)
        color('white')
        write('STOP', font=('Arial', 30, 'normal', 'bold'))
    elif inMap == True:
        setheading(90)
        forward(-100 * x)
        setheading(0)
        forward(-220 * x)
        color('white')
        pendown()
        write('STOP', font=('Arial', 20, 'normal', 'bold'))
        penup()

#END OF STOP SIGN FUNCTION


#BUS STOP SIGN

def busStop(x):
    setheading(90)
    pendown()
    pensize(3)
    color('#FFD700')
    fillcolor('#228B22')
    begin_fill()
    circle(70*x)
    end_fill()
    penup()
    pendown()
    setheading(0)
    forward(-15*x)
    setheading(90)
    color('#FFD700')
    fillcolor('#FFD700')
    begin_fill()
    circle(55*x)
    end_fill()
    penup()
    setheading(0)
    forward((-70*x - 25*x))
    setheading(90)
    forward(-70*x)
    color('#228B22')
    write('H', font=('Arial', int(90*x), 'normal'))


#END OF BUS STOP FUNCTION

#NO VEHICLES SIGN BY JOYAL SHAJI

def no_vehicles(x):
    # draws a circle for the sign and fills it in
    setheading(90)
    forward(-50*x)
    pensize(30*x)
    pendown()
    color("#c1111b", "white")
    begin_fill()
    circle(radius=int(100 * x), extent=None, steps=int(200 * x))
    end_fill()
    penup()

#END OF NO VEHICLES SIGN

#RAILROAD CROSSING SIGN BY JOYAL SHAJI

def railroad_crossing():
    speed(0)

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
        setheading(90)
        color("#c1111b", "#c1111b")
        forward(90)
        pendown()
        begin_fill()
        right(70)
        forward(106)
        left(70)
        forward(45)
        left(110)
        forward(106)
        left(70)
        forward(45)
        end_fill()

    def writing():
        #   code for the 50 m writing
        penup()
        color("black")
        setheading(90)
        forward(215)
        right(90)
        forward(50)
        write("50", True, align="center", font=("Lexend", 30, "normal"))
        right(90)
        forward(30)
        right(90)
        forward(20)
        write(arg="m", move=True, align="center", font=("Lexend", 30, "normal"))

    sign_background()
    red_strip()
    writing()
    ht()

#END OF RAILROAD CROSSING SIGN

#RAILROADCROSSING SMALLER SIGN BY JOYAL SHAJI

def railroad_crossing_small():
    speed(0)

    def sign_background_small():
        # code for the background and border of the sign
        penup()
        #goto(-50, -50)
        pendown()
        setheading(0)
        color("black", "white")
        begin_fill()
        pensize(2)
        forward(100/2.5)
        left(90)
        forward(350/2.5)
        left(90)
        forward(100/2.5)
        left(90)
        forward(350/2.5)
        end_fill()

    def red_strip_small():
        # code for the red strip and fills it in
        penup()
        setheading(90)
        color("#c1111b", "#c1111b")
        forward(90/2.5)
        pendown()
        begin_fill()
        right(70)
        forward(106/2.5)
        left(70)
        forward(45/2.5)
        left(110)
        forward(106/2.5)
        left(70)
        forward(45/2.5)
        end_fill()

    def writing_small():
        #   code for the 50 m writing
        penup()
        color("black")
        setheading(90)
        forward(215/2.5)
        right(90)
        forward(50/2.5)
        write("50", True, align="center", font=("Lexend", 10, "normal"))
        right(90)
        forward(30/2.5)
        right(90)
        forward(20/3)
        write(arg="m", move=True, align="center", font=("Lexend", 10, "normal"))

    sign_background_small()
    red_strip_small()
    writing_small()
    ht()

#END OF RAILROADCROSSING SMALLER SIGN


#FUNCTION THAT CREATES MAP BY JOYAL SHAJI
def map_design():
    screensize(None, None, "#4ce32d")

#FUNCTION THAT MAKES THE RAILROAD
#Charlton

    def railroad():
        penup()
        goto(-700, -400)
        pencolor("grey")
        width(10)
        setheading(90)
        pendown()
        forward(1000)
        penup()
        setheading(0)
        forward(75)
        setheading(270)
        pendown()
        forward(1000)
        penup()
        goto(-700, -400)
        setheading(90)
        forward(30)
        penup()
        setheading(0)
        back(30)
        pencolor("brown")
        for i in range(0, 16):
            setheading(0)
            pos = position()
            pendown()
            forward(130)
            penup()
            goto(pos)
            setheading(90)
            forward(50)

        # code for the railroad by joyal
        # also creates the curved road
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

    #   function to make roads/rectangles by joyal

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
    #   Making the roads (joyal)
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


#END OF FUNCTION THAT CREATES MAP

#FUNCTION TO MAKE SIGNS ON MAP
#Charlton
def mapSigns():
    penup()
    goto(40,-110)
    stopsign(0.2)
    goto(200, 30)
    danger(.4)
    goto(240,-110)
    busStop(.5)
    goto(140,240)
    curveLeft(.4)
    goto(-500,90)
    no_vehicles(.3)
    goto(-550, -230)
    railroad_crossing_small()

#END FUNCTION TO MAKE SIGNS ON MAP


#MENU
#Charlton

#Loops a fucntion asking for user input, ensuring that the menu will stay operable after
#something has been drawn
while True:
    print("Select and Option:")
    print("Display Map [1]")
    print("Display Specific Sign [2]")
    print("Exit [3]")
    decision = int(input())
    if decision == 1:
        turtle.Screen().reset()
        inMap = True
        speed(0)
        map_design()
        mapSigns()
    elif decision == 2:
        print("Select and Option:")
        print("Danger [1]")
        print("Curve Left [2]")
        print("Bus/Tram Stop [3]")
        print("Railroad Crossing [4]")
        print("No Vehicles of Any Kind Permitted [5]")
        print("Stop [6]")
        print("Exit [7]")
        decision2 = int(input())
        if decision2 == 1:
            penup()
            goto(0,0)
            turtle.Screen().reset()
            speed(0)
            danger(1)
        elif decision2 == 2:
            penup()
            goto(0, 0)
            turtle.Screen().reset()
            speed(0)
            inMap = False
            curveLeft(1)
        elif decision2 == 3:
            penup()
            goto(0, 0)
            turtle.Screen().reset()
            speed(0)
            busStop(1)
        elif decision2 == 4:
            penup()
            goto(0, 0)
            turtle.Screen().reset()
            speed(0)
            railroad_crossing()
        elif decision2 == 5:
            penup()
            goto(0, 0)
            turtle.Screen().reset()
            speed(0)
            no_vehicles(1)
        elif decision2 == 6:
            penup()
            inMap = False
            goto(0, 0)
            turtle.Screen().reset()
            speed(0)
            stopsign(1)

    elif decision == 3:
        exit()

#END OF MENU

Turtle._screen.exitonclick()
exit()
