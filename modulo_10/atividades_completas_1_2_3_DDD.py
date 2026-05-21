'''
Use a biblioteca `requests` para pegar dados do tempo da API do OpenWeatherMap.

Exiba Filtre e exiba apenas as informações relevantes da API, como temperatura e condições climáticas.

TrateImplemente um bloco de tratamento de exceção para lidar com falhas de requisição HTTP.

Crie um programa que busca dados de filmes com a API do TMDB e exiba título, gênero e sinopse.
'''
import requests

def consultar_dados_ddd(ddd):
    # URL pública da API de DDD do BrasilAPI (Não precisa de chave/key)
    url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
    
    print(f"\n--- Conectando à API para o DDD {ddd} ---")
    
    try:
        # Requisito 1: Consumir a API usando a biblioteca requests
        resposta = requests.get(url)
        
        # Se a API responder com 404, significa que o DDD digitado não existe no Brasil
        if resposta.status_code == 404:
            print(f"❌ Erro: O DDD {ddd} não é um código de área válido no Brasil.")
            return
            
        # Dispara uma exceção para qualquer outro tipo de falha no servidor (ex: erro 500)
        resposta.raise_for_status()
        
        # Transforma a resposta JSON recebida em um dicionário Python
        dados = resposta.json()
        
        # Requisito 2: Filtrar e exibir apenas dados específicos relevantes
        estado = dados['state']       # Filtra a sigla do Estado (ex: SP, RJ, BA)
        cidades = dados['cities']     # Filtra a lista com todas as cidades do DDD
        
        print(f"\n📍 Estado localizado: {estado}")
        print(f"🏙️ Cidades que usam o DDD {ddd} (Total: {len(cidades)}):")
        print("-" * 40)
        
        # Listando as cidades de forma organizada
        for cidade in cidades:
            print(f"• {cidade}")
            
    # Requisito 3: Tratar erros de conexão e falhas HTTP
    except requests.exceptions.ConnectionError:
        print("\n❌ Erro de Rede: Verifique se o seu computador está conectado à internet!")
        
    except requests.exceptions.HTTPError as erro_http:
        print(f"\n❌ Erro HTTP encontrado: {erro_http}")
        
    except Exception as erro:
        print(f"\n❌ Ocorreu um erro imprevisto: {erro}")
        
    finally:
        print("\n--- Fim da verificação de telecomunicação ---")

# --- EXECUÇÃO DO PROJETO ---
print("=== Atividade Prática: Descobrir Cidades por DDD ===")
codigo_area = input("Digite o DDD que deseja consultar (apenas os 2 números, ex: 11): ").strip()

consultar_dados_ddd(codigo_area)