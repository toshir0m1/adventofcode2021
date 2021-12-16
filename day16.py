hexData = open('inputs/input_day16bis.txt').read()
fullData = ''
for char in hexData:
  fullData += hexTable[char]

versions = list()
hexTable = {
  '0': '0000',
  '1': '0001',
  '2': '0010',
  '3': '0011',
  '4': '0100',
  '5': '0101',
  '6': '0110',
  '7': '0111',
  '8': '1000',
  '9': '1001',
  'A': '1010',
  'B': '1011',
  'C': '1100',
  'D': '1101',
  'E': '1110',
  'F': '1111'
}

def readPacket(data):
  version = int(data[:3], 2)
  versions.append(version)
  typeID = int(data[3:6], 2)
  data = data[6:]
  
  if typeID == 4:
    literalValue = ''
    while data[0] == '1':
      literalValue += data[1:5]
      data = data[5:]
    literalValue += data[1:5]
    print('Version = ' + str(version))
    print('typeID = ' + str(typeID) + ' (literal)')
    print('Literal value = ' + str(int(literalValue, 2)))
    print('-----------')

  lengthTypeID = data[0]
  data = data[1:]
  if lengthTypeID == 0:
    subpacketsLength = data[:15]
    readPacket(data[15:15+subpacketsLength])

print(readPacket(fullData))
