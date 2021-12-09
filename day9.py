data = open('inputs/input_day9.txt').read()
lines = data.split('\n')
lowPoints = list()

def isLow(line, col):
    global lines
    x = int(lines[line][col])
    up = int(lines[line-1][col]) if line > 0 else 9
    down = int(lines[line+1][col]) if line < (len(lines)-1) else 9
    left = int(lines[line][col-1]) if col > 0 else 9
    right = int(lines[line][col+1]) if col < (len(lines[line])-1) else 9
    return x < up and x < down and x < left and x < right

for line in range(len(lines)):
    for col in range(len(lines[line])):
        if isLow(line, col):
            lowPoints.append(int(lines[line][col]))

print(sum(lowPoints) + len(lowPoints))
