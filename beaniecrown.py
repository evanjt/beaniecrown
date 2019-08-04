#!/usr/bin/env python3
import turtle

def draw_crown():
    t = turtle.Turtle()
    t.circle(200, extent=20)
    t.dot(5)
    t.circle(200, extent=20)
    win = turtle.Screen()
    win.exitonclick()

def form_explanation():
    explanation = "\nDecrease sections:\tThe amount of sections that the decrease will " \
                "occur at in each round.\n" \
                "\t\t\tIt also indicates the amount of stitches left in the final decrease\n" \
                "\t\t\tto join together at the end.\n" \
                "\n" \
                "Stitch per section:\tThe amount of stitches initially that will occur before a\n" \
                "\t\t\tknit 2 together (k2tog) occurs. This decrease by 1 after each row.\n" \
                "\n" \
                "Rows:\t\t\tThe amount of rows leading to the final decrease\n"
    return explanation

CIRCLE_RADIUS = 200
#num_stitches = input("Enter number of stitches in the round: ")

num_stitches = 120
possibilities = []
for i in range(1,num_stitches):
    divisable_groups = num_stitches % i
    stitches_per_group = (num_stitches / i) - i
    if (divisable_groups == 0) and (stitches_per_group >= 0):
        stitch_count = num_stitches
        count = 0
        while stitch_count > 0:
            stitch_count -= i
            count += 1
        possibilities.append((i, stitches_per_group, count))

for possibility in possibilities:
    print("Decrease sections: {:3} | Stitch per section: {:3} | Rows: {}".format(possibility[0], possibility[1], possibility[2]))

print(form_explanation())

#draw_crown()
