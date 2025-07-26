from hashlib import pbkdf2_hmac
from base64 import b64encode

from models.characteres import Characteres
from models.opcoes import Opcoes

class Encriptador:
    def gera_senha_criptografada(site, senha, salt="ASdh3729¨!8290AH7", opcoes: dict=None) -> str:
        if not opcoes:
            opcoes = Opcoes().get_opcoes()

        iter = 500_000
        original_key = b64encode(bytes(f'{site+senha+salt}', 'utf-8'))
        enc_key = pbkdf2_hmac('sha256', original_key, bytes(f'{salt}', 'utf-8') * 2, iter)
        return b64encode(enc_key).decode("utf-8")[:opcoes[0]]
    
    def vigenere(senha: str, chave: str="ASdh3729¨!8290AH7", opcoes: dict=None) -> str:
        if not opcoes:
            opcoes = Opcoes().get_opcoes()

        if len(chave) < len(senha):
            chave += senha
        chave = chave[:len(senha)]
        
        lista_characteres_validos, len_characteres_validos = Characteres().lista_characteres_validos(opcoes)
        lista_characteres_totais, _ = Characteres().lista_characteres_validos()
        cifra = ""
        for senha_char, chave_char in zip(senha, chave):
            index_senha = lista_characteres_totais.index(senha_char)
            index_chave = lista_characteres_totais.index(chave_char)
            offset = (index_senha + index_chave) % len_characteres_validos
            cifra += lista_characteres_validos[offset]
        return cifra