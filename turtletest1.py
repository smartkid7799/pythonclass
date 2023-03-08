from turtle import *

color("blue", "cyan")
pensize(5)

begin_fill()
sides = 1000
i = 0
while i<sides:
    forward(1)
    left(360/sides)
    i=i+1

end_fill()
done()