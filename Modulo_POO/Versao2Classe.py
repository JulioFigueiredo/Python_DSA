class Livro():
    
    def __init__(self, titulo, isbn):
        self.titulo=titulo
        self.isbn=isbn
        print('construtor')
        
    def imprime(self, titulo, isbn):
        print(f'Esse é o livro {titulo}, com isbn {isbn}')
        
Livro2 = Livro("O Poder do Hábito", 77886611)

print(Livro2.titulo)