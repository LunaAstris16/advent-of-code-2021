testmain = str(open('testinputday4', 'r').read()).splitlines()
cordinates = [[0 for _ in range(10)] for _ in range(10)]
for t in range(len(testmain)):
    currentVaule = testmain[t].split('->')
    xvalueStart = int(currentVaule[0].split(',')[0])
    yvauleStart = int(currentVaule[0].split(',')[1])
    xvauleEnd = int(currentVaule[1].split(',')[0])
    yvauleEnd = int(currentVaule[1].split(',')[1])
    lengthDeltax = abs(xvauleEnd - xvalueStart)
    lengthDeltay = abs(yvauleEnd - yvauleStart)
    if lengthDeltax != 0 and lengthDeltay != 0:
        if xvalueStart < xvauleEnd:
            if yvauleStart < yvauleEnd:
                for i in range(lengthDeltax + 1):
                    temp = cordinates[yvauleStart + i]
                    temp[xvalueStart + i] = temp[xvalueStart + i] + 1
            else:
                for p in range(lengthDeltax + 1):
                    temp = cordinates[yvauleEnd + p]
                    temp[xvalueStart + p] = temp[xvalueStart + p] + 1
        else:
            if yvauleStart < yvauleEnd:
                for u in range(lengthDeltax + 1):
                    temp = cordinates[yvauleStart + u]
                    temp[xvauleEnd + u] = temp[xvauleEnd + u] + 1
            else:
                for h in range(lengthDeltax + 1):
                    temp = cordinates[yvauleEnd + h]
                    temp[xvauleEnd + h] = temp[xvauleEnd + h] + 1
    else:
        if lengthDeltax != 0 and lengthDeltay == 0:

            if xvalueStart < xvauleEnd:
                for x in range(lengthDeltax + 1):
                    temp = cordinates[yvauleStart]
                    temp[xvalueStart + x] = temp[xvalueStart + x] + 1
            else:
                for y in range(lengthDeltax + 1) :
                    temp = cordinates[yvauleStart]
                    temp[xvauleEnd + y] = temp[xvauleEnd + y] + 1
        else:
            if yvauleStart < yvauleEnd:
                for z in range(lengthDeltay + 1):
                    temp = cordinates[yvauleStart + z]
                    temp[xvalueStart] = temp[xvalueStart] + 1
            else:
                for v in range(lengthDeltay + 1):
                    temp = cordinates[yvauleEnd + v]
                    temp[xvalueStart] = temp[xvalueStart] + 1
totalup2 = 0;
for w in range(len(cordinates)):
    for g in range(len(cordinates[w])):
        if cordinates[w][g] >= 2:
            totalup2 += 1
print(totalup2)
for w in range(len(cordinates)):
    print(cordinates[w],'line: ',w)
