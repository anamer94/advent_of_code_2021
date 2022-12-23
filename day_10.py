file = open('day_10.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]
data = [[letter for letter in element] for element in data]

print(data)

# puzzle 1

dict_syn = {}
dict_syn['('] = ')'
dict_syn['['] = ']'
dict_syn['{'] = '}'
dict_syn['<'] = '>'

dict_point = {}
dict_point[')'] = 3
dict_point[']'] = 57
dict_point['}'] = 1197
dict_point['>'] = 25137

sum_tot = 0
new_data = []
for line in data:
    bol =  1
    syntaxe_a_fermer = []
    for element in line :
        if element in ['(', '[', '{', '<']:
            syntaxe_a_fermer.append(element)
        else :
            if dict_syn[syntaxe_a_fermer[-1]] != element:
                sum_tot += dict_point[element]
                bol = 0
                break
            else:
                del syntaxe_a_fermer[-1]
    if bol == 1:
        new_data.append(line)
               

print(sum_tot)

#puzzle 2

dict_point = {}
dict_point['('] = 1
dict_point['['] = 2
dict_point['{'] = 3
dict_point['<'] = 4

print(new_data)

list_sum =[]
for line in new_data:
    bol =  1
    syntaxe_a_fermer = []
    for element in line :
        if element in ['(', '[', '{', '<']:
            syntaxe_a_fermer.append(element)
        else :
            del syntaxe_a_fermer[-1]
    syntaxe_a_fermer.reverse()
    sum_tot = 0
    if syntaxe_a_fermer != []:
        for element in syntaxe_a_fermer:
            sum_tot = sum_tot*5 + dict_point[element]
    list_sum.append(sum_tot)
    
list_sum.sort()
print(list_sum)
print(list_sum[len(list_sum)//2])

#490493