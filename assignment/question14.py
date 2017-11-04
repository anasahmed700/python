# Question 14:
# A robot moves in a plane starting from the original point (0,0). The
# robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡
# The numbers after the direction are steps. Please write a program to
# compute the distance from current position after a sequence of
# movement and original point. If the distance is a float, then just
# print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

position = {'x': 0, 'y': 0}

while True:
    line = input('> ')
    if not line:
        break

    direction, step = line.split()
    if direction == 'up':
        position['y'] += int(step)
    elif direction == 'down':
        position['y'] -= int(step)
    elif direction == 'right':
        position['x'] += int(step)
    elif direction == 'left':
        position['x'] -= int(step)

print(int(round((position['x']**2 + position['y']**2)**0.5)))