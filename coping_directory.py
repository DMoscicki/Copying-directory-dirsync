import shutil
from dirsync import sync
import sys

print(f'Введите путь к папке:')
folder_1 = str(input()) # put the path to the directory
print(f'Введите путь куда хотите скопировать:')
folder_2 = str(input())

origin_stdout = sys.stdout
sys.stdout = open('info.txt', 'w', encoding='utf-8') # write the output to file
sync(folder_1, folder_2, 'sync', verbose=True, purge=True)
sys.stdout = origin_stdout

with open('info.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        print(line, end='') # return output to console

# f = open('info.txt', 'r')
# print(f.readlines())
# f.close()
# with open('info.txt', 'r') as file:
#     for message in file:
#         print(message, end='')
# sys.stdout.close()
# file.close()
