def find_dir(file):
    dir_main = '\\'.join(file.split('\\')[:-1]) + '\\' #Diretório do script
    return dir_main