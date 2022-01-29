testMain = [(line.strip()) for line in open("inputday1.txt", "r")]
count = 0
for x in range(len(testMain)-3) :
    if int(testMain[x]) + int(testMain[x + 1]) + int(testMain[x + 2]) < int(testMain[x + 1]) + int(testMain[x + 2]) + int(testMain[x + 3]):
        count += 1
print(count)