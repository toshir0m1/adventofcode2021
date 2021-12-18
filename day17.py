'''
#XMIN = 20
#XMAX = 30
#YMAX = -5
#YMIN = -10
XMIN = 235
XMAX = 259
YMAX = -62
YMIN = -118

def drag(x):
    if x > 0:
        x -= 1
    elif x < 0:
        x += 1
    return x
'''

# found part 1 result by trying around in console mode :
# print('Max Y = ' + str(findVelY(117)))
def findVelY(startingVelocity):
    positions = [0]
    velY = startingVelocity
    while positions[-1] > YMAX:
        positions.append(positions[-1]+velY)
        print(positions[-1])
        velY -= 1
    if positions[-1] >= YMIN:
        return max(positions)
    return False

'''
def findVelX():
    candidates = list()
    for candidate in range(XMAX//2):
        nextCandidate = False
        posX = 0
        velX = candidate
        while nextCandidate == False:
            posX += velX
            velX = drag(velX)
            if velX == 0:
                if posX >= XMIN and posX <= XMAX:
                    candidates.append(candidate)
                nextCandidate = True
    return candidates

#possibleX = findVelX()
#print(possibleX)
'''
