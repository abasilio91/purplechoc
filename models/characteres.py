import string
import random
from models.opcoes import Opcoes

class Characteres:
    def maiusculas(self):
        return list(string.ascii_uppercase)

    def minusculas(self):
        return list(string.ascii_lowercase)
    
    def numeros(self):
        return list(string.digits)
    
    def simbolos(self):
        return list(string.punctuation)
    
    def lista_characteres_validos(self, opcoes: dict=None) -> list:
        if not opcoes:
            opcoes = Opcoes().get_opcoes()

        print(f'--- {opcoes} ---')

        opcoes = {
            self.maiusculas: opcoes[1],
            self.minusculas: opcoes[2],
            self.numeros: opcoes[3],
            self.simbolos: opcoes[4]
        }

        characteres_validos = []
        for chave, valor in opcoes.items():
            if valor:
                characteres_validos.append(chave())
                
        lista_achatada = [val for sublista in characteres_validos for val in sublista]
        random.Random(42).shuffle(lista_achatada)
        return lista_achatada, len(lista_achatada)