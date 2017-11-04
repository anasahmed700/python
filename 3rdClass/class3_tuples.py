# TUPLE 1
dimensions = (200,50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

# TUPLE 2
print('CHANGING IN TUPLE WILL NOT OCCUR AND FOLLOWING CODE WILL WILL BE THE CAUSE OF AN ATTRIBUTE ERROR!')
# dimensions.append(60)
# print(dimensions)

# TUPLE 3
# dimensions[1] = 45
# print(dimensions)

# TUPLE 5
dimensions = tuple(range(1,11))
print(dimensions)
for d in dimensions:
    print(d)

# TUPLE 6
dimensions = (399,588)
print(dimensions)
dimensions = (355,633)
print(dimensions)

# TUPLE 7
print('YOU CAN ASSIGN A TUPLE IN ANY WAY BUT CAN NOT CHANGE IT')
dimensions = tuple(value**3 for value in range(1,11))
print(dimensions)

for dimension in dimensions:
    print(dimension)