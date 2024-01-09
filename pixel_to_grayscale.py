# Pixel to grayscale
# Author: Dulneth
# Date: 19 December 2023

def pixel_to_grayscale(pixel: tuple) -> tuple:
    average_value = sum(pixel) / len(pixel)
    grayscale_pixel = (average_value, average_value, average_value)

    return grayscale_pixel