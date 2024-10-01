# возьмем определители простых чисел, ограничив диапазон
# наибольшим значением списка numbers
simple_numbers = [2, 3, 5, 7, 11, 13]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()

for i in numbers[1:15]:
    is_prime = True
    for j in simple_numbers[0:i]:
        if (i % j == 0) and (j < i):
            is_prime = False
            break

    if (is_prime == False):
        not_primes.append(i)
    else:
        primes.append(i)

print(primes)
print(not_primes)