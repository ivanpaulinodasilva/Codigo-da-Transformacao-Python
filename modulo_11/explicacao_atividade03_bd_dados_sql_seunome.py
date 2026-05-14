'''

1.  **Crie sua primeira tabela:** Configure um banco de 
dados SQLite e crie uma tabela 
`Clientes` com `id`, `nome` e `email`.

2.  **Implemente operações CRUD:** 
Desenvolva um programa para inserir, consultar, 
atualizar e deletar dados na tabela Clientes.

3.  **Filtre dados com SQL:** Execute consultas 
para extrair informações específicas do banco de 
dados, como clientes com nome começando em "A".

* **Desafio Extra:** Crie um sistema de 
gerenciamento de tarefas que permita adicionar, 
visualizar e excluir tarefas, usando o SQLite 
para armazenar os dados.

Antônio Alves 
Alexandra Augusta 
Ana Alves
Arthur Augusto 
Antônio Alves 
Alexandra Augusta 
Adriana Almeida
Alexandre Alves
Angélica Andrade
Adriano Alvin
Augusto Albuquerque
Adriano Amaral
Alberto Alexandre 
Alice Amaral 
Alison Andrade 
Adriana Silva;
Arthur Souza
Arthur Alexandre 
Matheus Albano
Maycon augusto
Paulo Paiva
Arthur Alexandre 
Matheus Albano
Guilherme Souza
Adriano Alvin
Augusto Albuquerque
Arthur Almeida
André Alves 
Jhonatan Oliveira
Alberto Augustos;
Adriano Almeida
Miguel Soares
Miguel Soares
Jhonatas Nascimento
Lucas Freitas
Matheus Hideo

'''

# importar biblioteca
import sqlite3

# conectar banco de dados
conn = sqlite3.connect('atividade_info_cliente.db')

# executar o sql
cursor = conn.cursor()

clientes = cursor.fetchall()


cursor.execute('''

    INSERT INTO clientes (nome, email) VALUES
                
    ('Leticia Dorta', 'joao.silva@mail.com'),
               
    ('Ayla Sousa', 'maria.oliveira@mail.com'),
               
    ('Aurélio Dinis ', 'carlos.santos@mail.com'),
               
    ('Igor Freitas', 'joao.silva@mail.com'),
               
    ('Ana Cecília ', 'maria.oliveira@mail.com'),
               
    ('Ana Alves', 'carlos.santos@mail.com'),
    
    ('André Ramalho', 'joao.silva@mail.com'),
               
    ('Maria Helena', 'maria.oliveira@mail.com'),
               
    ('Antônio Fernandes', 'carlos.santos@mail.com'),
    
    ('Ana Clara Machado', 'joao.silva@mail.com'),
               
    ('Vitor Bispo Cruz', 'maria.oliveira@mail.com'),
               
    ('Pedro Henrique', 'carlos.santos@mail.com')
               

''')

conn.commit()

cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', clientes)
conn.commit()
print("Sucesso: Novos clientes inseridos na base de dados.")

# --- CONSULTAR (Read) ---
print("\n--- LISTA DE CLIENTES ATUAIS ---")
cursor.execute("SELECT * FROM clientes")
for cliente in cursor.fetchall():
    print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")



# --- CONSULTAR (Somente com a letra 'A') ---
print("\n--- Clientes com nome começando com 'A' ---")
# O símbolo % é um coringa que representa "qualquer coisa depois"
cursor.execute("SELECT * FROM clientes WHERE nome LIKE 'A%'")

for cliente in cursor.fetchall():
    print(f"ID: {cliente[0]} | Nome: {cliente[1]}")