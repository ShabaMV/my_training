# Вариант 1
index = 0
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

while index < len(my_list):
    if(my_list[index] > 0):
        print(my_list[index])
        index += 1
    elif(my_list[index]<0):
        break
    else:
        index += 1
        continue

# Вариант 2. Как
# а) демо усвоение материала.
# б) расширить понимание цикла while
# в) применение менее типичного ветвления
# Отчетливо понимаю, что вариант 1 более предпочтителен
# с точки зрения чтения кода, но прибавление index в двух
# точках ветвления выглядит не очень, как по мне. А
# continue выходит в начало цикла безаппеляционно

while len(my_list) > 0:
    current_val = my_list.pop(0)
    if (current_val <= 0):
        if(current_val == 0):
            continue
        else:
            break
    else:
        print(current_val)

