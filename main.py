import os
import time

directory = r'test_dz'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory)
        filetime = os.path.getatime(directory)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(directory)
        parent_dir = os.path.dirname(directory)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')
