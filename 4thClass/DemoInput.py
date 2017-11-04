# INPUT 1
print('INPUT 1')
print('TAKING INPUT FROM USER IN python')
massage = input('Enter your name here: ')
print('hello '+ massage.title() + '!')

# INPUT 2
print('INPUT 2')
#TAKING AN INTEGER INPUT
#age = input('how old are you? ')
#ge = int(age)
age = int(input('how old are you? ')) # this is an optimum way!
print(age)
if age > 18:
    print('you can apply for CNIC')
else:
    print('grow up!')

# INPUT 4
print('INPUT 4')
print('EVEN & ODD NUMBERS DETECTION')
num = int(input('select a number: '))
if num % 2 == 0:
    print('the number '+ str(num)+ ' is even')
else:
    print('the number ' + str(num)+ ' is odd')



