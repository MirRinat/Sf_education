file = open("FileCSV.csv",'r')

lines = file.readlines()
#print(lines)
fileAsArray = []

for line in lines:
#    print(line)
    lineAsArray = line.split(';')
#   print(lineAsArray)
    fileAsArray.append(lineAsArray)


print(fileAsArray)


slovarSumPoCat = {}

for strokaNum in range(1, len(fileAsArray)):
    celayaStroka = fileAsArray[strokaNum]
    keyCategory = celayaStroka[0]
    valueAmount = celayaStroka[1]

    cureentSum = slovarSumPoCat.get(keyCategory,0)
    cureentSum = cureentSum + float(valueAmount)
    slovarSumPoCat[keyCategory] = cureentSum
    print(keyCategory,valueAmount)
print(slovarSumPoCat)