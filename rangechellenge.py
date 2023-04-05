user = int(input("input a number"))
numlist=list(range(1,user,1))
print("list of numbers")
for num in numlist:
    print(num)
print("even numbers")
numlist=list(range(0,user,2))
for num in numlist:
    print(num+2)
print("odd numbers")
numlist = list(range(1, user, 2))
for num in numlist:
     print(num + 2)
numlist = list(range(1, user, 2))
counter=0
numlist = list(range(1, user, 1))
print("addition of all numbers")
for num in numlist:
    counter=counter+num
print(counter)