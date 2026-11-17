from musica import Musica

class Catalogo:
    def __init__(self):
        self.musicas = []
        self.musica_atual = None 
        self.reproducoes = {}   
        self.favoritos = []
        
    def add_musica(self ,musica):
        if not isinstance(musica, Musica):
            raise TypeError("É necessário informar um objeto da classe Musica!")
        self.musicas.append(musica)
        self.reproducoes[musica] = 0
        return True