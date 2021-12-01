input = open('inputs/input_day1.txt').read()

values = input.split('\n')
increases = 0
for i in range(len(values)):
  if i > 0:
    diff = int(values[i]) - int(values[i - 1])
    if diff > 0:
      increases += 1
print('Part 1 : ' + str(increases))

# --- part 2 ---

increases = 0
sums = list()
for i in range(len(values)):
  if i > 1:
    sum = int(values[i]) + int(values[i - 1]) + int(values[i - 2])
    sums.append(sum)
for s in range(len(sums)):
  if s > 0:
    diff = int(sums[s]) - int(sums[s - 1])
    if diff > 0:
      increases += 1
print('Part 2 : ' + str(increases))
