data = open('inputs/input_day6.txt').read()
sea = [int(x) for x in data.split(',')]
days = 256
census = [0,0,0,0,0,0,0,0,0]
population = 0

for fish in sea:
    census[fish] += 1
    population += 1

def tick():
    global census, population
    for group in range(len(census)):
        if group == 0:
            babies = census[group]
        if group < 8:
            census[group] = census[group + 1]
        if group == 6:
            census[6] += babies
        if group == 8: 
            census[8] = babies
    population += babies

for x in range(days):
    tick()
    print('Day ' + str(x+1))

print('Finished : ' + str(population))
