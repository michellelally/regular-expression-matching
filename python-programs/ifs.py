x = int(input("Enter an integer: "))

if x < 0: 
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else: 
    print("More")

if x < 0:
    print("Less than 0")
elif (x > 1) and (x < 10):
    print("Between 1 and 10")
elif (x < 1) or (x < 3):
    print("Less than 2 or 3")

