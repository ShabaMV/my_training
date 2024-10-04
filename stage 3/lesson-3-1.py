calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(my_string):
    count_calls()
    return ((len(my_string), my_string.upper(), my_string.lower()))


def is_contains(search_request, my_strings_list):
    count_calls()
    contains = False
    for i in range(len(my_strings_list)):
        if search_request.lower() in my_strings_list[i].lower():
            contains = True
            break
    return contains


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
