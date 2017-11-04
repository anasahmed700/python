# FunCtion 1
print('DEFINING A FUNCTION TO GREET A USER')
name = 'anas'
def greetUser():
    print('hello world')
    print('this is me' + name.title())
greetUser()

# FUNCTION 2
print('\nDEFINING A FUNCTION TO MAKE A CUP OF TEA')
def makeTea():
    print('take required amount of boiled water')
    print('add 1 tea bag')
    print('add 2 spoon sugar')
    print('add milk')
    print('bring it to me')

makeTea()
makeTea()

# FUNCTION 3
print('\nDEFINING FUNCTIONS WITH PARAMETERS')
def teaMaker(noOFCup, sugar):
    print('make tea')
    print('prepare '+ str(noOFCup) +' cups of tea')
    print('add '+ str(sugar) +' spoons of sugar')
    print('put 1 tea bag in each cup')
    print('bring tea here')

teaMaker(3,2)

# FUNCTION 4
print('\nWE CAN ALSO CALL FUNCTION WITH PARAMETERS & THEIR VALUES')

teaMaker(sugar=1, noOFCup=3)

# FUNCTION 5
teaMaker(2, sugar=3)

# FUNCTION 6
print('\nDEFINING PARAMETERS WITH DEFAULT VALUES')

def teaDefault(noOfCups, sugar=2):
    print("Make Tea")
    print("Preparing "+str(noOfCups)+" cups of Tea")
    print("Adding sugar "+str(sugar)+" spoon")
    print("Add 1 Tea bag")
    print("Fill cup")

teaDefault(4)
teaDefault(1,1)
teaDefault(noOfCups=5)

# FUNTIONS 7
print('\nSTORING FUNCTION IN VARIABLE')

collect = teaDefault(4)
print(collect)

# FUNCTIONS 8
print('\nADDITION OF OPTIONAL THING')

def teaDefault(noOfCups, sugar=2, elichi=''):
    print("Make Tea")
    print("Preparing "+str(noOfCups)+" cups of Tea")
    print("Adding sugar "+str(sugar)+" spoon")
    if elichi == 'yes':
        print('adding elichi')
    print("Add 1 Tea bag")
    print("Fill cup")
    return 'bring ' +str(noOfCups)+' cups here!'

collectTea = teaDefault(3,elichi='yes')
print(collectTea)

# FUNTIONS 9
print('\nSTORING PARAMETERS IN DICTIONARY')

def teaDefault(noOfCups, sugar=2, elichi=''):
    print("Make Tea")
    print("Preparing "+str(noOfCups)+" cups of Tea")
    print("Adding sugar "+str(sugar)+" spoon")
    if elichi == 'yes':
        print('adding elichi')
    print("Add 1 Tea bag")
    print("Fill cup")
    return {'cups': noOfCups, 'sugar': sugar, 'elichi': elichi}

collectTea = teaDefault(3,elichi='yes')
print(collectTea)


# FUCTIONS 19
print('\nUSING OF LIST')

def fayyaz(itemList):
    for i in itemList:
        print('buying '+i)

myItems = ['biryani', 'burger', 'lassi']
fayyaz(myItems)


# FUNTIONS 11
print('\nREPLACING AN ITEM FROM LIST')

def fayyaz(itemList):
    itemList[0] = 'pulao'
    for i in itemList:
        print('buying '+ i)

myItems = ['biryani', 'burger', 'lassi']
print(myItems)
fayyaz(myItems[:])
print(myItems)

# FUNTIONS 12
print('\nDEFINING A FUNCTION THAT CAN INPUT DATA IN LIST')
def fayyaz(*itemList):
    # itemList[0] = 'pulao'
    for i in itemList:
        print('buying '+ i)

fayyaz('biryani', 'burger', 'lassi')

# FUNCTIONS 13
print('\nUSING PARAMETER AS ITEM "i" AND QUANTITY "j"')

def fayyaz(**itemList):
    for i,j in itemList.items():
        print('buying '+ i)
        print(j)

fayyaz(rice= 3, coke= 1)