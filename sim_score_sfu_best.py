# SFU best similarity score
# Author: Dulneth
# Date: 10 November 2023

# Load data from a file.
# Read in a meaningful way
# Link our Sim Score algo to data

most_similar_score = 0
most_similar_name = ""
least_similar_score = 10
least_similar_name = ""

# Open the file
with open("./data.csv") as f:
    # Get the first line of data
    print(f.readline())

    # The second of the csv file
    print(f.readline())

# Create a "profile" of likes (fave places in SFU)
profile = [
    "Bubble Wolrd", 
    "Chef Hung", 
    "Uncle Fatih's", 
    "Guadalupe (MBC)", 
    "Steve's Poke Bar"
]

with open("./data.csv") as f:
    # Throw away the header
    header = f.readline()
    
    for line in f:
        # Convert the string to a list
        current_likes = line.split(",")

        # Store the person's name
        current_name = current_likes[1]

        # Initialize the current sim score
        current_sim_score = 0
        
        for item in profile:
            if item in current_likes:
                current_sim_score += 1

        # Print the results from this line of data
        print(f"{current_name} - Score: {current_sim_score}")

        # Update the most similar person
        if current_sim_score > most_similar_score:
            most_similar_score = current_sim_score
            most_similar_name = current_name
       
print("----Most Similar----")
print(f"🏅{most_similar_name} - {most_similar_score}")


if current_name == 0:
    input(current_name)
print("----Least Similar----")
print(f"{current_name}- {least_similar_score}")

        # For every line of data in our csv file
            # Convert the string to a list

            # For item in profile
                #If item in current line"s likes
                    #Increase sim score by 1