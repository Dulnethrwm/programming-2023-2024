# Functions Practice
# Author: Dulneth
# Date: 24 November 2023

def print_area_of_a_square(sidelength: float) -> None:
    """Calculates the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square"""

    area = sidelength**2

    print(
        f"The area of a square with side length = {sidelength} is: {area} square units"
    )


def area_of_a_square(sidelength: float) -> float:
    """Returns the area of a square with given
    sidelength

    Params:

    sidelength - length of one side of a square
    """
    area = sidelength**2

    return area


print_area_of_a_square(12.2)
print_area_of_a_square(13)
# sum_areas = area_of_a_square(12.2) + area_of_a_square(13)
print(area_of_a_square(2))

print(print_area_of_a_square(2))


# Question no.1
ask = input("Give me a number.")
def stars(number: int) -> str:
    return '*' * number

answer = stars(int(ask))
print(answer)


# Question no.2
def biggest_of_three():
    number_1 = float(input("Give me a number"))
    number_2 = float(input("Give me another number"))
    number_3=float(input("Give me another number"))
    if number_1 >= number_2 and number_1 >= number_3:
        return number_1
    elif number_2 >= number_1 and number_2 >= number_3:
        return number_2
    else:
        return number_3
    
result = biggest_of_three()
print(f"The biggest is {result}")


# Question no.3
def pyramid(num_layers: int) -> None:
    """Prints out a pyramid of given number of layers.

    Params:
    num_layers - number of layers in the pyramid
    """

    for current_layer in range(1, num_layers + 1):
        print(stars(current_layer))


pyramid(2)
pyramid(3)
pyramid(20)


# Question no.4
def pyramid_mirror(num_layers: int) -> None:
    """Prints out a mirrored pyramid.

    Params:
    num_layers - number of layers of pyramid
    """

    for current_layer in range(1, num_layers + 1):
        # Print the spaces then print the stars
        # num_layers == 2
        # " " * 1  +  stars(1)
        # " " * 0   + stars(2)
        # num_layers == 3
        # " " * 2  + stars(1)
        # " " * 1  + stars(2)
        # " " * 0  + stars(3)
        print(" " * (num_layers - current_layer) + stars(current_layer))


pyramid_mirror(4)
pyramid_mirror(20)

def inear_search(l: list, item: Any) -> int:
	"""Search through a list and if found, returns the index of the first occurence of item.

Params: 
	1 - list we're searching through
	item - item we're looking for
"""
counter = 0

# search algorithm
for thing in l:
	if thing == item:
		return counter
	counter += 1

return -1
