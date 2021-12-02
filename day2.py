donnees = open('inputs/input_day2.txt').read()

horizontal = 0
depth = 0
values = donnees.split('\n')
for i in range(len(values)):
  order = values[i].split(' ')
  direction = order[0]
  distance = order[1]

  if direction == 'forward':
    horizontal += int(distance)

  if direction == 'up':
    depth -= int(distance)
    
  if direction == 'down':
    depth += int(distance)

print('Horizontal = ' + str(horizontal))
print('Depth = ' + str(depth))
solution = horizontal * depth
print('Solution part 1 = ' + str(solution))

# --- Part 2 ---

horizontal = 0
depth = 0
aim = 0
for i in range(len(values)):
  order = values[i].split(' ')
  direction = order[0]
  howmuch = order[1]

  if direction == 'up':
    aim -= int(howmuch)
    
  if direction == 'down':
    aim += int(howmuch)

  if direction == 'forward':
    horizontal += int(howmuch)
    depth += (aim * int(howmuch))

print('Horizontal = ' + str(horizontal))
print('Depth = ' + str(depth))
print('Aim = ' + str(aim))
solution = horizontal * depth
print('Solution part 2 = ' + str(solution))
