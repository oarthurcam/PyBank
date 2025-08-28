import os
import json

caminho = os.path.join(os.getcwd(), "banco\dados.json")

def carregar_dados():
    if not os.path.exists(caminho):
        print('Falha ao se comunicar com o banco de dados')
        return None   # melhor que False, porque depois vc espera um dicionário
    
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)



def verificar(numero_frente, codigo, dados):
    print('Verificando dados...')
    
        # Verifica se o número do cartão existe
    if numero_frente in dados:

        if dados[numero_frente]["codigo_seguranca"] == codigo:
                
            print(f"Acesso autorizado para {dados[numero_frente]['nome_completo']} seu saldo atual é de R$ {dados[numero_frente]['saldo']}")
            return True
    else:
        print("Número do cartão ou código não encontrado.")
    
    return False

def transferir(numero_frente, dados):
    if numero_frente in dados:
        contatos = dados[numero_frente]["contatos"]

        print("=== Lista de contatos ===")
