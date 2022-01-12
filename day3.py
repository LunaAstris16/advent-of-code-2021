testMain = [(line.strip()) for line in open("inputday3.txt", "r")]
placement = 0
x = 0
gammaRate = []
eppilionRate = []
NumberHold = 0
while x < len(testMain) + 1:
    if x < len(testMain):
        digit = str(list(map(list, str(testMain[x])))[placement])[2]
        if(digit == "1"):
            NumberHold = NumberHold + 1
        else:
            NumberHold = NumberHold - 1
        x += 1
    else:
        print(NumberHold)
        if NumberHold < 0:
            gammaRate.append(1)
        else:
            gammaRate.append(0)
        NumberHold = 0
        x = 0
        if placement > 10:
            print(gammaRate)
            x= 15
        placement = placement + 1

