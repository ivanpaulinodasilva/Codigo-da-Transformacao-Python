class CarroPremium:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Este método é chamado sempre que usas print(objeto)
    def __str__(self):
        return f"Este é um luxuoso {self.marca} {self.modelo}."

# Exemplo de uso:
carro_luxo = CarroPremium("Porsche", "911")
# Note que não precisamos chamar um método, o print usa o __str__ automaticamente
print(carro_luxo) 