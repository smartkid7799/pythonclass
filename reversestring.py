name = input("Enter name: ")
revString = ""
counter = len(name) - 1
while counter >= 0:
    revString = revString + name[counter]
    counter = counter - 1
print(revString)
if name == revString:
    print("This is a palindrome")