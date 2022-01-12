testMain = [(line.strip()).split() for line in open("inputday2.txt", "r")]
depth = 0
aim = 0
xmovment = 0
for x in testMain:
    if "down" in x:
        aim = aim + int(x[1])
    if "forward" in x:
        xmovment = xmovment + int(x[1])
        depth = depth + (int(x[1]) * aim)
    if "up" in x:
        aim = aim - int(x[1])
overall = xmovment * depth
print(overall)