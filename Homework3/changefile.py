readfile = open('Mkt_data_test.txt','r')

lines = readfile.readlines()
readfile.close()
headerline = 'Time;Bid\Ask;Price;Volume\n'
newArray = []
for line in lines:
    line = line.strip()
    line = line.replace('\n', '')
    if '=' in line or len(line) == 0:
        continue
    line = line.replace('1900-01-01 ', '')
    line = line.replace('00:','')
    line = line.split(' ; ')
    line[0] = line[0][0:7]
    if line[1] == ' 1 ':
        line[1] = 'Ask'
    else:
        line[1] = 'Bid'
    line[3] = line[3][0:len(line[3]) - 2]
    newArray.append(line)

newFile = open('newFile.csv','w')
newFile.write(headerline)
for new in newArray:
    newFile.writelines(';'.join(new) + '\n')

