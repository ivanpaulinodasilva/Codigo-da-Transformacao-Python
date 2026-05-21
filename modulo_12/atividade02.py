import unittest

# 1. Definição da Classe Calculadora
class Calculadora:
    def somar(self, a, b):
        return a + b
        
    def dividir(self, a, b):
        if b == 0:
            # Lança um erro caso o usuário tente dividir por zero
            raise ValueError("Não é possível dividir por zero.")
        return a / b

# 2. Classe de Teste
class TestCalculadora(unittest.TestCase):
    
    # O método setUp roda ANTES de cada teste. Bom para criar objetos.
    def setUp(self):
        self.calc = Calculadora()

    def test_metodo_somar(self):
        # Testa a soma da calculadora
        self.assertEqual(self.calc.somar(10, 5), 15)

    def test_metodo_dividir_sucesso(self):
        # Testa uma divisão válida
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_metodo_dividir_por_zero(self):
        # Explicação: Aqui validamos se o programa lança a exceção (erro) correta
        # Esperamos que aconteça um ValueError quando dividimos por 0
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()