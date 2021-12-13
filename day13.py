data = open('inputs/input_day13.txt').read()
sections = data.split('\n\n')
dots = sections[0].splitlines()
foldings = sections[1].splitlines()

def fold(axis, value):
  global grid
  deadList = list()
  if axis == 'y':
    for dot in range(len(grid)):
      if grid[dot][1] > value:
        if [grid[dot][0], value - (grid[dot][1]-value)] not in grid:
          grid[dot][1] = value - (grid[dot][1]-value)
        else:
          deadList.insert(0, dot)
  if axis == 'x':
    for dot in range(len(grid)):
      if grid[dot][0] > value:
        if [value - (grid[dot][0]-value), grid[dot][1]] not in grid:
          grid[dot][0] = value - (grid[dot][0]-value)
        else:
          deadList.insert(0, dot)
  for dead in deadList:
    del grid[dead]

grid = list()
for dot in dots:
  coords = [int(x) for x in dot.split(',')]
  grid.append(coords)

for folding in foldings:
  foldingData = folding.split(' ')[2].split('=')
  fold(foldingData[0], int(foldingData[1]))
  if foldingData[0] == 'x':
    lastFoldX = int(foldingData[1])
  else:
    lastFoldY = int(foldingData[1])

display = list()
displayLine = ['.'] * lastFoldX
for i in range(lastFoldY):
  display.append(displayLine.copy())

for dot in grid:
  display[dot[1]][dot[0]] = '#'

for line in display:
  print(''.join(line))
