from math import sqrt
user=input("Do you want to calculate a, b, or c? ")
if user == 'c':
    b = int(input("what is the length of side b? "))
    a = int(input("What is the length of side a? "))
    c=sqrt(a*a + b*b)
    print(c)
if user == 'b':
    a = int(input("what is the length of side a? "))
    c = int(input("What is the length of side c? "))
    b = sqrt(c * c - a * a)
    print(b)
if user == 'a':
    b = int(input("what is the length of side b? "))
    c = int(input("What is the length of side c? "))
    a = sqrt(c*c - b*b)
    print(a)

