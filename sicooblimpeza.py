import os
import shutil
import subprocess
count = 0
option = 9

#PRECISA SER EXECUTADO COMO ADMINISTRADOR!

username = os.getenv('USERNAME')
def deletar_files(caminho):
    for root,dirs,files in os.walk(caminho):
        for file in files:
            caminho_completo = os.path.join(caminho, file)
            try:
                os.unlink(caminho_completo)
                print(f'Arquivo excluído: {file}')
            except:
                print(f'Não foi possível excluir esse arquivo: {file}')
                continue
while option != 4:
    print(f'''            \033[32mSICOOB VALE-SUL | (TI)\033[m''')
    print()
    print('1 - executar limpeza no disco. 🧹💿')
    print('2 - verificar espaço no disco. 🔍💿')
    print('3 - deletar usuários da máquina ❌👤')
    print('4 - sair 🚪')
    option = int(input('Digite a opção: '))

    match option:
        case 1:
            
            downloads = os.path.join(f'c:\\Users\\{username}\\Downloads\\')
            deletar_files(downloads)      
            temp = os.path.join(f'C:\\Users\\{username}\\AppData\\Local\\Temp')
            deletar_files(temp)
            wtemp = os.path.join('C:\\Windows\\Temp')
            deletar_files(wtemp)
            prefetch = os.path.join('C:\\Windows\\Prefetch')
            deletar_files(prefetch)
            print('\033[31mLimpeza de disco...\033[m')
            os.system('cleanmgr')
            print('Limpando cache DNS...')
            os.system('ipconfig /flushdns')
            print('Verificando arquivos corrompidos e corrigindo...')
            os.system('sfc /scannow')
            
        case 2:
            volume__= subprocess.check_output('fsutil volume diskfree C:', shell = True, text = True)
            volume_ =  volume__.split('\n')[:2]
            for line in volume_:
                print(line)        
            
        case 3:
            pass

        case 4:
            quit()
        
        case _:
            print('opção inválida :(')