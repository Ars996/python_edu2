# #Напишите функцию группового переименования файлов. Она должна:
# #принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def rename_files(dir_path:str,
                 new_name:str ='',
                 count:int = 1,
                 in_ext:str = 'txt',
                 new_ext:str = 'txt',
                 slice_name:tuple = (0,0)):
    if not os.path.isdir(dir_path):
        return False
    file_list = os.listdir(dir_path)
    print(file_list)
    files_count = 1
    for cur_file in file_list:
        cur_name,cur_ext = cur_file.split('.')

        if cur_ext == in_ext:
            new_file = ' '
            if slice_name:
                new_file += f'{cur_name[slice_name[0]:slice_name[1]]}'
            if new_name:
                new_file += f'{new_name}'
            new_file += f'_{files_count:0>{count}}.{new_ext}'
            os.rename(os.path.join(dir_path, cur_file),
                      os.path.join(dir_path, new_file))
            files_count += 1
    return f'{files_count} - количество переименованых файлов'



print(rename_files('Files', new_name="update_name", count=2, in_ext='txt', new_ext='doc', slice_name=(2,5)))
