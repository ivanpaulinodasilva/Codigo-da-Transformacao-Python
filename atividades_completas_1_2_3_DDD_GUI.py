'''
Use a biblioteca `requests` para pegar dados do tempo da API do OpenWeatherMap.

Exiba Filtre e exiba apenas as informações relevantes da API, como temperatura e condições climáticas.

TrateImplemente um bloco de tratamento de exceção para lidar com falhas de requisição HTTP.

Crie um programa que busca dados de filmes com a API do TMDB e exiba título, gênero e sinopse.
'''

import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# --- DEFINIÇÃO DA PALETA DE CORES (SUAS CORES EXTRAÍDAS) ---
COR_FUNDO_JANELA = "#004d6e"   # Azul Escuro
COR_BOTAO = "#0081ab"          # Azul Médio
COR_BOTAO_HOVER = "#00b1cd"    # Azul Claro
COR_TEXTO_DESTAQUE = "#b83764" # Vinho / Rosa Escuro
COR_TEXTO_LISTA = "#a6c844"    # Verde Claro
COR_TEXTO_TITULO = "#edce01"   # Amarelo Ouro
COR_FUNDO_TEXTO = "#4a3336"    # Marrom / Escuro

# --- FUNÇÃO LÓGICA DA API COM TRATAMENTO DE ERROS ---
def buscar_ddd():
    ddd = entrada_ddd.get().strip()
    
    # Validação inicial: verifica se o campo está vazio
    if not ddd:
        messagebox.showwarning("Aviso", "Por favor, digite um código de DDD!")
        return
        
    # Ativa a área de texto para permitir a atualização
    area_texto.config(state=tk.NORMAL)
    area_texto.delete(1.0, tk.END)
    area_texto.insert(tk.END, f"Conectando à API para buscar o DDD {ddd}...\n\n")
    
    url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
    
    try:
        # Requisito 1: Consumir a API via requests
        resposta = requests.get(url)
        
        # Requisito 3: Tratar erro de DDD inválido/não encontrado (Erro 404)
        if resposta.status_code == 404:
            area_texto.delete(1.0, tk.END) # Limpa o texto de carregamento
            messagebox.showerror("Erro", f"O DDD {ddd} não é um código de área válido no Brasil!")
            return
            
        resposta.raise_for_status()
        dados = resposta.json()
        
        # Limpa o texto temporário de busca
        area_texto.delete(1.0, tk.END)
        
        # Requisito 2: Filtrar e exibir dados específicos
        estado = dados['state']
        cidades = dados['cities'] # CORRIGIDO: de 'cidade' para 'cities'
        
        # Inserindo dados na tela com marcações de cores personalizadas
        area_texto.insert(tk.END, f"📍 Estado Localizado: {estado}\n", "titulo_destaque")
        area_texto.insert(tk.END, f"🏙️ Cidades atendidas (Total: {len(cidades)}):\n", "titulo_destaque")
        area_texto.insert(tk.END, "="*43 + "\n\n", "linhas")
        
        # CORRIGIDO: Removido a repetição de "in cidade" que quebrava a sintaxe
        for cidade in cidades:
            area_texto.insert(tk.END, f"• {cidade}\n", "conteudo_lista")
            
    # Requisito 3: Tratar falhas de conexão de rede
    except requests.exceptions.ConnectionError:
        area_texto.delete(1.0, tk.END)
        messagebox.showerror("Erro de Rede", "Não foi possível conectar à internet! Verifique o sinal.")
        
    except Exception as e:
        area_texto.delete(1.0, tk.END)
        messagebox.showerror("Erro Inesperado", f"Ocorreu um erro no sistema: {e}")
        
    finally:
        # Bloqueia novamente a área para impedir edição do usuário
        area_texto.config(state=tk.DISABLED)

# --- FUNÇÕES VISUAIS DO BOTÃO (EFEITO HOVER) ---
def on_enter(e):
    botao_buscar['background'] = COR_BOTAO_HOVER

def on_leave(e):
    botao_buscar['background'] = COR_BOTAO

# --- CONSTRUÇÃO DA INTERFACE GRÁFICA (GUI) ---
janela = tk.Tk()
janela.title("Localizador de Cidades por DDD")
janela.geometry("500x480")
janela.configure(bg=COR_FUNDO_JANELA)

# Título da tela
rotulo = tk.Label(janela, text="Digite o DDD (apenas 2 números):", 
                  font=("Arial", 12, "bold"), bg=COR_FUNDO_JANELA, fg=COR_TEXTO_TITULO)
rotulo.pack(pady=15)

# Entrada de dados
entrada_ddd = tk.Entry(janela, font=("Arial", 14), width=10, justify="center", bd=3)
entrada_ddd.pack(pady=5)

# Botão de comando (totalmente corrigido com padx e pady)
botao_buscar = tk.Button(
    janela, 
    text="Consultar Região", 
    font=("Arial", 11, "bold"), 
    bg=COR_BOTAO, 
    fg="white", 
    bd=0, 
    padx=12, 
    pady=6, 
    cursor="hand2", 
    command=buscar_ddd
)
botao_buscar.pack(pady=15)

# Vínculo do efeito hover
botao_buscar.bind("<Enter>", on_enter)
botao_buscar.bind("<Leave>", on_leave)

# Caixa de texto com rolagem lateral para listar as cidades
area_texto = scrolledtext.ScrolledText(janela, width=55, height=16, 
                                       font=("Courier New", 10, "bold"), 
                                       bg=COR_FUNDO_TEXTO, fg=COR_TEXTO_LISTA, bd=4)
area_texto.pack(pady=10)

# Tags de formatação de cores do texto interno
area_texto.tag_config("titulo_destaque", foreground=COR_TEXTO_TITULO, font=("Courier New", 11, "bold"))
area_texto.tag_config("linhas", foreground=COR_TEXTO_DESTAQUE)
area_texto.tag_config("conteudo_lista", foreground=COR_TEXTO_LISTA)

# Inicia travado para proteção do componente
area_texto.config(state=tk.DISABLED)

janela.mainloop()