class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return 'Som de animal'
    
    def apresentar(self):
        return f'Nome: {self.nome}, Idade: {self.idade} anos'
    
class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return 'Miau!'
    
class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return 'Au Au!'

animais = [Gato('Whiskers', 3), Cachorro('Buddy', 5)]
for animal in animais:
    print(animal.apresentar())
    print(animal.falar())
        
