# Semester Evaluator
# Author: Dulneth
# Date: 07 November 2023

import time

# Greet the user
print("Hey!")

#  Ask the user about their courses
courses = input("How many courses do you have this semester")

time.sleep(1)

# Create a list if questions to ask
questions = [
    "How do you rate your course 1(out of 5)?",
    "How do you rate course 2 (out of 5)?",
    "How do you rate course 3(out of 5)?",
    "How do you rate your 4th course (out of 5)?"
]
total_rating = 0

# Give the judge's score individually
for answer in questions:
    time.sleep(1)
    # Get score from judge
    rate = input(answer)

    # Calculate the total score
    total_rating += float(rate)

# Calculate the average
average_rating = total_rating / len(questions)
print(f"Your averag rating is {average_rating}")

