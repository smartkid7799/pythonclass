name= input("Enter your name. ")
print(name)
x = 0
while x<(len(name)):
    print(name[x])
    x=x+1

strlist = ["Hello", name]
print(f"Hello {name}")
toPrint = ' '.join(strlist)
print(toPrint)