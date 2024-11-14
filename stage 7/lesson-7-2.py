import io

def custom_write(file_name, strings):
    file = open(file_name,"w", encoding='utf-8')
    text = ""
    for row in strings:
        text = text + row + "\n"
    file.write(text)
    file.close()

    file = open(file_name, "r", encoding='utf-8')
    string_num = 1
    result = {}
    while True:
        first_symbol = file.tell()
        line = file.readline()
        if not line:
            break
        position = (string_num,first_symbol)
        result[position] = line.strip()
        string_num += 1
    file.close()
    return result


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)