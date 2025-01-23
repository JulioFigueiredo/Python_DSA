import Animal

class Gato(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Objeto gato criado.')
        
    def emitir_som(self):
        print('miau')