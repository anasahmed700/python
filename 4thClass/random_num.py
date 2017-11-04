# boolean statement
play = 'yes'
print(play is 'yes')

# RANDOM 1
print('GENERATING A RANDOM NUMBER LIKE A DICE')
from random import randint
RanNum = randint(1,6)
print(RanNum)

# RANDOM 2
print('RANDOM 2')
print('GENERATING A LIST OF RANDOM NUMBERS')
mylist = []
for val in range(0,10):
    num = randint(1,15)
    mylist.append(num)
    print(num)
print('ENDING OF LOOP!')
print(mylist)


