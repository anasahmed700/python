# LIST 1
squares = []

for value in range(1,11):
    square = value**2
    square = square+2
    squares.append(square)

print(squares)
# list 2
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# LIST 3
print('USING "min", "max", "sum", "len" KEY WORDS')
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

minVal = min(squares)
maxVal = max(squares)
sumVal = sum(squares)
lenVal = len(squares)

print('min', minVal)
print('max', maxVal)
print('sum', sumVal)
print('len', lenVal)
print('Average', sumVal/lenVal)

# LIST 4
print('ASSIGNING A LIST WITH THE HELP OF "for loop"')
values = [val for val in range(1,11)]
values2 = [val for val in range(1,11,2)]
squares = [value**2+2 for value in range(1,11)]
print(squares)
print(values)
print(values2)

# LIST 5
print('PRINTING A LIST WITHOUT ASSIGNING IT')
print([val for val in range(1,11)])
# list Comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)
# LIST 6 SLICE 1
print('SLICING WITH LIST')
players = ['ronaldo', 'messi', 'naymar', 'benzima', 'pepe', 'kawani', 'ibrahimovic']
print(players)
fewplayers = players[1:3]
fewplayers[0] = 'marcelo'
print(fewplayers)
# LIST 7 SLICE 2
print('HERE INDEXES ARE LIKE [STARTING:ENDING:STEP OVER]')
players_a = players[4:7]
print(players_a)
# LIST 8 SLICE 3
players_b = players[:4]
print(players_b)
# LIST 9 SLICE 4
players_c = players[4:]
print(players_c)
# LIST 10 SLICE 5
print('COPYING A LIST')
players_d = players[:]
print(players_d)
# LIST 11 SLICE 6
players_e = players[1:6:2]
print(players_e)
# LIST 12 SLICE 7
players_f = players[::2]
print(players_f)
# LIST 13 SLICE 8
print('WE CAN ALSO USE SLICING IN "FOR LOOP"')
for p in players[::2]:
    print(p.title())
# LIST 14 SLICE 9
print('SLICING IS ALWAYS RUN LEFT TO RIGHT')
fewplayers1 = players[-3:]
print(fewplayers1)
# LIST 15 SLICE 10
fewplayers2 = players[-5:-3]
print(fewplayers2)
# LIST 16 SLICE 11
print('YOU  CAN SLICE IN REVERSE BY SPECIFYING INDEX IN REVERSE ORDER')
fewplayers3 = players[-3:-7:-1]
print(fewplayers3)
# LIST 17 SLICE 12
print('IF STEP OVER INDEX IS NEGATIVE SLICING WILL BE REVERSE')
print(players[::-1])
# LIST 18 SLICE 13
print('COPYING A LIST')
favplayers = players[:]
print(players)
print(favplayers)
players.append('mosses')
favplayers.append('james')
print('team selection is:')
for player in players:
    print(player)
print('but i want '+ favplayers[-1].title() + ' instead of '+ players[-1])
print(players)
print(favplayers)
