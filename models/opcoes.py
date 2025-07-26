class Opcoes:
    def __init__(self, 
                 optin_tamanho: int=44, 
                 optin_maiusculas: bool=True, 
                 optin_minusculas: bool=True, 
                 optin_numeros: bool=True, 
                 optin_simbolos: bool=True):
        self.optin_tamanho = optin_tamanho
        self.optin_maiusculas = optin_maiusculas
        self.optin_minusculas = optin_minusculas
        self.optin_numeros = optin_numeros
        self.optin_simbolos = optin_simbolos

    def get_opcoes(self) -> list:
        opcoes = [
            self.optin_tamanho,
            self.optin_maiusculas,
            self.optin_minusculas,
            self.optin_numeros,
            self.optin_simbolos
        ]

        return opcoes