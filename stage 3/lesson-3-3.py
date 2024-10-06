def print_params(a=1, b='строка', c=True):
    print(a,b,c)

print_params()
print_params('zero',222, 'Nub')
print_params(1, c = False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [2.22, [4,5,6,7], 'string']
values_dict = {"c": False, "b": (1,4,5,6,6,9), "a":"string"}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3.33,'New long string']
print_params(*values_list_2,42)
