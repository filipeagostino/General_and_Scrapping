import pandas as pd
import os
from colorama import Fore, init
init(autoreset=True)


path_directorys = 'C://Users/User/Downloads/result/2021/'
path_to_save = 'C://Users/User/Downloads/output/'

def converter(path_directorys, path_to_save):

    try:
        os.chdir(path_directorys)
        list_directorys = []
        for f in os.listdir():
            print(f)
            list_directorys.append(f)

        size_directorys = len(list_directorys)
        cont_directorys = 0

    except (Exception) as err:
        print(Fore.RED + f'{err}')


    try:
        for i in list_directorys:
            path_file = path_directorys + f'/{i}'
            os.chdir(path_file)
            list_files_local = []
            for f in os.listdir():
                print(f)
                list_files_local.append(f)
                cont_directorys += 1

            print(Fore.GREEN + f'Directorys:\n{list_files_local}')
            print(Fore.GREEN + f'{cont_directorys} - {cont_directorys}')

            tam_local = len(list_files_local)
            cont_local = 0
                     
    except (Exception) as err:
        print(Fore.RED + f'{err}')

        for i in list_files_local:
            try:
                path_local2 = path_file + f'/{i}'
                df = pd.read_excel(path_local2, engine='pyxlsb', sheet_name='Base')
                print(df)
                print(df.shape)
                df.to_excel(f'{i}.xlsx', index=False)
                cont_local += 1
                print(Fore.GREEN + f'{cont_local} - {tam_local}')
            except (Exception) as err:
                print(Fore.RED + f'{err}')
