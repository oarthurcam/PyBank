import os
import json

caminho = os.path.join(os.getcwd(), "banco\dados.json")

# função de carregar os dados do banco
def carregar_dados():
    if not os.path.exists(caminho):
        print('Falha ao se comunicar com o banco de dados')
        return None   # melhor que False, porque depois vc espera um dicionário
    
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


# função de verificar os dados do usuário
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

    
    
# função de transferir dinheiro para outro usuário
def transferir(numero_frente, dados):
    if numero_frente in dados:
        contatos = dados[numero_frente]["contatos"]

        print("=== Lista de contatos ===")

        for i, contato in enumerate(contatos, start=1):
            print(f"({i}) {contato['nome']} - Cartão: {contato['cartao']} - Banco: {contato['banco']}")

        try:
            escolha = int(input("Digite o número do contato: ")) - 1
            if 0 <= escolha < len(contatos):
                escolhido = contatos[escolha]
                print(f"Você escolheu transferir para: {escolhido['nome']} ({escolhido['banco']})\nSeu saldo atual é de R$ {dados[numero_frente]['saldo']}")

                valor = float(input('Insira o valor que deseja enviar: '))
                
                if valor > dados[numero_frente]['saldo']:
                    print('valor eh maior que o saldo')
                
                else:
                    dados[numero_frente]['saldo'] -= valor
                    escolhido['saldo'] += valor

                    print(f'Transferência de R$ {valor} para {escolhido["nome"]} realizada com sucesso!')
                    print(f'Seu novo saldo é de R$ {dados[numero_frente]["saldo"]}')


            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
    else:
        print("Conta não encontrada.")
