data = open('inputs/input_day8.txt').read()
lines = data.split('\n')

totalSum = 0
for line in range(len(lines)):
    decodingTable = {}
    group5 = list()
    group6 = list()
    splitLine = lines[line].split(' | ')
    patterns = splitLine[0].split(' ')
    output = splitLine[1].split(' ')
    for word in patterns:
        word = ''.join(sorted(word))
        if len(word) == 2:
            decodingTable['1'] = word
        if len(word) == 3:
            decodingTable['7'] = word
        if len(word) == 4:
            decodingTable['4'] = word
        if len(word) == 7:
            decodingTable['8'] = word
        if len(word) == 5:
            group5.append(word)
        if len(word) == 6:
            group6.append(word)
    for word in range(len(group5)):
        match = 0
        for char in decodingTable['1']:
            if char in group5[word]:
                match += 1
        if match == 2:
            decodingTable['3'] = group5.pop(word)
            break
    for word in range(len(group5)):
        match = 0
        for char in decodingTable['4']:
            if char in group5[word]:
                match += 1
        if match == 2:
            decodingTable['2'] = group5[word]
        if match == 3:
            decodingTable['5'] = group5[word]
    for word in range(len(group6)):
        match = 0
        for char in decodingTable['7']:
            if char in group6[word]:
                match += 1
        if match == 2:
            decodingTable['6'] = group6.pop(word)
            break
    for word in range(len(group6)):
        for char in decodingTable['4']:
            if len(group6) > word and char not in group6[word]:
                decodingTable['0'] = group6.pop(word)
                decodingTable['9'] = group6.pop(0)
                break
    reverseTable = {}
    for entry in decodingTable:
        reverseTable[decodingTable[entry]] = entry
    lineValue = ''
    for digit in output:
        lineValue += reverseTable[''.join(sorted(digit))]
    totalSum += int(lineValue)

print(str(totalSum))
