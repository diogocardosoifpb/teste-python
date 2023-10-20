class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio * self.raio

    def circunferencia(self):
        return 2 * 3.14 * self.raio
def test_circulo_area():
    c = Circulo(2)
    assert c.area() == 12.56  # Teste bem-sucedido

def test_circulo_circunferencia():
    c = Circulo(3)
    assert c.circunferencia() == 18.84  # Teste bem-sucedido
