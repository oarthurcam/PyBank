import json
import os

contador = 0
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
                print(f"Acesso autorizado para {dados[numero_frente]['nome_completo']} seu saldo atual é de R$ {dados[numero_frente]['saldo']}")
                return True
        else:
            print("Número do cartão ou código não encontrado.")
    
    return False


# Sistema de entrar em conta
while True:
    if sn == 's':
        numero = input('Escreva o n° do cartão:\n ')
        cod_seg = input('Escreva o código de segurança:\n ')
        entrar = verificar(numero, cod_seg)
        
        # Usuário entro no sitema
        if entrar == True:
            
            # Ação do usuário
            while True:
                escolha = int(input('(1) transferir\n(2) Investir\n(3) Sair \n Digite um numero para selecionar a opção: '))
                
                if escolha == 1:
 
                elif escolha == 2:
                    investir = input('Qual de nossas opções\n')

                elif escolha == 3:
                    break
                else:
                    print('Tente novamente...\n')
                    contador += 1

                    if contador > 2:
                        break
                
        # Usuário errou os dados
        else:
            print('Acesso negado! \n')
            print('Tente Novamente!')
            contador += 1
            
            if contador > 2:
                print('Houve um excesso de tentativas tente novamente mais tarde')
                break
    
    # Criar conta
    elif sn == 'n':
        print('processo de criar conta') 
        break
    
    else:
        print('Não entendi oque quis dizer')
        break # inves de usar break usar algo para retornar , exceto se for maior que 3 tentativas
