file = open("FileCSV.csv",'w')

header = "Category;Amount;Date\n"
spendings = ['Food;2000;2019-07-07\n','Food;1500;2019-08-08\n']
file.write(header)
file.writelines(spendings)
file.close()