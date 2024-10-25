from module_4.sortfunc import bubble_sort, insertion_sort, selection_sort

data_1 = [9, 7, 4, 5, 6, 8, 1, 2, 3, 10, 12, 13, 18, 16, 11, 15, 14]
data_2 = [9, 7, 4, 5, 6, 7, 1, 2, 10, 1]
data_3 = [9, 7, 4, 5, 6, 7, 1, 2, 1, 2, 3]

print(bubble_sort(data_1))
print(bubble_sort(data_2))
print(bubble_sort(data_3))

print(insertion_sort(data_1))
print(insertion_sort(data_2))
print(insertion_sort(data_3))

print(selection_sort(data_1))
print(selection_sort(data_2))
print(selection_sort(data_3))
