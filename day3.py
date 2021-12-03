data = open('inputs/input_day3.txt').read()
values = data.split('\n')

threshold = len(values) / 2
counts = list()
gamma = list()
epsilon = list()
for column in range(len(values[0])):
  counts.append(0)
  for line in range(len(values)):
    if values[line][column] == '1':
      counts[column] += 1
  gamma.append('1' if counts[column] > threshold else '0')
  epsilon.append('1' if counts[column] < threshold else '0')
gamma = ''.join(gamma)
epsilon = ''.join(epsilon)

print('Gamma = ' + str(int(gamma, 2)))
print('Epsilon = ' + str(int(epsilon, 2)))
power = int(gamma, 2) * int(epsilon, 2)
print('Power consumption = ' + str(power))

# --- Part 2 ---

oxygen = values.copy()
for column in range(len(values[0])):
  ones = 0
  threshold = len(oxygen) / 2
  for line in range(len(oxygen)):
    if oxygen[line][column] == '1':
      ones += 1
  most = '1' if ones >= threshold else '0'
  newOxygen = list()
  for o in range(len(oxygen)):
    if oxygen[o][column] == most:
      newOxygen.append(oxygen[o])
  oxygen = newOxygen
oxygen = int(oxygen[0], 2)

co2 = values.copy()
for column in range(len(values[0])):
  if len(co2) > 1:
    ones = 0
    threshold = len(co2) / 2
    for line in range(len(co2)):
      if co2[line][column] == '1':
        ones += 1
    least = '1' if ones < threshold else '0'
    newCo2 = list()
    for o in range(len(co2)):
      if co2[o][column] == least:
        newCo2.append(co2[o])
    co2 = newCo2
co2 = int(co2[0], 2)

print('Solution part 2 = ' + str(co2 * oxygen))
