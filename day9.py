data = open('inputs/input_day9.txt').read()
lines = data.split('\n')
knownBasins = list()
newBasin = list()
basinSizes = list()

def searchBasin(line, col):
    global lines, newBasin
    if lines[line][col] == '9':
        return False
    if [line, col] in newBasin:
        return False
    for basin in knownBasins:
        if [line, col] in basin:
            return False
    newBasin.append([line, col])
    if (line > 0):
        searchBasin(line-1, col)
    if (line < (len(lines)-1)):
        searchBasin(line+1, col)
    if (col > 0):
        searchBasin(line, col-1)
    if (col < (len(lines[line])-1)):
        searchBasin(line, col+1)

for line in range(len(lines)):
    for col in range(len(lines[line])):
        searchBasin(line, col)
        if len(newBasin) > 0:
            knownBasins.append(newBasin)
            basinSizes.append(len(newBasin))
            newBasin = list()

basinSizes.sort(reverse=True)
print(basinSizes[0]*basinSizes[1]*basinSizes[2])

