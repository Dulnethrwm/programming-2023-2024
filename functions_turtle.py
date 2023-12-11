# Functions and Turtle
# Author: Ubial
# 28 November 2023

import turtle

alfred_river_wilson = turtle.Turtle()

alfred_river_wilson.color("lightblue")


def squared(num: float) -> float:
    """Takes a number and squares and returns it."""

    return num**2


def draw_square(side_length: int) -> None:
    """Draw a square of a given length."""
    alfred_river_wilson.forward(side_length)
    alfred_river_wilson.left(90)
    alfred_river_wilson.forward(side_length)
    alfred_river_wilson.left(90)
    alfred_river_wilson.forward(side_length)
    alfred_river_wilson.left(90)
    alfred_river_wilson.forward(side_length)
    alfred_river_wilson.left(90)


def draw_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree
    with initial given height in pixels

    Params:

    level - number representing the levels of branches
    height - height of the main trunk in pixels
    """

    if level > 0:
        # 1. Move turtle forward height pixels
        alfred_river_wilson.forward(height)

        # 2. Turn turtle left
        alfred_river_wilson.left(36)
        #    a. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height * 0.75)

        # 3. Turn turtle right
        alfred_river_wilson.right(36 * 2)
        #    a. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height * 0.75)

        # 4. Return to beginning
        alfred_river_wilson.left(36)
        alfred_river_wilson.back(height)
    else:
        original_colour = alfred_river_wilson.color()
        alfred_river_wilson.color("green")
        alfred_river_wilson.stamp()
        alfred_river_wilson.color(original_colour[0])  # revert alfred river wilson's colour


def draw_fancy_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree
    with initial given height in pixels

    Params:

    level - number representing the levels of branches
    height - height of the main trunk in pixels
    """

    if level > 0:
        # 1. Move turtle forward height pixels
        alfred_river_wilson.forward(height)

        # 2. Turn turtle left
        alfred_river_wilson.left(36)
        #    a. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * 0.65)

        alfred_river_wilson.right(36)
        draw_fancy_tree(level - 1, height * 0.65)

        # 3. Turn turtle right
        alfred_river_wilson.right(36)
        #    a. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * 0.65)

        # 4. Return to beginning
        alfred_river_wilson.left(36)
        alfred_river_wilson.back(height)
    else:
        original_colour = alfred_river_wilson.color()
        alfred_river_wilson.color("green")
        alfred_river_wilson.stamp()
        alfred_river_wilson.color(original_colour[0])  # revert alfred river wilson's colour


# Set-up Burt to draw trees
alfred_river_wilson.color("brown")
alfred_river_wilson.setheading(90)  # points alfred river wilson north
alfred_river_wilson.pu()
alfred_river_wilson.back(50)
alfred_river_wilson.pd()
alfred_river_wilson.width(4)  # trunk and branches thicker
alfred_river_wilson.speed(5)
alfred_river_wilson.shapesize(2, 2, 2)

draw_fancy_tree(4, 175)

turtle.done()
