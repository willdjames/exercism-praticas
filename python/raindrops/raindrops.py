def convert(number):

    saida = ''

    nao_entrou_no_if = True

    if (number % 3) == 0:
        saida += 'Pling'
        nao_entrou_no_if = False

    if (number % 5) == 0:
        saida += 'Plang'
        nao_entrou_no_if = False

    if (number % 7) == 0:
        saida += 'Plong'
        nao_entrou_no_if = False

    if nao_entrou_no_if :
        saida = str(number)
    
    return saida
