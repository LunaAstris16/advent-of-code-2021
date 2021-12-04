a_file = open("day1inut.txt", "r")
testMain = [(line.strip()).split() for line in a_file]
a_file.close()
parseFirst = 1
parseSecound = 2
countlist = len(testMain)
runningTotal = 0
x = 0
while x < countlist:
    firstTerm = testMain[parseFirst]
    secoundTerm = testMain[parseSecound]
    if firstTerm < secoundTerm:
        runningTotal = runningTotal + 1
    parseFirst = parseFirst + 1
    parseSecound = parseSecound + 1
    if parseSecound > (countlist - 1):
        print(testMain[(countlist - 1)] , testMain[(countlist - 2)])
        if testMain[(countlist - 1)] > testMain[(countlist - 2)]:
            runningTotal = runningTotal + 1
            break
        break
    x = x + 1
print(runningTotal)
