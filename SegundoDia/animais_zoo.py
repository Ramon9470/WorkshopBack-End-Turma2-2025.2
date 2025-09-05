class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return "Som genérico"

    def apresentar(self):
        return f"{self.nome}, {self.idade} anos"

class Gato(Animal):
    def falar(self):
        return "Miau"

class Cachorro(Animal):
    def falar(self):
        return "Au Au"

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        for animal in self.animais:
            print(f"{animal.apresentar()} - Som: {animal.falar()}")

    def filtrar_por_tipo(self, tipo):
        return [animal for animal in self.animais if isinstance(animal, tipo)]

zoo = Zoologico()

gato1 = Gato("Mimi", 3)
cao1 = Cachorro("Rex", 5)

zoo.adicionar_animal(gato1)
zoo.adicionar_animal(cao1)

print("Todos os animais:")
zoo.listar_animais()

print("\nApenas os gatos:")
gatos = zoo.filtrar_por_tipo(Gato)
for gato in gatos:
    print(f"{gato.apresentar()} - Som: {gato.falar()}")
