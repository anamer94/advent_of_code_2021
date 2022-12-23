file = open('day_01.txt','r')
data = file.read()
file.close()

data = data.split('\n')
if data[-1] == '':
    del data[-1]

# puzzle 1
sum_increase = 0
for k in range(len(data)-1):
    if int(data[k]) < int(data[k+1]):
        sum_increase += 1

print(sum_increase)

# puzzle 2
sum_increase = 0
for k in range(len(data)-3):
    if int(data[k]) < int(data[k+3]):
        sum_increase += 1

print(sum_increase)