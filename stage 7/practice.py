# import io
# from pprint import pprint
#
# name = "sample2.txt"
# file = open(name,'r', encoding='utf-8')
# print(file.tell())
# pprint(file.read())
# print(file.tell())
# file.close()

import os
from os import listdir

# print("Текущая директория: ",os.getcwd())
# if os.path.exists('second'):
#     os.chdir('second')
# else:
#     os.mkdir('second')
#     os.chdir('second')

print("Текущая директория: ", os.getcwd())
# os.makedirs(r'third\forth')
print(os.listdir())
file  = [f for f in os.listdir() if os.path.isfile(f)]
dirs  = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)
print(os.stat(file[5]).st_size)