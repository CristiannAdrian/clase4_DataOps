import os

# Carpeta Dataset #
location = 'C:\Users\USER\Desktop\ciclo 2024-1\Dataops\proyecto_parcial\python\datasets'

#Valisdar si existe la carpeta#
if not os.path.exists(location):
    #si la carpeta no existe, la creo#
    os.mkdir(location)
else: #la carpeta existe#
    #borrar contenido#
    for root, dirs, files in  os.walk(location,topdown=False):
        for name in files:
            os.remove(os.path.join(root,name)) #eliminar los archivos#
        for name in dirs:
            os.rmdir(os.path.join(root,name)) #eñiminar las carpetas#

# Importar library API Kaggle #
from kaggle.api.kaggle_api_extended import KaggleApi

#Autenticarnos#
api = KaggleApi()
api.authenticate()

#Descargar data set#
