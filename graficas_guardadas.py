# ****************
# Abre las graficas guradadas en un navegador
# ****************

import webbrowser
import os
import pdb
 
def graficas_guardadas(cliente,mes,findero,seleccion):

    carpeta = f'D:/01 Findero/{mes}/{cliente}/Graficas/{findero}'
    graficas = os.listdir(carpeta)
    graficas = [g for g in graficas if 'html' in g]

    for idx, elemento in enumerate(seleccion):  
        for grafica in graficas:
            if f' {elemento}.' in grafica:
                url = f'{carpeta}/{grafica}'

                webbrowser.open(url,new=2)