username = input("Enter your name:")
password = input("Enter your password:")
passwordlength = len(password)
while passwordlength < 8:
    print("password must be more than 8 characters long")
    password = input("Enter your password:")
    passwordlength = len(password)
hiddenpassword = '*' * len(password)
print(f"hello {username} your password is {hiddenpassword}")
