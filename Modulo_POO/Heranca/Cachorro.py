from Animal import Animal

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Objeto cachorro criado.')
        
    def emitir_som(self):
        print('auau')
        
rex = Cachorro()
rex.emitir_som()
rex.comer()