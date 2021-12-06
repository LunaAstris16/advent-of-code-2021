testMain = [(line.strip()).split() for line in open("inputday4.txt", "r")]
class bingoboard():
    def __init__(self, line1, line2, line3, line4, line5):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4
        self.line5 = line5
    def myfunction(self):
        print(self.line1)
        print(self.line2)
        print(self.line3)
        print(self.line4)
        print(self.line5)
counter = 0
line1temp = 0
line2temp = 0
line3temp = 0
line4temp = 0
line5temp = 0
bingoboard1 = bingoboard(0, 0, 0, 0, 0)
for x in testMain:
    counter = counter + 1
    if len(x) == 1:
        temporder = str(x).split(",")
        counter = 0
        print(temporder)
    elif x == []:
        counter = 0
        
    print(' ')
    bingoboard1.myfunction()
    if counter != 0:
        if counter == 1:
            #line1temp = ' '.join(str(e) for e in x)
            line1temp = x
            bingoboard1 = bingoboard(line1temp, line2temp, line3temp, line4temp, line5temp)
        elif counter == 2:
            #line2temp = ' '.join(str(e) for e in x)
            line2temp = x
            bingoboard1 = bingoboard(line1temp, line2temp, line3temp, line4temp, line5temp)
        elif counter == 3:
            #line3temp = ' '.join(str(e) for e in x)
            line3temp = x
            bingoboard1 = bingoboard(line1temp, line2temp, line3temp, line4temp, line5temp)
        elif counter == 4:
            #line4temp = ' '.join(str(e) for e in x)
            line4temp = x
            bingoboard1 = bingoboard(line1temp, line2temp, line3temp, line4temp, line5temp)
        elif counter == 5:
            #line5temp = ' '.join(str(e) for e in x)
            line5temp = x
            bingoboard1 = bingoboard(line1temp, line2temp, line3temp, line4temp, line5temp)
