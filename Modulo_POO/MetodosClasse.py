
class Circulo:
    
    pi = 3.14
    
    # deixa o raio como 5 por padrão
    def __init__(self, raio=5):
        self.raio = raio
        
    def area(self):
        return (self.raio * self.raio) * Circulo.pi
    
    def setRaio(self, novo_raio):
        self.raio=novo_raio
        
    def getRaio(self):
        return self.raio
    
c1 = Circulo()
print(c1.getRaio())

c2 = Circulo(8)
print(c2.getRaio())
print(c2.area())