class Musica:
    def __init__(self, titulo, genero, autor, duracao, lancamento):
        self._titulo = _validar_string(titulo,"Título")
        self._genero = _validar_string(genero,"Genero")
        self._autor =  _validar_string(autor,"Autor")
        self._duracao = _validar_inteiro(duracao, "Duracao")
        self._reproducoes = 0
        self._lancamento= _validar_inteiro(lancamento, "Lançamento")
        self.fav_bool = False
        self.rep_bool = False

    @staticmethod
    def _validar_string(valor,campo):
        if not isinstance(valor,str) or not valor.strip():
            raise ValueError(f"O campo {campo} deve ser um texto não vazio.")
        return valor.strip()

    @staticmethod
    def _validar_inteiro(valor,campo):
        if type(valor) is not int or valor <= 0:
            raise ValueError (f"O campo {campo} deve ser um número inteiro positivo")
        return valor

    @property
    def titulo(self):
        return self._titulo
    
    def genero(self):
        return self._genero
    
    def autor(self):
        return self._autor
    
    def duracao(self):
        return self._duracao
    
    def reproducoes(self):
        return self._reproducoes
    
    def lancamentos(self):
        return self._lancamentos

    def mudar_titulo(self, titulo):
        if not isinstance(titulo,str) or not titulo.strip():
            raise ValueError("O nome da música deve ser um texto não vazio!")
        self.titulo = titulo
        print(f"Informação alterado para {titulo}!")

    def mudar_genero(self, genero):
        if not isinstance(genero,str) or not genero.strip():
            raise ValueError("O genero da música deve ser um texto não vazio!")
        self.genero = genero
        print(f"Informação alterado para {genero}!")

    def mudar_autor(self, autor):
        self.autor = autor
        print(f"Informação alterado para {autor}!")

    def mudar_duracao(self, duracao):
        if type(duracao) is not int or duracao<=0:
            raise ValueError("A duração da música deve ser um número inteiro maior que 0!")
        self.duracao = duracao
        print(f"Informação alterado para {duracao}!")

    def mudar_lancamento(self, lancamento):
        if type(lancamento) is not int or lancamento<=0:
            raise ValueError("O ano de lançamento da música deve ser um número inteiro maior que 0!")
        self.lancamento = lancamento
        print(f"Informação alterado para {lancamento}!")

    def mostrar_titulo(self):
        print(f"Informação atual: {self.titulo}!")
    
    def mostrar_genero(self):
        print(f"Informação atual: {self.genero}!")

    def mostrar_autor(self):
        print(f"Informação atual: {self.autor}!")

    def mostrar_duracao(self):
        print(f"Informação atual: {self.duracao}!")

    def mostrar_reproducoes(self):
        print(f"Informação atual: {self.reproducoes}!")

    def mostrar_lancamento(self):
        print(f"Informação atual: {self.lancamento}!")

    def mostrar_notif(self):
        print(f"Musica: {self._titulo} - {self._autor} - {(self._duracao)//60}:{(self._duracao)%60})")

    def mostrar_detalhes(self):
        print("Detalhes da musica selecionada:")
        print(f"Titulo: {self._titulo};")
        print(f"Genero: {self._genero};")
        print(f"Autor: {self._autor};")
        print(f"Duracao: {(self._duracao)//60} minutos e {(self._duracao)%60} segundos ({self._duracao} segundos);")
        print(f"Reproducoes: {self._reproducoes};")
        print(f"Lancamento: {self._lancamento};")
        if self.fav_bool == True:
            print(f"A musica está favoritada!")
        else:
            print(f"A musica não está favoritada!")

    def favoritar(self):
        if self.fav_bool == True:
            print("A musica já está favoritada!")
        else:
            self.fav_bool = True
            print("Musica favoritada!")

    def desfavoritar(self):
        if self.fav_bool == False:
            print("A musica já está desfavoritada!")
        else:
            self.fav_bool = False
            print("Musica desfavoritada!")

    def reproduzir(self):
        if self.rep_bool == False:
            self.rep_bool = True
            self.reproducoes+=1
            print("Reproduzindo musica!")
        else:
            print("Musica já está em reprodução!")

    def pausar(self):
        if self.rep_bool == True:
            self.rep_bool = True
            print("Musica pausada!")
        else:
            print("Musica já está pausada!")
    