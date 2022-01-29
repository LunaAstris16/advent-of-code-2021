testMain = [(line.strip()) for line in open("inputday3.txt", "r")]
leastCommon = [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0]
mostCommon = [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1]
y = 1
x = 0
placement = 0
while y == 1:
    if x < len(testMain):
        print(x)
        digit = str(list(map(list, str(testMain[x])))[placement])[2]
        if int(digit) == leastCommon[placement]:
            x = x
        else:
            testMain.remove(str(testMain[x]))
            x = x - 1
        x = x + 1
    else:
        print('next iteration')
        placement = placement + 1
        print(testMain)
        if len(testMain) < 2:
      #      print(testMain)
            y = 0
        x = 0