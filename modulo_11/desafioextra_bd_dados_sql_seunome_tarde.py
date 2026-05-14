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

**Entrega:** Adicione o código na pasta 
`Modulo_11/` do seu repositório no GitHub e envie o link.


'''

import sqlite3
import json

conn = sqlite3.connect('atividade_info_cliente.db')

cursor = conn.cursor()

# --- PASSO 2: BUSCAR OS DADOS ---
cursor.execute("SELECT * FROM clientes")
linhas = cursor.fetchall()

# --- PASSO 3: TRANSFORMAR EM LISTA DE DICIONÁRIOS ---
# O JSON precisa de chaves (nomes) para cada valor
lista_clientes_json = []

for linha in linhas:
    dados_cliente = {
        "id": linha[0],
        "nome": linha[1],
        "email": linha[2]
    }
    lista_clientes_json.append(dados_cliente)

# --- PASSO 4: CRIAR E ESCREVER O ARQUIVO .JSON ---
# 'w' significa write (escrita)
# indent=4 serve para o arquivo ficar organizado e fácil de ler
with open('clientes_exportados.json', 'w', encoding='utf-8') as ficheiro:
    json.dump(lista_clientes_json, ficheiro, indent=4, ensure_ascii=False)

conn.close()

print("Sucesso! O arquivo 'clientes_exportados.json' foi criado na sua pasta.")