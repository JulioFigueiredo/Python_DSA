class Livro():
    
    def __init__(self): # construtor
        self.titulo = 'Sapiens - Uma breve história da humanidade'
        self.isbn = 9988888
        print('Construtor')
        
    def imprime(self):
        print(f'Foi criado o livro {self.titulo}, com ISBN {self.isbn}')
        
livro1 = Livro()

livro1.imprime()