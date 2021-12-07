data = open('inputs/input_day7.txt').read()
crabs = [int(x) for x in data.split(',')]
minFuel = 999999999999999
bestPos = False

def calculate(d):
    total = 0
    for n in range(d + 1):
        total += n
    return total

for pos in range(min(crabs), max(crabs)):
    fuel = 0
    for crab in range(len(crabs)):
        distance = abs(pos - crabs[crab])
        fuel += calculate(distance)
    if fuel < minFuel:
        minFuel = fuel
        bestPos = pos
        
print('Least fuel : ' + str(minFuel))
print('Best position : ' + str(bestPos))
