my_dict = {"first": 1, "second": 2}
print(my_dict)
print(my_dict["first"])
print(my_dict.get("third","Элемент не найден"))
my_dict.update({"third":3,"forth":4})

del_elem = my_dict.pop("first");
print(f"Был удален элемент словаря со значением {del_elem}")
print(my_dict)

my_set = {1, 1, 1, 2, 3, 4, 522, 5, 436, 23, 1,True, "More", "One more", "One more", ("asasa",True)}
print(my_set)
# Добавляем элементы множества поочередно
my_set.add(16)
my_set.add(17)
print(my_set)

# Другой вариант добавления элементов в множество путем слияния
my_new_set = {212,523,5}
my_set = my_set.union(my_new_set)
print(my_set)

my_set.remove(1)
print(my_set)
