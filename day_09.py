from statistics import *
from math import *

file = open('day_09.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]
data = [[int(letter) for letter in element] for element in data]

# puzzle 1
list_risk = []
sum_risk = 0
for k in range(len(data)):
    for j in range(len(data[0])):
        min = True
        if k != 0:
            if data[k-1][j]<=data[k][j]:
                min = False
        if k != len(data)-1:
            if data[k+1][j]<=data[k][j]:
                min = False
        if j != 0:
            if data[k][j-1]<=data[k][j]:
                min = False
        if j != len(data[0])-1:
            if data[k][j+1]<=data[k][j]:
                min = False
        if min == True:
            sum_risk += data[k][j] + 1
            list_risk.append([k,j])
print(sum_risk)

# puzzle 2

def find_basin(observer, data, x,y):
    print('new')
    list_a_observer = [[x,y]]
    observer.append([x,y])
    bassin = 1
    while list_a_observer != []:
        print(list_a_observer)
        k = list_a_observer[0][0]
        j = list_a_observer[0][1]
        del list_a_observer[0]
        
        if k != 0:
            if data[k-1][j]!=9 and [k-1,j] not in observer:
                list_a_observer.append([k-1,j])
                observer.append([k-1,j])
                bassin += 1
        if k != len(data)-1:
            if data[k+1][j]!=9 and [k+1,j] not in observer:
                list_a_observer.append([k+1,j])
                observer.append([k+1,j])
                bassin += 1
        if j != 0:
            if data[k][j-1]!=9 and [k,j-1] not in observer:
                list_a_observer.append([k,j-1])
                observer.append([k,j-1])
                bassin += 1
        if j != len(data[0])-1:
            if data[k][j+1]!=9 and [k,j+1] not in observer:
                list_a_observer.append([k,j+1])
                observer.append([k,j+1])
                bassin += 1
    return observer, bassin


observer = []
list_basin = []

for k in range(len(data)):
    for j in range(len(data[0])):
        if [k,j] not in observer and data[k][j] != 9:
            observer, basin = find_basin(observer, data, k,j)
            list_basin.append(basin)
            print('bassin')

print(prod(sorted(list_basin, reverse=True)[:3]))
