# Базы данных
# Архиватор или структурированное хранение и передача
# Архиватор ZIP
# ЗАпишем все созданные JSON в архив
from zipfile import ZipFile
import os

# os.chdir('data')
# file_list = os.listdir()
# with ZipFile('jsons.zip', 'w') as myzip:
#     for file in file_list:
#         myzip.write(file)
#         os.remove(file)
# os.chdir('..')

with ZipFile('data/jsons.zip') as z:
    print(z.namelist())
    # z.extract() - конкретно какой файл
    # z.extractall('куда')
