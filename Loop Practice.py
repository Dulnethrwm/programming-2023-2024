# Loop Practice
# Author: Dulneth
# Date:10 October 2023

import time

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games"]

# Do something for each thing in the list
# Print it out in a pretty way

for item in groceries:
    print(f"* {item}" )
    print("   ---")

# Create a pyramid like this using a for loop

# *
# **
# ***
# ****

stars = ["*", "**", "***", "****", "*****", "******"]
for item in stars:
    print(f" {item}" )
    
# Problem
## Create a new year's eve countdown
# Reqiurements
#  * Starts off at 10
#  * Countdown every second
#  * Instead of reaching zero it says "Happy New Year"
# Example Output: 
#   10
#   9
#   8
#   7
#   6
#   ....
#   Happy New Year

countdown = ["10", "9", "8", "7","6", "5", "4", "3", "2", "1", "Happy New Year!"]

for item in countdown:
    print(f" {item}")
    time.sleep(1)