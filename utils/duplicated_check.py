# Verifica se existe arquivos duplicados e informa quais são

import os

def check_duplicate_files(folders):
    all_files = set()
    duplicate_files = set()

    for folder_path in folders:
        files = set(os.listdir(folder_path))
        duplicate_files.update(all_files.intersection(files))
        all_files.update(files)

    if duplicate_files:
        print("Arquivos duplicados encontrados:")
        print(len(duplicate_files))
    else:
        print("Não foram encontrados arquivos duplicados.")

# Exemplo de uso
folder_paths = [
    r'C:\caminho\para\pasta',
    r'C:\caminho\para\pasta',
    r'C:\caminho\para\pasta',
    # Adicione quantas pastas desejar
]

check_duplicate_files(folder_paths)
