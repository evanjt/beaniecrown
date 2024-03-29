#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   A program written to calculate the amount of rows and stitches
#   to help with the determination of stitches  needed to decrease a beanie's
#   crown.
#
#   This code was guided by the advice given on:
#   https://fortheknitofit.wordpress.com/2013/07/11/knitting-101-hats-decreasing-the-crown/
#
#   Author:     Evan Thomas
#   Email:      evan {ą} evanjt ! com

import turtle

# Program constants
DECREASE_STITCH_REMOVES = 2 # knit 2 together (k2tog) dereases 2 stitches to 1

# Turtle constants
CIRCLE_RADIUS = 150             # For the simulation display
DEGREES_IN_CIRCLE = 360         # Well known constant
DEFAULT_TURTLE_SCREEN_X = 400   # Screen width
DEFAULT_TURTLE_SCREEN_Y = 400   # Screen height
CIRCLE_BREAK_POINT_SIZE = 4     # Dot size indicating point of decrease

def draw_crown(circle_sizes, partitions, screensizex, screensizey, circle_deg, dot_size):
    angle_per_turn = circle_deg/partitions
    turtle.setup(screensizex, screensizey)
    t = turtle.Turtle()
    window = turtle.Screen()
    t.speed(11) # Speed 1 slowest 11 fastest

    for beanie_reduction in circle_sizes:
        t.penup()               # Shift the centre
        t.goto(0,-beanie_reduction[1])  # of circle downwards
        t.pendown()             # one full radius to fit
        for i in range(partitions):
            t.circle(beanie_reduction[1], extent=angle_per_turn)
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
def calculate_decrease_possibilities(stitches_in_round, stitches_removed_in_decrease):
    possibility_list = []
    for i in range(1,stitches_in_round):
        divisable_groups = stitches_in_round % i
        stitches_per_group = (stitches_in_round / i) - stitches_removed_in_decrease
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

def decrease_pattern(num_stitches, decrease_amount, stitches_removed_in_decrease):
    stitches_between = int(decrease_amount[1])
    decrease_count = int(decrease_amount[0])
    remaining_stitches = int(num_stitches - decrease_count)

    pattern_list = []
    for seq in range(1, decrease_amount[2]+1):
        if seq == int(decrease_amount[2]):
            print("Row {:2} | Stitch count {:3}".format(seq, num_stitches))
        else:
            print("Row {:2} | Stitch count {:3} | Stitches between decreases {:3} | Stitches after decrease {:3}".format(seq, num_stitches, int(stitches_between), int(remaining_stitches)))
        pattern_list.append((seq, num_stitches, stitches_between, remaining_stitches))
        num_stitches = remaining_stitches
        stitches_between = (num_stitches / decrease_count) - stitches_removed_in_decrease
        remaining_stitches -= decrease_count

    return pattern_list

def main():
    print(form_explanation())
    num_stitches = input("Enter number of stitches in the round: ")
    possibility_list = calculate_decrease_possibilities(int(num_stitches), DECREASE_STITCH_REMOVES)
    print_possibilities(possibility_list)

    print()
    choice = input("Choose desired pattern using the index number: ")
    decrease_amount = possibility_list[int(choice)]
    pattern_list = decrease_pattern(int(num_stitches), decrease_amount, DECREASE_STITCH_REMOVES)

    # Draw in Turtle
    draw_crown(pattern_list, decrease_amount[0], DEFAULT_TURTLE_SCREEN_X, DEFAULT_TURTLE_SCREEN_Y,
                DEGREES_IN_CIRCLE, CIRCLE_BREAK_POINT_SIZE)



if __name__ == '__main__':
    main()
