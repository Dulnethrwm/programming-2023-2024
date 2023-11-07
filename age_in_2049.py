# Age in 2049
# Author: Dulneth
# Date: 02 November 2023

# Greet the user
print("Hey I'm here to calculate your age in 2049")

# Ask the user's current age
age = [
    "How old are you right now?"
]

for question in age:
    print(question)
# calculate the user's age in 2049
user_age = int(input().strip(",.?! "))
total_age = user_age + 26

# Present it
print(f"You will be {total_age} in 2049 ")