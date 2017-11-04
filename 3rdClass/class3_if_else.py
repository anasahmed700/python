# IF & ELSE
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# IF & ELSE 5
print('HERE IS A COMMON EXAMPLE OF DECISION MAKING PROGRAM')
marks = 54
if marks >= 80:
    print('A+')
elif marks >= 70 and marks < 80:
    print("A")
elif marks >= 60 and marks < 70:
    print('B')
elif marks >= 50 and marks < 60:
    print('C')
elif marks >= 40 and marks < 50:
    print('D')
else:
    print('failed')

# USE OF in OPERATOR
print('INTRODUCING "in" OPERATOR')
topping = ['mushroom', 'union', 'cheez']
print('mushroom' in topping)
if 'mushroom' in topping:
    print('yes sir!')
else:
    print('sorry! this is not available yet.')
