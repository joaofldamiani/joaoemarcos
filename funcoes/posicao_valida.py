from define_posicoes import define_posicoes



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