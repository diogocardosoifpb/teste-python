# Código da classe a ser testada
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio * self.raio

    def circunferencia(self):
        return 2 * 3.14 * self.raio
