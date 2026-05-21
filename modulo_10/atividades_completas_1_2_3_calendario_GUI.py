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
def buscar_feriados():
    ano = entrada_ano.get().strip()
    
    if not ano:
        messagebox.showwarning("Aviso", "Por favor, digite um ano!")
        return
        
    # Limpa a área de texto antes de exibir o novo resultado
    area_texto.config(state=tk.NORMAL) # Ativa temporariamente para permitir a escrita
    area_texto.delete(1.0, tk.END)
    area_texto.insert(tk.END, f"Buscando feriados para o ano {ano}...\n\n")
    
    url = f"https://brasilapi.com.br/api/feriados/v1/{ano}"
    
    try:
        resposta = requests.get(url)
        
        if resposta.status_code == 404:
            messagebox.showerror("Erro", "Ano não encontrado ou fora do limite do sistema!")
            area_texto.delete(1.0, tk.END)
            return
            
        resposta.raise_for_status()
        feriados = resposta.json()
        
        # Limpa o texto temporário de busca
        area_texto.delete(1.0, tk.END)
        
        # Inserindo o título com formatação de cor customizada
        area_texto.insert(tk.END, f"🎉 Feriados Nacionais em {ano}:\n", "titulo_destaque")
        area_texto.insert(tk.END, "="*43 + "\n\n", "linhas")
        
        # Loop para percorrer e filtrar os dados da API
        for feriado in feriados:
            texto_feriado = f"📅 Data: {feriado['date']} | 🎈 {feriado['name']}\n"
            area_texto.insert(tk.END, texto_feriado, "conteudo_lista")
            
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Erro de Conexão", "Não foi possível conectar à internet!")
        area_texto.delete(1.0, tk.END)
        
    except Exception as e:
        messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")
        area_texto.delete(1.0, tk.END)
        
    finally:
        area_texto.config(state=tk.DISABLED) # Bloqueia o campo para o usuário não digitar dentro dele

# --- FUNÇÕES VISUAIS PARA O BOTÃO (EFEITO HOVER) ---
def on_enter(e):
    botao_buscar['background'] = COR_BOTAO_HOVER

def on_leave(e):
    botao_buscar['background'] = COR_BOTAO

# --- CONSTRUÇÃO DA INTERFACE GRÁFICA (TELA CUSTOMIZADA) ---
janela = tk.Tk()
janela.title("Buscador de Feriados Brasileiros")
janela.geometry("500x480")
janela.configure(bg=COR_FUNDO_JANELA) # Aplicando a cor de fundo na janela principal

# Rótulo (Label) descritivo
rotulo = tk.Label(janela, text="Digite o ano desejado (ex: 2026):", 
                  font=("Arial", 12, "bold"), bg=COR_FUNDO_JANELA, fg=COR_TEXTO_TITULO)
rotulo.pack(pady=15)

# Campo de entrada (Entry) onde o usuário digita o ano
entrada_ano = tk.Entry(janela, font=("Arial", 14), width=12, justify="center", bd=3)
entrada_ano.pack(pady=5)

# --- CORREÇÃO DA LINHA 87: Substituído 'padding' por 'padx' e 'pady' ---
botao_buscar = tk.Button(
    janela, 
    text="Buscar Feriados", 
    font=("Arial", 11, "bold"), 
    bg=COR_BOTAO, 
    fg="white", 
    bd=0, 
    padx=12,      # Margem interna nas laterais esquerda/direita
    pady=6,       # Margem interna no topo/base
    cursor="hand2", 
    command=buscar_feriados
)
botao_buscar.pack(pady=15)

# Vinculando os eventos do mouse para criar o efeito visual de seleção do botão
botao_buscar.bind("<Enter>", on_enter) 
botao_buscar.bind("<Leave>", on_leave) 

# Área de texto com barra de rolagem para exibição dos resultados da API
area_texto = scrolledtext.ScrolledText(janela, width=55, height=16, 
                                       font=("Courier New", 10, "bold"), 
                                       bg=COR_FUNDO_TEXTO, fg=COR_TEXTO_LISTA, bd=4)
area_texto.pack(pady=10)

# Mapeamento das "Tags" de cores aplicadas dentro da caixa de texto
area_texto.tag_config("titulo_destaque", foreground=COR_TEXTO_TITULO, font=("Courier New", 12, "bold"))
area_texto.tag_config("linhas", foreground=COR_TEXTO_DESTAQUE)
area_texto.tag_config("conteudo_lista", foreground=COR_TEXTO_LISTA)

# Trava inicial para manter a caixa de texto limpa e protegida antes do clique
area_texto.config(state=tk.DISABLED)

# Inicializador do motor visual da janela
janela.mainloop()