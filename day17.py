XMIN = 235
XMAX = 259
YMAX = -62
YMIN = -118

def findVelY(velocityX):
    velocities = list()
    for candidate in range(YMIN, 250):
        nextCandidate = False
        velY = candidate
        velX = velocityX
        posX = 0
        posY = 0
        while posY >= YMIN:
            posY += velY
            velY -= 1
            posX += velX
            velX = drag(velX)
            if posX >= XMIN and posX <= XMAX and posY <= YMAX and posY >= YMIN:
                velocities.append([velocityX, candidate])
                nextCandidate = True
                break
        if nextCandidate:
            continue
    return velocities

def drag(x):
    if x > 0:
        x -= 1
    elif x < 0:
        x += 1
    return x

def findVelX():
    candidates = list()
    for candidate in range(XMAX+1):
        nextCandidate = False
        posX = 0
        velX = candidate
        while nextCandidate == False and velX != 0:
            posX += velX
            velX = drag(velX)
            if posX >= XMIN and posX <= XMAX:
                candidates.append(candidate)
                nextCandidate = True
    return candidates

possibleX = findVelX()

hits = list()
for x in possibleX:
    hitsForX = findVelY(x)
    hits.extend(hitsForX)

print(len(hits))

