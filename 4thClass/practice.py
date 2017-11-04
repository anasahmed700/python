# PRACTICE 1 RANDOM NUMBERS
print('GENERATE LIST OF RANDOM NUMBERS WITHOUT DUPLICATION')

maxnum = int(input('enter your max number: '))
count = maxnum+1
mylist = []

from random import randint
while len(mylist) != count:
    num = randint(0, maxnum)
    if num not in mylist:
        mylist.append(num)

print(mylist)

# PRACTICE 2 PRIME NUMBERS
print('A PROGRAM WHICH INDICATES THE PRIME NUMBERS')

value = int(input('enter a prime number: '))
check = True
num = 2
while num <= value/2:
    if value % num == 0:
        check = False
        break
    num += 1
if check:
    print('this is a prime number!')
else:
    print('this is not a prime number!')

# PRACTICE 3
ranNum = randint(1,6)
guessNum = int(input('please enter a random number between 1 to 6: '))
if guessNum == ranNum:
    print('you win!')
else:
    print('you lose!')