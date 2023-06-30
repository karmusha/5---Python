# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

mylist = [1, 2, 1, 1 ,3, 2, 4, 4, 5, 2, 2]
COUNT_NUMBER = 3

for item in mylist:
    if mylist.count(item) == COUNT_NUMBER:
        for _ in range(COUNT_NUMBER):
            mylist.remove(item)

print(mylist)
