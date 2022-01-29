testmain = str(open('testinputday4', 'r').read()).splitlines()
cordinates = [ [0 for _ in range(1000)] for _ in range(1000)]
print(cordinates)
for x in range(len(testmain)):
    currentVaule = testmain[x].split('->')
