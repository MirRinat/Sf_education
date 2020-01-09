file = open("ourFile.txt", 'r')

text = "This is first file"

lines = [ "\nthis is text from array","\nэто текст из аррея"]

asArray = file.readlines()
print(asArray)

file.close()