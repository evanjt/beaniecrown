#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   A program written to calculate the amount of rows and stitches
#   to help with the determination of stitches  needed to decrease a beanie's
#   crown.
#
#   Author:     Evan Thomas
#   Email:      evan {ą} evanjt ! com

import turtle
import math

# Program constants
DECREASE_STITCH_REMOVES = 2 # knit 2 together (k2tog) dereases 2 stitches to 1

# Turtle constants
CIRCLE_RADIUS = 150         # For the simulation display
DEGREES_IN_CIRCLE = 360
DEFAULT_TURTLE_SCREEN_X = 400
DEFAULT_TURTLE_SCREEN_Y = 400
CIRCLE_BREAK_POINT_SIZE = 4

def draw_crown(circle_size, partitions, screensizex, screensizey, circle_deg, dot_size):
    angle_per_turn = circle_deg/partitions
    turtle.setup(screensizex, screensizey)
    t = turtle.Turtle()
    window = turtle.Screen()
    t.penup()               # Shift the centre
    t.goto(0,-circle_size)  # of circle downwards
    t.pendown()             # one full radius to fit
    t.speed(11) # Speed 1 slowest 11 fastest
    for i in range(partitions):
        t.circle(circle_size, extent=angle_per_turn)
        t.dot(dot_size)
    window.exitonclick() # User must click to exit

def form_explanation():
    explanation = "\nDecrease sections:\tThe amount of sections that the decrease will " \
                "occur at in each round.\n" \
                "\t\t\tIt also indicates the amount of stitches left in the final decrease\n" \
                "\t\t\tto join together at the end.\n" \
                "\n" \
                "Stitch per section:\tThe amount of stitches initially that will occur before a\n" \
                "\t\t\tknit 2 together (k2tog) occurs. This decrease by 1 after each row.\n" \
                "\n" \
                "Rows:\t\t\tThe amount of rows before arriving at the final decrease\n"
    return explanation

# Calculates the decrease possibilities based on the input stitch amount
# and returns a list of tuples on (sections, stitches per section, rows until end)
def calculate_decrease_possibilities(stitches_in_round):
    possibility_list = []
    for i in range(1,stitches_in_round):
        divisable_groups = stitches_in_round % i
        stitches_per_group = (stitches_in_round / i) - DECREASE_STITCH_REMOVES
        if (divisable_groups == 0) and (stitches_per_group >= 0):
            stitch_count = stitches_in_round
            count = 0
            while stitch_count > 0:
                stitch_count -= i
                count += 1
            possibility_list.append((int(i), int(stitches_per_group), int(count)))

    return possibility_list

def print_possibilities(possibility_list):
    for idx, possibility in enumerate(possibility_list):
        print("[{:2}] Decrease sections: {:3} | Stitches per section: {:3} | Rows: {:3}".format( \
                            idx, possibility[0], possibility[1], possibility[2]))

def decrease_pattern(num_stitches, decrease_amount):
    stitches_between = int(decrease_amount[1])
    decrease_count = int(decrease_amount[0])
    remaining_stitches = int(num_stitches - decrease_count)

    for seq in range(1, decrease_amount[2]+1):
        if seq == int(decrease_amount[2]):
            print("Row {:2} | Stitch count {:3}".format(seq, num_stitches, int(stitches_between), int(remaining_stitches)))
        else:
            print("Row {:2} | Stitch count {:3} | Stitches between decreases {:3} | Stitches after decrease {:3}".format(seq, num_stitches, int(stitches_between), int(remaining_stitches)))

        num_stitches = remaining_stitches
        stitches_between = (num_stitches / decrease_count) - DECREASE_STITCH_REMOVES
        remaining_stitches -= decrease_count

def main():
    print(form_explanation())
    num_stitches = input("Enter number of stitches in the round: ")
    possibility_list = calculate_decrease_possibilities(int(num_stitches))
    print_possibilities(possibility_list)

    print()
    choice = input("Choose desired pattern using the index number: ")
    decrease_pattern(int(num_stitches), possibility_list[int(choice)])
    decrease_amount = possibility_list[int(choice)][0]

    draw_crown(CIRCLE_RADIUS, decrease_amount, DEFAULT_TURTLE_SCREEN_X, DEFAULT_TURTLE_SCREEN_Y,
                DEGREES_IN_CIRCLE, CIRCLE_BREAK_POINT_SIZE)


if __name__ == '__main__':
    main()
