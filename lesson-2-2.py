first_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")
third_number = input("Введите третье число: ")

if first_number == second_number and second_number == third_number:
    print(3)
elif first_number == second_number or second_number == third_number or third_number == first_number:
    print(2)

# по идее достаточно else, ибо в ситуации с тремя числами исхода всего три.
# else:
#    print(0)
# Но если по-хорошему то наверное правильнее так?
elif first_number != second_number and second_number != third_number and third_number != first_number:
    print(0)
else:
    print("Нет подходящих условий")