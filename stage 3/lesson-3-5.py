def get_multiplied_digits(number):
    str_number = str(number)
    first=int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)

# Решил закрепить знания по рекурсии, расчетом факториала. В задание не входит.
# Для понимания работы рекурсии.

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)

number = int(input("Введите значение для расчета факториала: "))
factor = factorial(number)
print(f"{number}! = {factor}")