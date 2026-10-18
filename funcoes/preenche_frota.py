def define_posicoes(linha, coluna, orientacao, tamanho):

    posicao = []

    i = 0
    while i < int(tamanho):
        if orientacao == "vertical":
            posicao.append([linha+i, coluna])
        elif orientacao == "horizontal":
            posicao.append([linha, coluna+i])

        i = i + 1

    return posicao

def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):

    posicao = define_posicoes(linha, coluna, orientacao, tamanho) #chave 'nome navio' receb valores da ultima funcao(contem as posicoes)

    if nome_navio not in frota:
        frota[nome_navio] = [] #cria uma lista vazia para cada navio

    frota[nome_navio].append(posicao)

    return frota