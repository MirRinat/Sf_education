dict = {"Vlas":29, "Petr":31}
print(dict["Vlas"])
dict["Olga"] = 22
print(dict)

spqrArray = ["Senatus","Populus","Que","Romanus"]
abbreviation = ["R", "Q", "P", "S"]

for abbr , name in abbreviation ,spqrArray:
    spqrDict = {abbreviation[abbr]: spqrArray[name]}

print(spqrDict)