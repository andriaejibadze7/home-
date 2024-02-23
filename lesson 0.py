from turtle import *

#we want to point a house

#step 1:  draw a square

width(5)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

forward(75)
left(90)

color("green")
begin_fill()
forward(75)
right(90)

forward(50)
right(90)

forward(75)
left(90)
end_fill()
color("blue")
forward(75)
left(90)

forward(200)
left(45)

color("red")
begin_fill()
forward(144)
left(90)

forward(144)
left(45)
end_fill()

penup()
goto(40, 160)
pendown()

color("black")
forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

penup()
goto(60, 160)
pendown()

forward(40)
left(90)

penup()
goto(40, 140)
pendown()

forward(40)
right(90)
 
penup()
goto(130, 160)
pendown()

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

forward(40)
left(90)

penup()
goto(150, 160)
pendown()

forward(40)
left(90)

penup()
goto(130,140)
pendown()

forward(40)

exitonclick()