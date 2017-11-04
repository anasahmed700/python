print('THIS IS 2ND CLASS OF PYTHOB PROGRAMMING IN SAYLANI TRAINING CENTER.')
print ('IN THIS CLASS WE WILL LEARN ABOUT "LISTS" IN PYTHON AND ITS DIFFERENT FUNCTIONS.')

# LIST1
print ('CREATING A LIST AND SELECTING ITS VALUES BY INDEX:')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles)
print (motorcycles[0])
print (motorcycles[-2])
mymotorcycle = motorcycles[-1]
print (mymotorcycle.upper())

# LIST2
print ('ADDING DATA IN LIST:')

motorcycles.append('harley davidson')
print ('APPEND IS AN IN MEMORY FUNCTION')
print (motorcycles)

motorcycles.insert(2, 'BMW')
print ('INSERT IS ALSO AN IN MEMORY FUNCTION AND INDEX NUMBER OF LIST IS ALSO REQUIRED')
print (motorcycles)

print ('ANOTHER WAY TO INSERT DATA IN LIST')
motorcycles[-2] = 'kawasaki'
print (motorcycles)

# LIST3
print ('DELETING DATA FROM LISTS')

print ('SIMPLE DEL STATEMENT BEFORE LIST AND INDEX# OF DATA')
del motorcycles[0]
print (motorcycles)
# LIST4
# POP FUNCTION
print('USE OF POP FANCTION')
print(motorcycles)
removedmotorcycles = []
PopMC = motorcycles.pop()
removedmotorcycles.append(PopMC)
print(motorcycles)
print(removedmotorcycles)
popmc1 = motorcycles.pop(1)
removedmotorcycles.append(popmc1)
print(motorcycles)
print(removedmotorcycles)

print('YOU CAN ALSO USE IT WITHOUT ASSIGNING ANY VARIABLE')
removedmotorcycles.append(motorcycles.pop(2))
print(motorcycles)
print(removedmotorcycles)

# LIST5
print('REMOVE FUNCTION IS USE FOR REMOVE DATA BY CALLING EXACT ELEMENT IN LIST')
removedbike = motorcycles.remove('yamaha')
removedmotorcycles.append(removedbike)
print(motorcycles)
print(removedmotorcycles)

# LIST6
print('SORT A LIST')
cars = ['subaru', 'bmw', 'toyota', 'audi']
print(cars)
cars.sort()
print(cars)
# LIST 7
print('SORT IN DESCENDING ORDER')
print(cars)
cars.sort(reverse=True)
print(cars)
# LIST 8
print('STORING SORTED LIST IN A VARIABLE')
cars = ['subaru', 'bmw', 'toyota', 'audi']
sortedlist = sorted(cars)
print(cars)
print(sortedlist)

#LIST 9
mycars = cars[1] + ' and ' + cars[3]
print(mycars)
print(cars)
cars.reverse()
print(cars)
#LIST 10
print(len(cars))
print(cars[-1])
