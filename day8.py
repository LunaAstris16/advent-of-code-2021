testmain = [(line.split("|")[1].split(" ")) for line in open('day8.txt', 'r').read().splitlines()]
y = 0
for x in range(len(testmain)):
    templist = testmain[x]
    templist.pop(0)
    print("\n",templist, )
    for i in range(len(templist)):
        if len(templist[i]) == 4 or len(templist[i]) == 3 or len(templist[i]) == 2 or len(templist[i]) == 7:
            y +=1
            print("found the letter combo is :", templist[i] , "the length of it is :", len(templist[i]))
print(y)
# 4 3 2 7