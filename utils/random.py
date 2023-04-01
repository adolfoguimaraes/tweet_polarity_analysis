import os
import random
import shutil

# Seleciona arquivos aleatoriamente e copia para outra pasta desejada

source_dir_path = r'C:\caminho\para\pasta' # Substitua pelo caminho da pasta que deseja selecionar os arquivos
destination_dir_path = r'C:\caminho\para\outra\pasta' # Substitua pelo caminho da pasta para onde deseja copiar os arquivos
num_files = 5 # Substitua pelo número de arquivos que deseja selecionar aleatoriamente

files = os.listdir(source_dir_path)
selected_files = random.sample(files, num_files)

for file_name in selected_files:
    source_file_path = os.path.join(source_dir_path, file_name)
    destination_file_path = os.path.join(destination_dir_path, file_name)
    shutil.copy(source_file_path, destination_file_path)

print(f'{num_files} arquivos selecionados aleatoriamente foram copiados para {destination_dir_path}.')
