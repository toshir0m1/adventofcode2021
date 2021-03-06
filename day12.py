data = open('inputs/input_day12.txt').read()
links = data.split('\n')

validPaths = list()
caves = {}
for link in links:
  points = link.split('-')
  for point in range(len(points)):
    if points[point] not in caves:
      caves[points[point]] = {}
    if point == 0:
      caves[points[0]][points[1]] = True
    else:
      caves[points[1]][points[0]] = True

def hasDoubleSmall(steps):
  for step in range(len(steps)):
    if steps[step].islower():
      others = steps.copy()
      del others[step]
      if steps[step] in others:
        return True
  return False

def searchCave(path):
  for nextCave in caves[path[-1]]:
    if nextCave == 'start':
      continue
    if nextCave in path and nextCave.islower() and hasDoubleSmall(path):
      continue
    nextStep = path.copy()
    nextStep.append(nextCave)
    if nextCave == 'end':
      validPaths.append(nextStep)
    else:
      searchCave(nextStep)

searchCave(['start'])
print(len(validPaths))
