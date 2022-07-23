import random

def randNum():
    return random.random()

# You are given a function that returns a random number between 0 and 1

# Now calculate Pi

# ----------- Here is my solution --------------------

# This is how many times the loop will run
# the bigger this number, the more acurate number of Pi
n = 1000000

# Variables counting points inside the circle vs outside
inside = 0
points = 0

# Simple loop
i = 0
while i < n:
    i +=1

    # Using the random function to make a point on a 1 by 1 chart
    x = randNum()
    y = randNum()

    # Using A^2 + B^2 = C^2 
    # C will be used to determain if the given point is inside or outside a cirlce with a radius of 1
    A = x*x
    B = y*y
    C = A+B
    if (C <= 1):
        # if the point is inside the circle add to the inside variable
        inside += 1

    # all of the points will be counted
    points +=1

# area of a circle = (inside/points) * 4
# area of a circle = Pi * (r * r)
# if r = 1 then circle = Pi * 1 = Pi
# 4(inside/points)=Pi

area = inside/points
pi = area * 4

print(pi)