import re

def sort_file_names(file_path):
    with open(file_path, 'r') as f:
        file_names = f.read().splitlines()

    # Função para extrair as partes numéricas do nome do arquivo
    def file_key(file_name):
        match = re.match(r'coletaPlanalto(\d+)\s\((\d+)\)\.jsonl', file_name)
        if match:
            return int(match.group(1)), int(match.group(2))
        else:
            return (0, 0)

    file_names.sort(key=file_key)

    with open(file_path, 'w') as f:
        for file_name in file_names:
            f.write(file_name + '\n')

# Exemplo de uso
file_path = 'selected_files.txt'
sort_file_names(file_path)
