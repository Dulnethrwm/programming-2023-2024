# Turtle Example
# Author: Dulneth
# Date: 21 November 2023

import turtle

# ---- CONSTANTS
TURTLE_MAGNITUDE = 20
# Create a turtle
michaelangelo = turtle.Turtle()

# Get some instructions from the user
print("""To give commands, type:
F - to go forward
L - to go left
R - to go right
B - to go backward
Stop - to stop""")

# Repeat the code indefinetely
done = False

while not done:
    command = input("Where should I go?")
    # Based on te instructions move the turtle on the screen.
    if command.strip(".,?! ").lower() == "f":
        michaelangelo.forward(TURTLE_MAGNITUDE)
    elif command.strip(".,?! ").lower() == "r":
        michaelangelo.right(90)
    elif command.strip(".,?! ").lower() == "l":
        michaelangelo.left(90)
    elif command.strip(".,?! ").lower() == "b":
        michaelangelo.backward(TURTLE_MAGNITUDE)
    elif command  == "stop":
        done = True