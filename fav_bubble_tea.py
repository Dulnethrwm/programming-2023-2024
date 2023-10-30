# Bubble Tea Populaity Algorithm
# Author: Dulneth
# Date: 27 October 2023

# Ask 5 users what their favourite bubble tea place is 
# Print out a summary of the data

# ----- CONSTANTS

NUM_RESPONDENTS = 5

# -----

# Like counters
coco_likes = 0
suntea_likes = 0
chatime_likes = 0
bbqueen_like = 0
xingfutang_likes = 0

for _ in range(NUM_RESPONDENTS): 
    # Ask the user what their favourite bbt place is
    print("What's your favourite bubble tea place?")
    fave_bbt = input().strip(",.?! ").lower()

    # tallying/Counting Algo
    # Options: CoCo, Chatime, SunTea, Xing Fu Tang, Bubble Queen
    # if they say CoCo, increase the counter for CoCo by one, etc.
    if fave_bbt == "coco":
        coco_likes = coco_likes + 1
    elif fave_bbt == "chatime":
        chatime_likes += 1
    elif fave_bbt == "suntea":
        suntea_likes += 1
    elif fave_bbt == "xingfutang":
        xingfutang_likes +=1
    elif fave_bbt == "bubble queen":
        bbqueen_like +=1

# Print the summary of the results
print(f"Chatime Likes - {chatime_likes} | Percentage - {round(chatime_likes / NUM_RESPONDENTS * 100, 2)}%")
print(f"CoCo Likes - {coco_likes} | Percentage - {round(coco_likes/NUM_RESPONDENTS*100, 2)}%")
print(f"SunTea Likes - {suntea_likes} | Percentage - {round(suntea_likes/NUM_RESPONDENTS*100, 2)}%")
print(f"BBQueen Likes - {bbqueen_like} | Percentage - {round(bbqueen_like /NUM_RESPONDENTS*100, 2)}%")
print(f"Xing Fu Tang Likes - {xingfutang_likes} | Percentage - {round(xingfutang_likes/NUM_RESPONDENTS*100,2)}%")