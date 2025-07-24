import json
import os


caminho = os.path.join(os.getcwd(), "dados.json")

sn = input('Voce tem uma conta? S/N: ').strip().lower()

# Função para verificar existencia
def verificar(numero_frente, codigo):
    print('Verificando dados...')
    
    if not os.path.exists(caminho):
        print('Falha ao se comunicar com o banco de dados')
        return False

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        
        # Verifica se o número do cartão existe
        if numero_frente in dados:
            if dados[numero_frente]["codigo_seguranca"] == codigo:
                print(f"Acesso autorizado para {dados[numero_frente]['nome_completo']}")
                return True
            else:
                print("Código de segurança incorreto.")
        else:
            print("Número do cartão não encontrado.")
    
    return False

# Sistema de entrar em conta
while True:
    if sn == 's':
        numero = input('Escreva o n° do cartão:\n ')
        cod_seg = input('Escreva o código de segurança:\n ')
        entrar = verificar(numero, cod_seg)

        if entrar == True:
            print('Acesso permitido!')
            break
        else:
            print('Acesso negado! \n')
            print('Tente Novamente!\n')
    
    elif sn == 'n':
        print('processo de criar conta') # inserir dados
        break
    
    else:
        print('Não entendi oque quis dizer')
        print('Tente novamente...')
        
