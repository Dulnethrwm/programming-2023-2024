# Colour helper

BLACK_PIXEL = (0, 0, 0)
WHITE_PIXEL = (255, 255, 255)

def is_light(pixel: tuple) -> bool:
    average = sum(pixel) / len(pixel)
    """"""

    return average>= 128