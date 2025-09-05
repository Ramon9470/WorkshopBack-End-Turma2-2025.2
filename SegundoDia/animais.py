class Animal:
    def falar(self):
        return 'Som de animal'

class Gato:
    def falar(self):
        return 'Miau!'
    
class Cachorro:
    def falar(self):
        return 'Au Au!'

animais = [Animal(), Gato(), Cachorro()]

for animal in animais:
    print(animal.falar())