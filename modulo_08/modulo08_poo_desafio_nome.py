'''
Criar um Sistema de Biblioteca

Class Livro

    (Produtos) 
    Livros, Periodicos, Jornal, Maps, Gibi/Mangás

Class Biblioteca (main)

    (Processos / Serviços)
    Ler, Pesquisa, Emprestado-Devolução
atributos - metodos
'''
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' - {self.autor} [{status}]"

class Biblioteca:
    def __init__(self):
        self.livros = [] # Lista para armazenar objetos da classe Livro

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo_procurado):
        for livro in self.livros:
            if livro.titulo == titulo_procurado:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Empréstimo de '{livro.titulo}' realizado!")
                else:
                    print(f"O livro '{livro.titulo}' já está ocupado.")
                return
        print("Livro não encontrado no acervo.")

# --- Testando o Sistema de Biblioteca ---
biblioteca_municipal = Biblioteca()
l1 = Livro("Dom Quixote", "Miguel de Cervantes")
l2 = Livro("O Principezinho", "Antoine de Saint-Exupéry")
l3 = Livro("Don casmurro", "Machado de Assis")
l4 = Livro("It a coisa", "Stephen King")

biblioteca_municipal.adicionar_livro(l1)
biblioteca_municipal.adicionar_livro(l2)

print(l2) # Estado inicial
biblioteca_municipal.emprestar_livro("O Principezinho")
print(l2) # Estado após empréstimo