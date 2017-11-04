# Question 13:
# Define a class with a generator which can iterate the numbers, which
# are divisible by 7, between a given range 0 and n.
# Hints:
# Consider use yield

userIn = int(input('input value of "n":'))

class abc():
    for num in range(0,userIn):
        if num % 7 == 0:
            print(num)

print(abc)