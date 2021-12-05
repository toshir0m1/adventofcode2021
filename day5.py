data = open('inputs/input_day5.txt').read()
vents = data.split('\n')
scale = 1000

# create grid
grid = list()
for y in range(scale):
    row = list()
    for x in range(scale):
        row.append(0)
    grid.append(row)

def mark(x, y):
    grid[y][x] += 1

def markGrid(x1, y1, x2, y2):
    mark(x1, y1)
    if y1 == y2:
        if x1 < x2:
            for x in range(x2 - x1):
                mark(x1 + x + 1, y1)
        if x1 > x2:
            for x in range(x1 - x2):
                mark(x2 + x, y1)
        return
    if x1 == x2:
        if y1 < y2:
            for y in range(y2 - y1):
                mark(x1, y1 + y + 1)
        if y1 > y2:
            for y in range(y1 - y2):
                mark(x1, y2 + y)
        return
    if x1 < x2:
        if y1 < y2:
            for x in range(x2 - x1):
                mark(x1 + x + 1, y1 + x + 1)
        if y1 > y2:
            for x in range(x2 - x1):
                mark(x1 + x + 1, y1 - x - 1)
    if x1 > x2:
        if y1 < y2:
            for x in range(x1 - x2):
                mark(x1 - x - 1, y1 + x + 1)
        if y1 > y2:
            for x in range(x1 - x2):
                mark(x1 - x - 1, y1 - x - 1)

# mark vents on grid
for line in range(len(vents)):
    coords = vents[line].split(' -> ')
    p1 = coords[0].split(',')
    p2 = coords[1].split(',')
    x1 = int(p1[0])
    y1 = int(p1[1])
    x2 = int(p2[0])
    y2 = int(p2[1])
    markGrid(x1, y1, x2, y2)

# count overlap
overlap = 0
for y in range(scale):
    for x in range(scale):
        if grid[y][x] > 1:
            overlap += 1
print(overlap)
