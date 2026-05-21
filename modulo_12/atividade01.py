import unittest

# 1. Esta é a função que queremos testar
def somar(a, b):
    return a + b

# 2. Esta é a classe que vai conter os nossos testes
class TestSoma(unittest.TestCase):
    
    # Cada método de teste DEVE começar com a palavra 'test_'
    def test_soma_numeros_positivos(self):
        # Explicação: Estamos testando se somar(2, 3) é igual a 5
        resultado = somar(2, 3)
        self.assertEqual(resultado, 5)

    def test_soma_numeros_negativos(self):
        # Explicação: Testando se somar(-1, -1) é igual a -2
        resultado = somar(-1, -1)
        self.assertEqual(resultado, -2)

# Código para permitir executar o teste direto pelo terminal
if __name__ == '__main__':
    unittest.main()