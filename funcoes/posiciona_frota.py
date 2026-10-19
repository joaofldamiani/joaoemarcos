
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