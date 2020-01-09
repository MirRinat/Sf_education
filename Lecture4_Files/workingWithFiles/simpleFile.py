file  = open('tst.csv', 'r')
lines = file.readlines()
file.close()

oneColumnFile = []
for line in lines:
    line = line.replace('\n','')
    ogrns = line.split(';')
    for ogrn in ogrns:
        oneColumnFile.append(ogrn + '\n')
reafyFile = open('readyFile.csv', 'w')
reafyFile.writelines(oneColumnFile)



