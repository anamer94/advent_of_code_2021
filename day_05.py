from math import *
import re

file = open('day_05.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]
    
data = [re.split(',| -> ', element) for element in data]

print(data)

# puzzle 1

dict_position = {}

for line in data:
    if int(line[0]) == int(line[2]):
        for k in range (abs(int(line[1])-int(line[3]))+1):
            v_min = str(min(int(line[1]), int(line[3])) + k)
            v_const = line[0]
            if v_const + ',' + v_min in dict_position.keys():
                dict_position[v_const + ',' + v_min] += 1
            else:
                dict_position[v_const + ',' + v_min] = 1
    elif int(line[1]) == int(line[3]):
        for k in range (abs(int(line[0])-int(line[2]))+1):
            v_min = str(min(int(line[0]), int(line[2])) + k)
            v_const = line[1]
            if v_min + ',' + v_const in dict_position.keys():
                dict_position[v_min + ',' + v_const] += 1
            else:
                dict_position[v_min + ',' + v_const] = 1


value = list(dict_position.values())
value = [element for element in value if element >= 2]
print(len(value))

# puzzle 1

dict_position = {}

for line in data:
    if int(line[0]) == int(line[2]):
        for k in range (abs(int(line[1])-int(line[3]))+1):
            v_min = str(min(int(line[1]), int(line[3])) + k)
            v_const = line[0]
            if v_const + ',' + v_min in dict_position.keys():
                dict_position[v_const + ',' + v_min] += 1
            else:
                dict_position[v_const + ',' + v_min] = 1
    elif int(line[1]) == int(line[3]):
        for k in range (abs(int(line[0])-int(line[2]))+1):
            v_min = str(min(int(line[0]), int(line[2])) + k)
            v_const = line[1]
            if v_min + ',' + v_const in dict_position.keys():
                dict_position[v_min + ',' + v_const] += 1
            else:
                dict_position[v_min + ',' + v_const] = 1
    else:
        for k in range (abs(int(line[0])-int(line[2]))+1):
            v_min = str(int(line[0]) + k * int(copysign(1,int(line[2]) - int(line[0]))))
            v_const = str(int(line[1]) + k * int(copysign(1,int(line[3]) - int(line[1]))))
            if v_min + ',' + v_const in dict_position.keys():
                dict_position[v_min + ',' + v_const] += 1
            else:
                dict_position[v_min + ',' + v_const] = 1


value = list(dict_position.values())
value = [element for element in value if element >= 2]
print(len(value))
