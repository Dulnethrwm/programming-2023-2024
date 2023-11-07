# Mcdonalds
# Author: Dulneth
# Date: 06 November 2023

import time

# Greet the user
print("Hey! Wanna grab something to eat?")
print("Let me help you")

# Ask if the user likes a burger
Burger = input("Would you like a burger for $5? (Yes/No)")

one_burger = 5
fries_p = 3
total = 0
burger = ["YES"]
if Burger .lower().strip(",.?! ").upper() in burger:
    Friesy = input("Would you like some fries for $3? (Yes/ No)")
    total += one_burger
    time.sleep(1)

# Ask if the user likes fries 
else:
    Friesy = input("Then would like some fries for $3? (Yes/ No)")
fries = ["YES"]
if Friesy .lower().strip(",.?! ").upper() in fries:
    total += fries_p
    time.sleep(1)

# Make the total
totalp = total / 100 * 14
total += totalp
print(f"Your total is ${total}.")