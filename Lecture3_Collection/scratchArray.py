strangeFriends = [ "Феофан","Иннокентий","Просковья"]

text = "{} встречается с {}ом".format(strangeFriends[2],strangeFriends[0])

print(text)
print(strangeFriends)

strangeFriends.append("Савелий")

print(strangeFriends)
text = "{} встречается с {}".format(strangeFriends[2],strangeFriends[3])
print(text)
print(strangeFriends)
result = strangeFriends.pop() #возвращает значение и изменяет хранилище массива
print(result)
print(strangeFriends)