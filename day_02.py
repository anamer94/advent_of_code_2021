from math import *

file = open('day_02.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]
data = [line.split(' ') for line in data]

# puzzle 1

position = [0,0]

for line in data:
    if 'forward' == line[0]:
        position[0] += int(line[1])
    if 'down' == line[0]:
        position[1] += int(line[1])
    if 'up' == line[0]:
        position[1] -= int(line[1])

print(prod(position))

# puzzle 2

position = [0,0,0]

for line in data:
    if 'forward' == line[0]:
        position[0] += int(line[1])
        position[1] += position[2]*int(line[1])
    if 'down' == line[0]:
        position[2] += int(line[1])
    if 'up' == line[0]:
        position[2] -= int(line[1])
    print(position)

print(prod(position[:2]))