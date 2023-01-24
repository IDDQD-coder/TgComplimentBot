import os


def rename_files_to_numbers(path):
    number = 1
    for f in os.listdir(path):
        print(f)
        os.rename(path+'/'+f, f'{path}/.{number}.jpg')
        print(os.path)
        number += 1
    number = 1
    for f in os.listdir(path):
        print(f)
        os.rename(path+'/'+f, f'{path}/{number}.jpg')
        print(os.path)
        number += 1


rename_files_to_numbers('./myimages')
rename_files_to_numbers('./herimages')