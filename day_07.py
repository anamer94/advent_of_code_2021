from statistics import *
from math import *

file = open('day_07.txt','r')
data = file.read()
file.close()

data = data.split(',')
data = [int(element) for element in data]

# puzzle 1 

data = sorted(data)
median_crabs = median(data)

sum_fuel = 0
for element in data:
    sum_fuel += int(abs(element - median_crabs))

print(sum_fuel)

# puzzle 2

data = sorted(data)
mean_crabs = floor(mean(data))

sum_fuel_p = 0
sum_fuel_m = 0
for element in data:
    steps = abs(element - mean_crabs)
    for k in range (steps):
        sum_fuel_p += k+1
        sum_fuel_m += k+1
    sum_fuel_p += steps + 1

print(min(sum_fuel_p, sum_fuel_m))
