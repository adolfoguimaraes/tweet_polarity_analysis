import os
import random
import shutil

source_dir_path = r'E:\John\\aUNIT\TCC\collecting_tweets\coleta\\basefull\input' # Substitua pelo caminho da pasta que deseja selecionar os arquivos
destination_dir_path = r'E:\John\\aUNIT\TCC\collecting_tweets\coleta\\random4000\input4' # Substitua pelo caminho da pasta para onde deseja copiar os arquivos
num_files = 4000 # Substitua pelo número de arquivos que deseja selecionar aleatoriamente

# Exclui todos os arquivos da pasta de destino
for file_name in os.listdir(destination_dir_path):
    file_path = os.path.join(destination_dir_path, file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)

# Verifica se já existem arquivos selecionados anteriormente
selected_files = set()
if os.path.exists('selected_files.txt'):
    with open('selected_files.txt', 'r') as f:
        selected_files = set(f.read().splitlines())

# Obtém a lista de arquivos não selecionados
files = [file_name for file_name in os.listdir(source_dir_path) if file_name not in selected_files]

# Verifica se há arquivos suficientes não selecionados
if len(files) < num_files:
    print('Não há arquivos suficientes para selecionar.')
    num_files = len(files)

# Seleciona aleatoriamente os arquivos disponíveis, evitando duplicatas
selected_files = set(random.sample(files, num_files))

# Copia os arquivos selecionados para a pasta de destino
for file_name in selected_files:
    source_file_path = os.path.join(source_dir_path, file_name)
    destination_file_path = os.path.join(destination_dir_path, file_name)
    shutil.copy(source_file_path, destination_file_path)

# Adiciona os novos arquivos selecionados ao arquivo "selected_files.txt"
with open('selected_files.txt', 'a') as f:
    f.write('\n'.join(selected_files))
    f.write('\n')

print(f'{num_files} arquivos selecionados aleatoriamente foram copiados para "{destination_dir_path}".')
