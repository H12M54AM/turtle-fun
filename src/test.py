"""
Ch 8 Question 6 - If turtle goes to border, it will turn around
---
Edward Naidoo
BSYS-2065
May 2, 2023
"""

import random
import turtle
import math

def isInScreen(w,t) -> bool:
    """
    Checks if Turtles are within the 
    screens borders
    """
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

def areColliding(t1, t2, distance) -> float:
    """
    Checks the distance between two turtles\n
    Returns Float
    """
    turtle1x, turtle1y = t1.position()
    turtle2x, turtle2y = t2.position()
    distance_between = math.sqrt((turtle1x - turtle2x)**2 + (turtle1y - turtle2y)**2)
    return distance_between < distance

t1 = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

t1.color('darkblue')

# Moves to random position
t1.penup()
t2.penup()

t1.goto(random.randint(-200, 200), random.randint(-200, 200))
t2.goto(random.randint(-200, 200), random.randint(-200, 200))

t1.pendown()
t2.pendown()

while isInScreen(wn,t1) and isInScreen(wn,t2) and not areColliding(t1, t2, 30):
    """
    Checks if turtle within the screen or colliding with 
    each other
    """
    coin1 = random.randrange(0, 2)
    coin2 = random.randrange(0, 2)

    if coin1 == 0:
        t1.left(random.randint(1, 180))
    else:
        t1.right(random.randint(1, 180))

    if coin2 == 0:
        t2.left(random.randint(1, 180))
    else:
        t2.right(random.randint(1, 180))

    t1.forward(50)
    t2.forward(50)

    if not isInScreen(wn,t1):
        t1.right(180)
        t1.forward(50)

    if not isInScreen(wn,t2):
        t2.right(180)
        t2.forward(50)

    if areColliding(t1, t2, 30):
        t1.right(180)
        t2.right(180)
        t1.forward(50)
        t2.forward(50)

turtle.mainloop()