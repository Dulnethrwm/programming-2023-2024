# Images Problem
# Author: Dulneth
# 19 December 2023
from PIL import Image
import colour_helper

def picture_to_grayscale(filename: str) -> None:
    """Convert a given picture to grayscale"""

    # Open up the image
    with Image.open(f"./Images/best_pizza.png") as im:
        # Visit every pixel
        for y in range(im.height):
            for x in range(im.width):    
                pixel = im.getpixel((x, y))
                
                # Take that pixel and convert it to gray
                gray_pixel = colour_helper.pixel_to_grayscale(pixel)

                im.putpixel((x, y), gray_pixel)
        
        # Save the image
        im.save("./Images/grayscale.jpg")