import io
from pprint import pprint

name = "sample2.txt"
file = open(name,'r', encoding='utf-8')
print(file.tell())
pprint(file.read())
print(file.tell())
file.close()
