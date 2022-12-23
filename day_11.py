file = open('day_11.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]
data = [[int(letter) for letter in element] for element in data]

print(data)

def increase_all_energy (data):
    for k in range(len(data)):
        for j in range(len(data[0])):
            data[k][j] += 1
    return data

def increase_one_flash(data, xy, flash):
    move = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
    for element in move:
        x1 = xy[0] + element[0]
        y1 = xy[1] + element[1]
        if x1 >=0 and x1 < len(data) and y1 >= 0 and y1 < len(data[0]) and [x1, y1] not in flash:
            data[x1][y1] += 1
    return data

def where_flash(data):
    flash =[]
    for k in range(len(data)):
        for j in range(len(data[0])):
            if data[k][j] > 9:
                flash.append([k, j])
                data[k][j] = 0
    return flash

# puzzle 1

sum_tot = 0
for k in range(100):
    data = increase_all_energy (data)
    total_flash = where_flash(data)
    flash = total_flash[:]
    while flash != []:
        for element in flash:
            data = increase_one_flash(data, element, total_flash)
        flash = where_flash(data)
        total_flash += flash
    
    sum_tot += len(total_flash)

print(sum_tot)

# puzzle 2

sum_tot = 100 # 100 itération puzzle 1
while len(total_flash) != len(data)*len(data[0]):
    sum_tot += 1
    data = increase_all_energy (data)
    total_flash = where_flash(data)
    flash = total_flash[:]
    while flash != []:
        for element in flash:
            data = increase_one_flash(data, element, total_flash)
        flash = where_flash(data)
        total_flash += flash
    
print(sum_tot)
    