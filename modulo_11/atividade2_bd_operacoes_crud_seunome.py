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

conn = sqlite3.connect('atividade_info_cliente.db')

cursor = conn.cursor()


cursor.execute('''

    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )

''')

cursor.execute('''

    INSERT INTO clientes (nome, email) VALUES 
    ('Matheus Hideo', 'joao.silva@mail.com'),
               
    ('Antônio  Alves', 'maria.oliveira@mail.com'),
               
    ('Alexandra Augusta ', 'carlos.santos@mail.com'),
               
    ('Lucas Freitas', 'joao.silva@mail.com'),
               
    ('Arthur Augusto ', 'maria.oliveira@mail.com'),
               
    ('Ana Alves', 'carlos.santos@mail.com'),
    
    ('Jhonatas nascimento', 'joao.silva@mail.com'),
               
    ('Antônio  Alberto', 'maria.oliveira@mail.com'),
               
    ('Alex Augustinho ', 'carlos.santos@mail.com'),
    
    ('Adriana Almeida', 'joao.silva@mail.com'),
               
    ('Angélica Andrade', 'maria.oliveira@mail.com'),
               
    ('Alê Alvarenga', 'carlos.santos@mail.com')
               

''')

conn.commit()

cursor.execute('DELETE FROM clientes') 
dados_iniciais = [
    ('Matheus Hideo', 'matheus@mail.com'), 
    ('Antônio Alves', 'antonio@mail.com'),
    ('Alexandra Augusta', 'alexandra@mail.com'), 
    ('Lucas Freitas', 'lucas@mail.com'),
    ('Arthur Augusto', 'arthur@mail.com'), 
    ('Ana Alves', 'ana@mail.com'),
    ('Jhonatas Nascimento', 'jhonatas@mail.com'), 
    ('Antônio Alberto', 'alberto@mail.com'),
    ('Alex Augustinho', 'alex@mail.com'), 
    ('Adriana Almeida', 'adriana@mail.com'),
    ('Angélica Andrade', 'angelica@mail.com'), 
    ('Alê Alvarenga', 'ale@mail.com')
]
cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', dados_iniciais)

conn.commit()

cursor.execute('UPDATE clientes SET email = ? WHERE nome = ?', ('hideo.novo@mail.com', 'Matheus Hideo'))

conn.commit()

cursor.execute('DELETE FROM clientes WHERE nome = ?', ('Lucas Freitas',))