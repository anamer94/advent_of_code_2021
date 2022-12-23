from math import *

file = open('day_03.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]

# puzzle 1

gamma_rate = ''
epsilon_rate = ''

for k in range(len(data[0])):
    sum_1 = 0
    for j in range(len(data)):
        if data[j][k] == '1':
            sum_1 +=1
    if sum_1 > (len(data)//2):
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print( int(gamma_rate, 2) * int(epsilon_rate, 2))
            
# puzzle 2

list_int = data

for k in range(len(list_int[0])):
    if len(list_int) == 2:
        if list_int[0][k] == '0':
            oxygen = list_int[1]
        else :
            oxygen = list_int[0]
        break
    
    sum_1 = 0
    list_1 = []
    for j in range(len(list_int)):
        if list_int[j][k] == '1':
            sum_1 +=1
            list_1.append(list_int[j])
            
    if sum_1 >= (len(list_int)-sum_1):
        list_int = list_1                
    else:
        list_int = [x for x in list_int if x not in list_1]
        
list_int = data

for k in range(len(list_int[0])):
    if len(list_int) == 2:
        if list_int[0][k] == '1':
            co_2 = list_int[1]
        else :
            co_2 = list_int[0]
        break
    
    sum_1 = 0
    list_1 = []
    for j in range(len(list_int)):
        if list_int[j][k] == '1':
            sum_1 +=1
            list_1.append(list_int[j])
            
    if sum_1 > len(list_int)-sum_1:
        list_int = [x for x in list_int if x not in list_1]          
    else:
        list_int = list_1    
          

print(int(oxygen,2)*int(co_2,2))