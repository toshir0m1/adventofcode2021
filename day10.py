import re

data = open('inputs/input_day10.txt').read()
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
  line = trimLine(line)
  suspect = re.search(outlaws, line)
  if suspect != None:
    offender = suspect.group()[1]
    score += errorTable[offender]
  else:
    incompletes.append(line)

print('Part 1 : ' + str(score))

# --- Part 2 ---

repairValues = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4,
}
matchings = {
  "(": ")",
  "[": "]",
  "{": "}",
  "<": ">",
}

def completionScore(repair):
  score = 0
  for char in repair:
    score = (score*5) + repairValues[char]
  return score

def middleScore(scoreList):
  scoreList.sort()
  while len(scoreList) > 1:
    scoreList.pop(-1)
    scoreList.pop(0)
  return scoreList[0]

def completeLine(line):
  completion = ''
  for char in line:
    completion = matchings[char] + completion
  return completion

scores = list()
for line in incompletes:
  ending = completeLine(line)
  scores.append(completionScore(ending))

print('Part 2 : ' + str(middleScore(scores)))
