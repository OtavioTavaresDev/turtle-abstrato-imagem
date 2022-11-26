import turtle
from turtle import *

begin_fill()
color("cyan")
speed(10000)

bg = Screen()
bg.bgcolor("black")

for i in range(15):
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(90)
    right(100)
    circle(100)
    forward(20)
    right(90)
    forward(20)
    circle(140)
    right(90)
    circle(180)


done()
end_fill()



