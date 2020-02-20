# from ftplib import FTP
#
# ftp = FTP('192.168.77.23')
#
# ftp.login('root', '20091665')

import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection('192.168.77.66', username='root', password=input("Password: "), cnopts=cnopts) as sftp:
    with sftp.cd('NetworkProgramming'): # cambiar de directorio temporalmente
        print(sftp.listdir())
        print(sftp.pwd) # retorna directorio en el que se está trabajando actualmente
        sftp.put("C:\\Users\\Ivan's PC\\Documents\\tmp\\firstkeypair.pem")  # cargar archivo
        sftp.get('mi_archivo.txt', "C:\\Users\\Ivan's PC\\Documents\\mi_archivo_descargado.txt")         # descargar archivo
