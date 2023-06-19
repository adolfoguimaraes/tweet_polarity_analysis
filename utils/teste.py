import os
import shutil

def remove_duplicate_files(folders):
    all_files = {}
    duplicate_files = set()

    for folder_path in folders:
        files = set(os.listdir(folder_path))
        for file in files:
            if file in all_files:
                duplicate_files.add(file)
                os.remove(os.path.join(folder_path, file)) # remove o arquivo duplicado
            else:
                all_files[file] = folder_path

    if duplicate_files:
        print("Arquivos duplicados encontrados e removidos:")
        print(len(duplicate_files))
    else:
        print("Não foram encontrados arquivos duplicados.")

# Exemplo de uso
folder_paths = [
    r'E:\John\\aUNIT\TCC\collecting_tweets\coleta\\random4000\input',
    r'E:\John\\aUNIT\TCC\collecting_tweets\coleta\\random4000\input1',
    r'E:\John\\aUNIT\TCC\collecting_tweets\coleta\\random4000\input2',
    r'E:\John\\aUNIT\TCC\collecting_tweets\coleta\\random4000\input3',
    r'E:\John\\aUNIT\TCC\collecting_tweets\coleta\\random4000\input4',
    # Adicione quantas pastas desejar
]

remove_duplicate_files(folder_paths)
