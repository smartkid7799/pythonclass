from turtle import *

def square(length):
    i=0
    while i < 4:
        forward(length)
        left(90)
        i=i+1

def polygon(length, sides):
    i=0
    while i < sides:
        forward(length)
        left(360/sides)
        i=i+1

s=int(input("Enter number of sides: "))
l=int(input("Enter length: "))
polygon(l, s)

done()