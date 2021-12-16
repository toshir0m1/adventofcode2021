data = open('inputs/input_day14bis.txt').read()
sections = data.split('\n\n')
polymerSize = len(sections[0])
print(polymerSize)

def step(n):
  global polymerSize
  return n + (n-1)

STEPS = 40
for x in range(STEPS):
  polymerSize = step(polymerSize)
  print(polymerSize)

'''
rulesLines = sections[1].splitlines()

inventory = {}
for p in polymer:
  if p not in inventory:
    inventory[p] = 0

rules = {}
for line in rulesLines:
  parts = line.split(' -> ')
  rules[parts[0]] = parts[1]
  if parts[1] not in inventory:
    inventory[parts[1]] = 0

def evolve():
  global rules, polymer, inventory
  for pos in range(len(polymer)-2, -1, -1):
    pair = polymer[pos] + polymer[pos+1]
    if pair in rules:
      polymer.insert(pos+1, rules[pair])

STEPS = 15
for step in range(STEPS):
  print(step)
  evolve()
nMin = 99999999
nMax = -1
for item in inventory:
  n = polymer.count(item)
  inventory[item] = n
  if n > nMax:
    nMax = n
  if n < nMin:
    nMin = n
print(nMax-nMin)
'''
