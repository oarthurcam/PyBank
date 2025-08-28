import func

contador = 0

sn = input('Voce tem uma conta? S/N: ').strip().lower()

# Sistema de entrar em conta
while True:
    if sn == 's':
        numero = input('Escreva o n° do cartão:\n ')
        cod_seg = input('Escreva o código de segurança:\n ')
        
        dados = func.carregar_dados()
        entrar = func.verificar(numero, cod_seg, dados)
        
        # Usuário entro no sitema
        if entrar == True:
            
            # Ação do usuário
            while True:
                escolha = int(input('(1) transferir\n(2) Investir\n(3) Sair \n Digite um numero para selecionar a opção: '))
                
                if escolha == 1:
                    func.transferir(numero, dados) 
                    

 
                #elif escolha == 2:
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
