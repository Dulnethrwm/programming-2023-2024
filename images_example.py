# Images and Python
# Author: Dulneth
# Date: 11 December 2023

from PIL import Image

# Open up kidgreen
with Image.open("./Images/kid-green.jpg") as im:
    # grab the pixel in the top left corner
    pixel = im.getpixel((0, 0))
    # print the pixel information
    print(pixel)