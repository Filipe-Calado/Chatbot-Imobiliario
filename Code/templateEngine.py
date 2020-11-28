import time

def chatbotEngine(inicio=1):
    if inicio == 1:
        print('INICIANDO.....\n')
        print('Olá Queridxs! Prazer, sou o UFBot, vou te ajudar a analisar o preço de algumas casas. Vamos lá?\n')
    else:
        print('Eu de novo! rsrs\n')
        print('REINICIANDO.....\n')
        
    while True:
        time.sleep(1)
        
        def validaEntrada(pergunta):
            print('Digite 0 para SIM, 1 para NÃO e 2 para VOLTAR AO INÍCIO\n')
            escolha = int(input(pergunta+'\n'))
            if escolha != 0 and escolha != 1 and escolha!=2:
                print('Digite um valor válido!\n')
                validaEntrada(pergunta)
            elif escolha == 2:
                chatbotEngine(inicio=2)
            else:
                return escolha