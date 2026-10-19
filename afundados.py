
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