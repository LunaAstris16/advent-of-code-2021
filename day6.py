number0 = []
number1 = []
number2 = []
number3 = []
number4 = []
number5 = []
number6 = []
number7 = []
number8 = []
temp = 0
testmain = [3,3,2,1,4,1,1,2,3,1,1,2,1,2,1,1,1,1,1,1,4,1,1,5,2,1,1,2,1,1,1,3,5,1,5,5,1,1,1,1,3,1,1,3,2,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,3,3,1,1,3,1,3,1,2,1,3,1,1,4,1,2,4,4,5,1,1,1,1,1,1,4,1,5,1,1,5,1,1,3,3,1,3,2,5,2,4,1,4,1,2,4,5,1,1,5,1,1,1,4,1,1,5,2,1,1,5,1,1,1,5,1,1,1,1,1,3,1,5,3,2,1,1,2,2,1,2,1,1,5,1,1,4,5,1,4,3,1,1,1,1,1,1,5,1,1,1,5,2,1,1,1,5,1,1,1,4,4,2,1,1,1,1,1,1,1,3,1,1,4,4,1,4,1,1,5,3,1,1,1,5,2,2,4,2,1,1,3,1,5,5,1,1,1,4,1,5,1,1,1,4,3,3,3,1,3,1,5,1,4,2,1,1,5,1,1,1,5,5,1,1,2,1,1,1,3,1,1,1,2,3,1,2,2,3,1,3,1,1,4,1,1,2,1,1,1,1,3,5,1,1,2,1,1,1,4,1,1,1,1,1,2,4,1,1,5,3,1,1,1,2,2,2,1,5,1,3,5,3,1,1,4,1,1,4]
#testmain = [3,4,3,1,2]
testmain.sort()
for x in range(len(testmain)):
    if testmain[x] == 1:
        number1.append(1)
    if testmain[x] == 2:
        number2.append(1)
    if testmain[x] == 3:
        number3.append(1)
    if testmain[x] == 4:
        number4.append(1)
    if testmain[x] == 5:
        number5.append(1)
    if testmain[x] == 6:
        number6.append(1)
    if testmain[x] == 7:
        number7.append(1)
    if testmain[x] == 8:
        number8.append()

num0 = len(number0)
num1 = len(number1)
num2 = len(number2)
num3 = len(number3)
num4 = len(number4)
num5 = len(number5)
num6 = len(number6)
num7 = len(number7)
num8 = len(number8)

for x in range(256):

    tempnum = num0
    num0 = num1
    num1 = num2
    num2 = num3
    num3 = num4
    num4 = num5
    num5 = num6
    num6 = num7
    num7 = num8
    num8 = 0
    num6 += tempnum
    num8 = tempnum

testmain = [num0,num1,num2,num3,num4,num5,num6,num7,num8]
temp = 0

for x in range(len(testmain)):
    temp += testmain[x]
print(temp)
