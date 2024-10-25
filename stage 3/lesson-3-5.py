def get_multiplied_digits(number):
    str_number = str(number)
    first=int(str_number[0])
    if len(str_number) > 1 and int(str_number[1:]) >0:
        # добавил проверку на ноль ^^^^^
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(4020300)
print(result)

# Решил закрепить знания по рекурсии, расчетом факториала. В задание не входит.
# Для понимания работы рекурсии.

# def factorial(number):
#     if number == 1:
#         return number
#     else:
#         return number * factorial(number - 1)
#
# number = int(input("Введите значение для расчета факториала: "))
# factor = factorial(number)
# print(f"{number}! = {factor}")

def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n-1)

print(summa(5))