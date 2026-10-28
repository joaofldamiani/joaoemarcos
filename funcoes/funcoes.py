def afundados(frota, tabuleiro):
    afundados = 0

    for navio in frota:
        for posicao in frota[navio]:
            acertos = 0
            i = 0

            while i < len(posicao):
                linha = posicao[i][0]
                coluna = posicao[i][1]
                i = i + 1

                if tabuleiro[linha][coluna] == "X":
                    acertos = acertos + 1


            if acertos == len(posicao):
                afundados = afundados + 1

    return afundados

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

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"

    return tabuleiro



def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in novas_posicoes:
        linha_atual = posicao[0]
        coluna_atual = posicao[1]

        # Verifica se a casa está fora do tabuleiro
        if linha_atual < 0 or linha_atual > 9:
            return False

        if coluna_atual < 0 or coluna_atual > 9:
            return False

        # Verifica se a casa já está ocupada
        for lista_de_navios in frota.values():
            for navio in lista_de_navios:
                if posicao in navio:
                    return False
    return True


def posiciona_frota(frota):
    tabuleiro = []

    for i in range(10):
        linha = [0] * 10
        tabuleiro.append(linha)

    for navio in frota:
        for posicao in frota[navio]:
            i = 0
            while i < len(posicao):
                linha = posicao[i][0]
                coluna = posicao[i][1]
                tabuleiro[linha][coluna] = 1
                i = i + 1

    return tabuleiro



def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):

    posicao = define_posicoes(linha, coluna, orientacao, tamanho) #chave 'nome navio' receb valores da ultima funcao(contem as posicoes)

    if nome_navio not in frota:
        frota[nome_navio] = [] #cria uma lista vazia para cada navio

    frota[nome_navio].append(posicao)

    return frota