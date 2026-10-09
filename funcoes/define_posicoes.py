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