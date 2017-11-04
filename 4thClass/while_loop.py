# WHILE 1
print('WHILE 1')
num = 1
while num <= 5:
    print(num)
    num += 1
print('ending of loop!')
print(num)

# WHILE 2
print('WHILE 2')
current_num = int(input('enter your number: '))
num = 0
while num < current_num:
    print(num)
    num += 1
print('final num is', num)

# WHILE 3 use of break
print('WHILE 3')
print('BREAKING A WHILE LOOP')
input_num = int(input('enter a number: '))
num = 0
while num < input_num:
    num +=1
    if num > 9 and num <16:
        break
    print(num)
print('loop is broken')
print('final num is ',num)
# WHILE 4 USE OF CONTINUE
print('CONTINUE A WHILE LOOP')
input_num = int(input('enter a number: '))
num = 0
while num < input_num:
    num +=1
    if num > 9 and num <= 15:
        continue
    print(num)
print('loop was broken on num "9" and continue from "16"')
print('final num is ',num)
