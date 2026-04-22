class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Passo 1: Precisamos de criar o método aqui na classe pai
    def exibir_info(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo}"

class CarroEletrico(Carro):
    # Herança de Classe
    def __init__(self, marca, modelo, autonomia_bateria):
        # O super() inicializa a marca e o modelo na classe pai
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria # Atributo específico do elétrico

    # Passo 2: Agora o super().exibir_info() vai funcionar!
    def exibir_info(self):
        # Ele vai buscar "Marca: X | Modelo: Y" da classe Carro
        info_base = super().exibir_info() 
        return f"{info_base} | Autonomia: {self.autonomia_bateria}km"

# --- Exemplo de uso ---
meu_ev = CarroEletrico("Tesla", "Model Y", 450)
print(meu_ev.exibir_info())