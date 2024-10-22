import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директория {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы {", ".join([file for file in catalog[2]])}')
    print('-'*40)

print_docs('C:/Music/Dorian Electra - Fanfare (2023) [CD FLAC] {6922462566}')