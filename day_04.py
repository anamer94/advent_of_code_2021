from math import *

file = open('day_04.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]

list_numero = data[0].split(',')

planche = [element.split(' ') for element in data[2:]]
planche = [[element for element in line if element != ''] for line in planche if line != ['']]


# puzzle 1
line = planche[:]
colone = []
for k in range(len(line)//5):
    for j in range(len(line[0])):
        colone.append([line[5*k][j], line[5*k+1][j], line[5*k+2][j], line[5*k+3][j], line[5*k+4][j]])


def planche_win (line, colone, list_numero):
    for number in list_numero:
        for k in range(len(line)):
            if number in line[k]:
                line[k].remove(number)
            if number in colone[k]:
                colone[k].remove(number)
        
        if [] in line:
            stop = line
            break
        
        if [] in colone:
            stop = colone
            break

    index = stop.index([]) // 5
    grid = stop[5*index: 5*index+5]
    print(sum([sum([int(element) for element in line]) for line in grid if line != []]) * int(number))
    return index, number

index, number = planche_win (line, colone, list_numero)


# puzzle 2

planche = [element.split(' ') for element in data[2:]]
planche = [[element for element in line if element != ''] for line in planche if line != ['']]

line = planche[:]
colone = []
for k in range(len(line)//5):
    for j in range(len(line[0])):
        colone.append([line[5*k][j], line[5*k+1][j], line[5*k+2][j], line[5*k+3][j], line[5*k+4][j]])

lok = 0

while (len(line) > 5 or len(colone) > 5):
    index, number = planche_win  (line, colone, list_numero)
    del line[5*index: 5*index+5]
    del colone[5*index: 5*index+5]
    lok = lok+1

index, number = planche_win  (line, colone, list_numero)