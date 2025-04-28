import random

x = random.randint(1, 100)
z = int(input("Enter a number (1 - 100): "))

print("You were this far from my number:", abs(z - x))

if z-x < 20:
    print("Close")
elif z-x > 50:
    print("Too far")
elif z-x < 10:
    print("Yikes")
elif z-x == 0:
    print("Are you even Human?")