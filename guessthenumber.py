import random
computer = random.randint(1, 9)
counter = 0
guess = False
while not guess:
    usernum = int(input("Enter a number between 1 and 9: "))
    counter = counter + 1
    if usernum == computer:
        guess = True
    elif usernum < computer:
        print("Too low")
    else:
        print("Too high")

    if counter>=3:
        print("Too many guesses")
        break