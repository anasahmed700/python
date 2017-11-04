# CHAP 4 LOOP 1
print('NOW WE ARE GOING TO LEARN FOR_LOOP IN PYTHON')
magicians = ['alice', 'david', 'caroline']
for magician in magicians:
    print('hello Mr. '+magician)
    print(magician)
print('hello')
print(magician)
# CHAP 4 LOOP 2
names = ['anas', 'asad', 'ansar', 'jameel']
for a in names:
    print('hello! '+ a)
    print('testing!')
print('working!')

# CHAP 4 LOOP 3
print('HERE WE ARE USING "range" FUNCTION TO BUILD A LOOP')
for value in range(1,11):
    print(value)
print('end of loop')
for value in range(1,15,2):
    print(value)
print('end of loop')
for value in range(100,0,-5):
    print(value)
print('end')
# CHAP 4 LOOP 4
print(names)
for value in range(0,len(names)):
    print(value)
    print(names[value])
print('end')
print(names[value])

# CHAP 4 LOOP 5
print(names)
print('PRINTING LIST IN REVERSE ORDER')
for value in range(len(names)-1, -1, -1):
    print(value)
    print(names[value])

# CHAP 4 LOOP 6
for value in range(1,10):
    x = 23
    print('Hello',value)
print('new',value)
print('new2',x)

# CHAP 4 LOOP 7
print('ASSIGNING A LIST WITH range KEY WORD')
mylist = range(1,10)
print(mylist)
mylist2 = list(range(1,6))
print(mylist2)
mylist3 = list(range(1,20,3))
print(mylist3)