file = open('ObamaToTrump.txt','r')
line = file.read()
file.close()
# print(line)
line = line.replace('Obama','Trump')
line = line.replace('Barack','Donald')
line = line.replace('Mr.','Sir')
# print(line)
line = line.split('.')
# print(line)

fileTowrite = open('newFile.txt','w')


for l in line:
    if 'Trump' in l or 'Donald' in l:
        fileTowrite.write(l)





