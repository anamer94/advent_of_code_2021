from math import *
import re

file = open('day_06.txt','r')
data = file.read()
file.close()

data = data.split(',')
data = [int(element) for element in data]

# puzzle 1

dict_fish = {}
for k in range (9):
    dict_fish[k] = data.count(k)

for k in range (80):
    for j in range (9):
        if j == 0:
            new = dict_fish[j]
        else:
            dict_fish[j-1] = dict_fish[j]
    dict_fish[8] = new
    dict_fish[6] += new
    
    
print(sum(list(dict_fish.values())))

# puzzle 2

dict_fish = {}
for k in range (9):
    dict_fish[k] = data.count(k)

for k in range (256):
    for j in range (9):
        if j == 0:
            new = dict_fish[j]
        else:
            dict_fish[j-1] = dict_fish[j]
    dict_fish[8] = new
    dict_fish[6] += new
    
    
print(sum(list(dict_fish.values())))
