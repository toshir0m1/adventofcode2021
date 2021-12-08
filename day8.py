data = open('inputs/input_day8.txt').read()
lines = data.split('\n')

uniques = 0
for line in range(len(lines)):
    splitLine = lines[line].split(' | ')
    #patterns = splitLine[0].split(' ')
    output = splitLine[1].split(' ')
    for word in output:
        lword = len(word)
        if lword < 5 or lword > 6:
            uniques += 1

print(uniques)
