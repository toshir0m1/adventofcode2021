data = open('inputs/input_day11.txt').read()
grid = data.split('\n')

SIZE = 10
THRESHOLD = 9
STEPS = 100
step = 0
flashes = 0
stepFlashes = 0

flashMap = list()
for line in range(SIZE):
  grid[line] = [int(char) for char in grid[line]]
  flashMap.append([False] * SIZE)

def resetFlash():
  global flashMap
  flashMap = list()
  for line in range(SIZE):
    flashMap.append([False] * SIZE)
  
def step1():
  global grid, flashMap, flashMapOff, step, stepFlashes
  step += 1
  stepFlashes = 0
  #print('Step ' + str(step))
  for line in range(SIZE):
    for col in range(SIZE):
      if flashMap[line][col] == False:
        power(line, col)
  resetFlash()
  #show()

def power(y, x):
  global grid, flashMap
  grid[y][x] += 1
  if grid[y][x] > THRESHOLD and flashMap[y][x] == False:
    grid[y][x] = 0
    flash(y, x)

def flash(y, x):
  global flashes, flashMap, stepFlashes
  flashMap[y][x] = True
  flashes += 1
  stepFlashes += 1
  for yy in range(-1, 2):
    for xx in range(-1, 2):
      if (y + yy) >= 0 and (y + yy) < SIZE and (x + xx) >= 0 and (x + xx) < SIZE:
        if flashMap[y + yy][x + xx] == False:
          power(y + yy, x + xx)

def show():
  global grid, flashes
  for line in grid:
    print(line)
  print('flashes = ' + str(flashes))

while stepFlashes < 100:
  step1()
print(step)

