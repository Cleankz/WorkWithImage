import os.path

def File_reader(extension):
    """Этот модуль возвращает список файлов в директории"""
    fil = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if extension in file:
                fileees = ''.join(file)
                fil.append(fileees)
    return fil