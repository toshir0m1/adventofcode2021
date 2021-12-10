import re

data = open('inputs/input_day10bis.txt').read()
lines = data.split('\n')

outlaws = '(\(\]|\(\}|\(\>|\{\]|\{\)|\{\>|\[\)|\[\}|\[\>|\<\}|\<\)|\<\])'
minichunks = '(\(\)|\[\]|\{\}|\<\>)'
errorTable = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137
}

def trimLine(line):
  while re.search(minichunks, line) != None:
    line = re.sub(minichunks, '', line)
  return line

score = 0
incompletes = list()
for line in lines:
  original = line
  line = trimLine(line)
  suspect = re.search(outlaws, line)
  if suspect != None:
    offender = suspect.group()[1]
    score += errorTable[offender]
  else:
    incompletes.append(original)

print('Part 1 : ' + str(score))

# --- Part 2 ---

'''
def completionScore(repair):
  for char in repair:
'''
