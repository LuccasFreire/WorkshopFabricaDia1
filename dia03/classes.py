from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def falar(self):
        """"""
    @abstractmethod
    def andar(self):
        """"""
class Cachorro(IAnimal):
    def falar(self):
        print("Au au")
    
    def andar(self):
        print("Ando com 4 patas")

class Pessoa():
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade
        self.___humano = True

    def mostra_nome(self):
        print(self.nome)

    def fala_pessoa():
        print("Falando")

catchorro = Cachorro()
catchorro.andar()

humano = Pessoa("Lucas", 21)
humano.fala_pessoa()
humano.mostra_nome()