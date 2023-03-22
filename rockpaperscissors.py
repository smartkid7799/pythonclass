import random
user = input("Enter r for rock, p for paper, or s for scissors: ")
computer = random.choice(['r', 'p', 's'])
if user == 'r' and computer == 's':
    print("Computer selected scissors and you won")
elif user == 'p' and computer == 'r':
    print("computer selected Rock and you won")
elif user =='s' and computer =='p':
    print("Computer selected paper and you won")
elif user == 's' and computer == 's':
    print("it's a tie'")
elif user == 'r' and computer == 'r':
    print("it's a tie")
elif user == 'p' and computer == 'p':
    print("it's a tie")
elif user == 's' and computer == 'r':
    print("Computer selected rock and you lost")
elif user == 'r' and computer == 'p':
    print("computer selected paper and you lost")
elif user =='p' and computer =='s':
    print("Computer selected scissors and you lost")