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
    r'E:\John\\aUNIT\TCC\collecting_tweets\coleta\\random4000\input',
    r'E:\John\\aUNIT\TCC\collecting_tweets\coleta\\random4000\input1',
    r'E:\John\\aUNIT\TCC\collecting_tweets\coleta\\random4000\input2',
    r'E:\John\\aUNIT\TCC\collecting_tweets\coleta\\random4000\input3',
    r'E:\John\\aUNIT\TCC\collecting_tweets\coleta\\random4000\input4',
    # Adicione quantas pastas desejar
]

check_duplicate_files(folder_paths)
