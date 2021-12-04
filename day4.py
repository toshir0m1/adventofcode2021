data = open('inputs/input_day4.txt').read()
sections = data.split('\n\n')

stack = sections.pop(0).split(',')
stack = [int(x) for x in stack]

boards = list()
scores = list()
for s in range(len(sections)):
  lines = sections[s].split('\n')
  board = list()
  score = list()
  for line in range(len(lines)):
    lineScores = [False, False, False, False, False]
    score.append(lineScores)
    lineNumbers = list()
    lineNumbers.append(int(lines[line][:2]))
    lineNumbers.append(int(lines[line][3:5]))
    lineNumbers.append(int(lines[line][6:8]))
    lineNumbers.append(int(lines[line][9:11]))
    lineNumbers.append(int(lines[line][12:]))
    board.append(lineNumbers)
  boards.append(board)
  scores.append(score)

def updateScore(board, x, y):
  scores[board][y][x] = True
  #viewB(board)
  #viewS(board)

def checkBoard(board, n):
  for line in range(len(boards[board])):
    for slot in range(len(boards[board][line])):
      if boards[board][line][slot] == n:
        updateScore(board, slot, line)
        if checkVictory(board):
          return True
  return False

def checkVictory(board):
  for y in range(len(boards[board])):
    if scores[board][y] == [True, True, True, True, True]:
      return True
  for x in range(len(boards[board][0])):
    if (scores[board][0][x] == True and
        scores[board][1][x] == True and
        scores[board][2][x] == True and
        scores[board][3][x] == True and
        scores[board][4][x] == True):
      return True
  return False

def viewB(board):
  for b in range(len(boards[board])):
    print(boards[board][b])

def viewS(board):
  for b in range(len(scores[board])):
    print(scores[board][b])

def countUnmarked(board):
  sum = 0
  for y in range(len(boards[board])):
    for x in range(len(boards[board][y])):
      if scores[board][y][x] == False:
        sum += boards[board][y][x]
  return sum

over = False
for draw in range(len(stack)):
  print('Next number : ' + str(stack[draw]))
  for candidate in range(len(boards)):
    check = checkBoard(candidate, stack[draw])
    if check == True:
      print('Board number ' + str(candidate) + ' HAS WON!')
      viewB(candidate)
      viewS(candidate)
      unmarked = countUnmarked(candidate)
      solution = unmarked * stack[draw]
      print('Solution = (sum of unmarked)(' + str(unmarked) + ') * (last number called)(' + str(stack[draw]) + ') = ' + str(solution))
      over = True
      break
    #else:
      #print('Board number ' + str(candidate) + ' has not won yet')
  if over == True:
    break
