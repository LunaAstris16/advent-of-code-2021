a_file = open("inputday2.txt", "r")
testMain = [(line.strip()).split() for line in a_file]
a_file.close()
toataly = 0
totalx = 0
#testMain.sort()
for x in testMain:
    if "down" in x:
        y = x[1]
        z = int(y)
        toataly = toataly + z
    if "forward" in x:
        a = x[1]
        b = int(a)
        toataly = toataly * b
        totalx = totalx + b
    if "up" in x:
        c = x[1]
        d = int(c)
        toataly = toataly - d
print(totalx)
print(toataly)
overall = totalx * toataly
print(overall)