from statistics import mode
testMain = [(line.strip()) for line in open("inputday3.txt", "r")]
num12, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = [], [], [], [], [], [], [], [], [], [], []
num11, modeall = [], []
for x in testMain:
    num1.append([int(i) for i in str(x)][0])
    num2.append([int(i) for i in str(x)][1])
    num3.append([int(i) for i in str(x)][2])
    num4.append([int(i) for i in str(x)][3])
    num5.append([int(i) for i in str(x)][4])
    num6.append([int(i) for i in str(x)][5])
    num7.append([int(i) for i in str(x)][6])
    num8.append([int(i) for i in str(x)][7])
    num9.append([int(i) for i in str(x)][8])
    num10.append([int(i) for i in str(x)][9])
    num11.append([int(i) for i in str(x)][10])
    num12.append([int(i) for i in str(x)][11])
modeall.append(mode(num1))
modeall.append(mode(num2))
modeall.append(mode(num3))
modeall.append(mode(num4))
modeall.append(mode(num5))
modeall.append(mode(num6))
modeall.append(mode(num7))
modeall.append(mode(num8))
modeall.append(mode(num9))
modeall.append(mode(num10))
modeall.append(mode(num11))
modeall.append(mode(num12))
decimal = 0
print(modeall)
for digit in modeall:
    decimal = decimal*2 + int(digit)
print(decimal)
binary = int("".join(map(str, modeall)))
binary = str(binary)
inverse = ''.join(['1' if i == '0' else '0'
                     for i in binary])
print(inverse)
decimall = 0
for digit in inverse:
    decimall = decimall*2 + int(digit)
print(decimall)
print(decimal * decimall)
