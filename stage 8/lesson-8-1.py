def add_everything_up(a,b):
    try:
        return(a + b)
    except TypeError as tperr:
        return(str(a) + str(b))
        # тут можно было бы отработать tperr

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
# вот в этом месте возникает вопрос ^^^ почему-то по результату сложения
# к результату приклеивается 0.000000000002 float + int должны же
# нормально складываться?
