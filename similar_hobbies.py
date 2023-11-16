# Similar Hobbies
# Author: Dulneth Mohottala
# Date: 14 November 2023

# variables
common_similarity = 0

# Greet the user
print("Hey!")

# Ask their hobbies
print("Please enter 3 of your hobbies seperated by spaces.")
p_1 = input("Person 1:").lower().split()
p_2 = input("Person 2:").lower().split()

# Calculate the common
if p_1[0] in p_2:
    common_similarity += 1
if p_1[1] in p_2:
    common_similarity += 1
if p_1[2] in p_2:
    common_similarity += 1

# Show the score
print(f"You have {common_similarity} hobbies in commmon.")