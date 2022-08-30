import os
import app
import config



def recupera_imagem(id):
    
    for nome_arquivo in os.listdir(f'{config.IMG_PATH}'):
        if f'capa{id}.jpg' == nome_arquivo:
            return nome_arquivo
    
    return "capa_padrao.png"