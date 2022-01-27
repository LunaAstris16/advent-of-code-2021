testmain = str(open('inputday7.txt', 'r').read()).split(',')
#testmain = [16,1,2,0,4,2,7,1,2,14] used for testing
highest = 0
lowest = 100
iteration = 0
fule = 0
tempfule = 0
value = 1000000000000
for x in range(len(testmain)):
    if int(testmain[x]) > int(highest):
        highest = testmain[x]
    if int(testmain[x]) < int(lowest):
        lowest = testmain[x]
iteration = int(highest) - int(lowest)
while int(iteration) > 0:
    for x in range(len(testmain)):
        if int(testmain[x]) < iteration:
            #tempfule = iteration - int(testmain[x]) for part 1
            temp = iteration - int(testmain[x])
            for x in range(temp):
                tempfule = tempfule + (x + 1)
        else:
            #tempfule = int(testmain[x]) - iteration for part 1
            temp = int(testmain[x]) - iteration
            for x in range(temp):
                tempfule = tempfule + (x + 1)
        fule = fule + tempfule
        tempfule = 0
    if int(fule) < int(value):
        value = fule
        print('new value')
        print(value)
    fule = 0
    iteration = iteration - 1
print(value)
