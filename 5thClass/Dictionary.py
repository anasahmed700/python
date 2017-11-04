# DICTIONARY 1
# e.g; dict = {'key': 'value'}
profile = {'name': 'Anas', 'age': 24, 'email': 'anasahmed700@gmail.com'}
print(profile)
print(profile['name'])
print(profile['age'])

# DICTIONARY 2
profile = {'name': 'Anas', 'age': 24, 'email': 'anasahmed700@gmail.com', True: 'working', 5: True}
print(profile[True])
print(profile[5])

# DICTIONARY 3
print('\nCHANGING VALUE OF A KEY:')
profile['name'] = 'Anas Ahmed'
print(profile)

# DICTIONARY 4
print('\nPRINTING KEYS & VALUES IN SEPARATED LISTS')
print(profile.items())
print('USING for loop')
for key, value in profile.items():
    print('\nkey: ', key)
    print('value: ', value)

# DICTIONARY 5
print('\nPRINTING JUST VALUES FROM DICT')
print(profile.values())
print('USING for loop')
for value in profile.values():
    # print('\nkey: ', key)
    print('value: ', value)

# DICTIONARY 6
favoriteLanguage = {'anas': 'python',
                    'babar': 'C#',
                    'sameer': 'html',
                    'ali': 'python'}
print('\nSORT THE DICT FOR TEMPORARILY')
for name in sorted(favoriteLanguage.keys()):
    print(name.title()+', thank you for taking the poll.')

# DICTIONARY 7
print('\nUSING set KEYWORD TO PICK ALL UNIQUE VALUES')
for language in set(favoriteLanguage.values()):
    print(language.title())

# DICTIONARY 8
print('\nDICTIONARY DOES NOT DUPLICATE THE VALUES')
a = {'anas', 'ahmed', 'ahmed'}
print(a)

# DICTIONARY 9
user1 = {'name': 'anas', 'email': 'anasahmed700@gmail.com'}
user2 = {'name': 'ali', 'email': 'alikhan700@gmail.com'}
user3 = {'name': 'asad', 'email': 'm_asad700@gmail.com'}

users = []
users.append(user1)
users.append(user2)
users.append(user3)
print('\nAPPENDING DICTIONARY IN A LIST')
print(users)

# DICTIONARY 10
stud1 = {'name': 'anas', 'email': 'anasahmed700@gmail.com', 'languages': ['python', 'C#', 'sql']}
stud2 = {'name': 'babar', 'email': 'babarali@gmail.com', 'languages': ['C#', 'java', 'php']}
stud3 = {'name': 'ali', 'email': 'alikhan@gmail.com', 'languages': ['C', 'python', 'sql']}

students = [stud1,stud2,stud3]

print(students)

# DICTIONARY 11
print('\nNESTED for loop')
for stud in students:
    print(stud)
    for key, val in stud.items():
        print('key: ', key,' -- value: ',val)
        if key == 'languages':
            for lang in val:
                print (lang)
    print ('')

# Dictionary 12
print('\nSTORING LISTS IN A DICTIONARY:')
studentDict = {}
studentDict['stud1'] = stud1
studentDict['stud2'] = stud2
studentDict['stud3'] = stud3
print(studentDict)

# Dictionary 13
responses = {}
pollingActive = True
while pollingActive:
    name = input('\nwhat is your name? ')
    response = input('\nWhich mountain would you like to climb someday? ')

    responses[name] = response

    repeat = input('\nWould you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        pollingActive = False

print('\n--polling results--')
for name, response in responses.items():
    print(name + ' would you like to climb '+ response + '.')

# Dictionary 14
'''
Global dictionary
1) cmp(dic1, dict2)
2) len(dic)
3) str(dic)
4) type(variable)
Class function
1) dic.clear()
2) dic.copy()
3) dict.fromkeys()
4) dic.get(key, default=None)
5) dic.has_key(key)
6) dic.items()
7) dic.keys()
8) dic.values()
9) dic.setdefault(key, default=None)
10) dic.update(dic2)
'''

print('\nUSE OF DICT CLASS FUNCTIONS')

student = {'Name': 'Anas','age': 23}
print(student)
# student.clear()
# print(student)
# print(student.fromkeys())
print(student)
