def test_function():
    def inner_function():
        print("Я в области видимости test_function")
    inner_function()

# Ошибочно. Точнее выдаст ошибку, поскольку функция inner_function является вложенной в test_function и является
# локальной функцией для test_function.
inner_function()