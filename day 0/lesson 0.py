from turtle import *

speed(15)

#main box of the house

width(5)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(70)
right(90)
forward(120)
end_fill()


#roof

penup()
goto(200,200)
pendown() 

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#left window

penup()
goto(20,180)
pendown()

color("blue")

begin_fill()

left(30)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

end_fill() 

penup()
goto (140,180)
pendown()

begin_fill()

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

end_fill() 

exitonclick() 