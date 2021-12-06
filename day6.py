data = open('inputs/input_day6bis.txt').read()
sea = [int(x) for x in data.split(',')]
future = list()
days = 80

def tick():
    global sea, future
    sea = [age(x) for x in sea]
    sea.extend(future)
    future = list()

def age(fish):
    global sea, future
    if fish == 0:
        future.append(8)
        return 6
    else:
        return (fish - 1)

for x in range(days):
    tick()
    print(x)

print('Finished : ' + str(len(sea)))
