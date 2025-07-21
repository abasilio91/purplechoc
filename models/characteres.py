import string
import random
from models.opcoes import Opcoes

class Characteres:
    def __init__(self):
        self.characteres = {
            "maiusculas": list(string.ascii_uppercase),
            "minusculas": list(string.ascii_lowercase),
            "numeros": list(string.digits),
            "simbolos": list(string.punctuation)
        }        

    def lista_characteres_validos(self, opcoes: dict=None) -> list:
        if not opcoes:
            opcoes = Opcoes().get_opcoes()

        characteres_validos = []
        for item_opcoes, item_chararacter in zip(opcoes[1:], self.characteres.values()):
            if item_opcoes:
                characteres_validos.append(item_chararacter)

        lista_achatada = [val for sublista in characteres_validos for val in sublista]
        random.Random(42).shuffle(lista_achatada)

        return lista_achatada, len(lista_achatada)