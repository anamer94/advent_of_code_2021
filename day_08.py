from statistics import *
from math import *

file = open('day_08.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]
data = [element.split(' | ') for element in data]
data = [[element.split(' ') for element in line] for line in data]


# puzzle 1

sum_number = 0 
for line in data:
    sortie = line[1]
    for element in sortie:
        if len(element) in [2,3,4,7]:
            sum_number += 1
print(sum_number)


# puzzle 2

def interception_g_p (number_a, number_b):
    if len(number_a) > len(number_b):
        return [element for element in number_a if element not in number_b]
    return [element for element in number_b if element not in number_a]

def interception_p_g (number_a, number_b):
    if len(number_a) < len(number_b):
        return [element for element in number_a if element not in number_b]
    return [element for element in number_b if element not in number_a]

def is_in (number_a, number_b):
    for element in number_a:
        if element not in number_b:
            return False
    return True

def nombre (list_number, element):
    for number in list_number:
        if is_in (number, element) and len(number) == len(element):
            return number
    return False

dict_letter = {}
dict_letter[2] = 1
dict_letter[4] = 4
dict_letter[3] = 7
dict_letter[7] = 8

sum_number = 0 
for line in data:
    letter = {}
    number = [''] * 10
    enter = line[0]
    list_6 = []
    list_5 = []
    for element in enter:
        if len(element) == 5:
            list_5.append(element)
        elif len(element) == 6:
            list_6.append(element)
        else:
            number[dict_letter[len(element)]] = element
    
    letter['a'] = interception_g_p (number[1], number[7])[0]
    number[9] = [element for element in list_6 if is_in(number[4], element)][0]
    list_6.remove(number[9])
    number[0] = [element for element in list_6 if is_in(number[1], element)][0]
    list_6.remove(number[0])
    number[6] = list_6[0]
    
    letter['d'] = interception_p_g (number[0], number[4])[0]
    letter['c'] = interception_p_g (number[6], number[0])[0]
    letter['e'] = interception_p_g (number[9], number[0])[0]
    letter['b'] = interception_g_p (number[4], number[1]+letter['d'])[0]
    letter['f'] = [element for element in number[1] if element != letter['c']][0]
    letter['g'] = [element for element in number[8] if element not in letter][0]
    
    number[3] = [element for element in list_5 if is_in(number[1], element)][0]
    list_5.remove(number[3])
    number[2] = [element for element in list_5 if is_in(letter['c'], element)][0]
    number[5] = [element for element in list_5 if is_in(letter['b'], element)][0]     
        
    sortie = line[1]
    str_number = ''
    for element in sortie:
        str_number += str(number.index(nombre (number, element)))
    print(str_number)
    sum_number += int(str_number)

print(sum_number)
