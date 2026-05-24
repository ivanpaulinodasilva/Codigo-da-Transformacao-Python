# Arquivo: gerador_dados.py

# Importa a classe Faker da biblioteca faker
from faker import Faker

# Cria uma instância (objeto) da classe Faker
# A instância 'faker' agora pode gerar dados falsos
faker = Faker('pt_BR')  # 'pt_BR' para gerar dados em português do Brasil

# O problema prático: gerar uma lista de 5 perfis de usuários
print("Gerando 5 perfis de usuários com dados falsos:\n")

# Loop para gerar 5 perfis
for i in range(15):
    nome = faker.name()
    endereco = faker.address()
    email = faker.email()
    
    # Imprime os dados gerados
    print(f"--- Perfil {i+1} ---")
    print(f"Nome: {nome}")
    print(f"Endereço: {endereco}")
    print(f"Email: {email}")
    print("-" * 20)  # Linha divisória