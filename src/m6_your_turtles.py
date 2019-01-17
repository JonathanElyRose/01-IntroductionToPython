"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Jonathan Ely.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
import math

window = rg.TurtleWindow()
window.delay(1)

circle = rg.SimpleTurtle()
circle.speed = 500000
circle.pen = rg.Pen('black', 1)

circle.pen_down()
circle.forward(1)
for g in range(1):
    circle.left(5)
    circle.forward(1)

square = rg.SimpleTurtle()
square.speed = 500000
square.pen = rg.Pen('red', 1)
colors = ['red', 'orange', 'yellow','green','blue','purple']

for k in range(300):
    for h in range(5):
        for g in range(6):
            square.pen = rg.Pen(colors[g], 1)
            square.forward(3)
    square.left(90)
    square.pen_up()
    square.forward(k)
    square.pen_down()




