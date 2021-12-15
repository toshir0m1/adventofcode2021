data = open('inputs/input_day15.txt').read()
maze = data.splitlines()

for row in range(len(maze)):
  maze[row] = [int(x) for x in list(maze[row])]

MAX_X = len(maze[0]) - 1
MAX_Y = len(maze) - 1
minRisk = 999999999999
aborts = 0
paths = 0

def findPath(posX, posY, risk):
  global minRisk, aborts, paths
  if risk > minRisk:
    aborts += 1
    return
  if posX == MAX_X and posY == MAX_Y:
    if risk < minRisk:
      paths += 1
      print(paths)
      print(risk)
      print(aborts)
      print('---')
      minRisk = risk
    return
  if posX < MAX_X:
    findPath(posX+1, posY, risk + maze[posY][posX+1])
  if posY < MAX_Y:
    findPath(posX, posY+1, risk + maze[posY+1][posX])

findPath(0, 0, 0)
print(minRisk)
