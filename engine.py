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

        locationsdiscretized = float(validaEntrada('Is the location discretized <= 0.5?'))
        if locationsdiscretized <= 0.5:
            sqftlivingdiscretized = float(validaEntrada('Is the number of sqft living <= 2858.22?'))
            if sqftlivingdiscretized <= 0.5:
                bathroomsdiscretized = float(validaEntrada('Is the number of bathrooms <= 2.8?'))
                if bathroomsdiscretized <= 0.5:
                    gradediscretized = float(validaEntrada('Is the grade <= 8.58?'))
                    if gradediscretized <= 0.5:
                        bedroomsdiscretized = float(validaEntrada('Is the number of bedrooms <= 3.56?'))
                        if bedroomsdiscretized <= 0.5:
                            sqftabovediscretized = float(validaEntrada('Is the number of sqft above <= 2408.84?'))
                            if sqftabovediscretized <= 0.5:
                                return(0)
                            else:  # if sqftabovediscretized > 0.5
                                return(0)
                        else:  # if bedroomsdiscretized > 0.5
                            sqftabovediscretized = float(validaEntrada('Is the number of sqft above <= 2408.84?'))
                            if sqftabovediscretized <= 0.5:
                                return(0)
                            else:  # if sqftabovediscretized > 0.5
                                return(1)
                    else:  # if gradediscretized > 0.5
                        bedroomsdiscretized = float(validaEntrada('Is the number of bedrooms <= 3.56?'))
                        if bedroomsdiscretized <= 0.5:
                            return(0)
                        else:  # if bedroomsdiscretized > 0.5
                            return(2)
                else:  # if bathroomsdiscretized > 0.5
                    viewdiscretized = float(validaEntrada('Is the view classified as <= 1.27?'))
                    if viewdiscretized <= 0.5:
                        return(0)
                    else:  # if viewdiscretized > 0.5
                        return(0)
            else:  # if sqftlivingdiscretized > 0.5
                waterfrontdiscretized = float(validaEntrada('Is the waterfront classification <= 0.5?'))
                if waterfrontdiscretized <= 0.5:
                    sqftliving15discretized = float(validaEntrada('Is the number sqft living 15 <= 2554.55?'))
                    if sqftliving15discretized <= 0.5:
                        return(1)
                    else:  # if sqftliving15discretized > 0.5
                        bathroomsdiscretized = float(validaEntrada('Is the number of bathrooms <= 2.8?'))
                        if bathroomsdiscretized <= 0.5:
                            gradediscretized = float(validaEntrada('Is the grade <= 8.58?'))
                            if gradediscretized <= 0.5:
                                return(0)
                            else:  # if gradediscretized > 0.5
                                return(0)
                        else:  # if bathroomsdiscretized > 0.5
                            sqftabovediscretized = float(validaEntrada('Is the number of sqft above <= 2408.84?'))
                            if sqftabovediscretized <= 0.5:
                                return(0)
                            else:  # if sqftabovediscretized > 0.5
                                return(1)
                else:  # if waterfrontdiscretized > 0.5
                    return(2)
        else:  # if locationsdiscretized > 0.5
            gradediscretized = float(validaEntrada('Is the grade <= 8.58?'))
            if gradediscretized <= 0.5:
                sqftlivingdiscretized = float(validaEntrada('Is the number of sqft living <= 2858.22?'))
                if sqftlivingdiscretized <= 0.5:
                    bedroomsdiscretized = float(validaEntrada('Is the number of bedrooms <= 3.56?'))
                    if bedroomsdiscretized <= 0.5:
                        return(1)
                    else:  # if bedroomsdiscretized > 0.5
                        return(0)
                else:  # if sqftlivingdiscretized > 0.5
                    return(1)
            else:  # if gradediscretized > 0.5
                viewdiscretized = float(validaEntrada('Is the view classified as <= 1.27?'))
                if viewdiscretized <= 0.5:
                    bathroomsdiscretized = float(validaEntrada('Is the number of bathrooms <= 2.8?'))
                    if bathroomsdiscretized <= 0.5:
                        bedroomsdiscretized = float(validaEntrada('Is the number of bedrooms <= 3.56?'))
                        if bedroomsdiscretized <= 0.5:
                            sqftabovediscretized = float(validaEntrada('Is the number of sqft above <= 2408.84?'))
                            if sqftabovediscretized <= 0.5:
                                return(1)
                            else:  # if sqftabovediscretized > 0.5
                                return(0)
                        else:  # if bedroomsdiscretized > 0.5
                            sqftlivingdiscretized = float(validaEntrada('Is the number of sqft living <= 2858.22?'))
                            if sqftlivingdiscretized <= 0.5:
                                return(0)
                            else:  # if sqftlivingdiscretized > 0.5
                                return(1)
                    else:  # if bathroomsdiscretized > 0.5
                        bedroomsdiscretized = float(validaEntrada('Is the number of bedrooms <= 3.56?'))
                        if bedroomsdiscretized <= 0.5:
                            return(1)
                        else:  # if bedroomsdiscretized > 0.5
                            return(0)
                else:  # if viewdiscretized > 0.5
                    return(0)
