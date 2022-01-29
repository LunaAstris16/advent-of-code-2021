testmain = str(open('testinputday5.txt', 'r').read()).splitlines()
cordinates = [ [0 for _ in range(10)] for _ in range(10)]
for x in range(len(testmain)):
    currentVaule = testmain[x].split('->')
    xvalueStart = int(currentVaule[0].split(',')[0])
    yvauleStart = int(currentVaule[0].split(',')[1])
    xvauleEnd = int(currentVaule[1].split(',')[0]) 
    yvauleEnd = int(currentVaule[1].split(',')[1])
    lengthDeltax = abs(xvauleEnd - xvalueStart)
    lengthDeltay = abs(yvauleEnd - yvauleStart)
    if lengthDeltax != 0:
        for x in range(lengthDeltax):
            print(x)
        print('new range')
print(cordinates)