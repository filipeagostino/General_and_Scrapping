import pandas as pd
import os
import numpy as np


path_arquivos = f'path/'


repositorio_geral = pd.DataFrame()

os.chdir(path_arquivos)
list_files = []
for f in os.listdir():
    print(f)
    list_files.append(f)

tam = len(list_files)
cont = 0

for i in list_files:
    try:
        path = path_arquivos + f'{i}'
        df = pd.read_excel(path)
        print(df)
        print(df.shape)
        list_temp_concat = [df, repositorio_geral]
        repositorio_geral = pd.concat(list_temp_concat)
        cont += 1
        print(f'Repositorio:\n{repositorio_geral}')
        print(f'ANDAMENTO: {tam - cont} de {tam}')
    
    except (Exception) as err:
        print(err)

print(repositorio_geral)

repositorio_geral.to_excel(f'path_to_save/name.xlsx', index=False)
