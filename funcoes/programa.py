from funcoes import (monta_tabuleiros, posicao_valida, posiciona_frota, preenche_frota, faz_jogada, afundados)


frota = {}

# nome, tamanho, quantidade
embarcacoes = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4),
]

for nome, tamanho, quantidade in embarcacoes:
    for i in range(quantidade):
        posicionado = False

        while not posicionado:
            print(
                f"Insira as informações referentes ao navio {nome} "
                f"que possui tamanho {tamanho}s"
            )

            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome == "submarino":
                orientacao = "vertical"
            else:
                escolha = int(
                    input("Orientação (1 vertical, 2 horizontal): ")
                )

                if escolha == 1:
                    orientacao = "vertical"
                elif escolha == 2:
                    orientacao = "horizontal"
                else:
                    print("Esta posição não está válida!")
                    continue

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(
                    frota, nome, linha, coluna, orientacao, tamanho
                )
                posicionado = True
            else:
                print("Esta posição não está válida!")

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    tiro_valido = False

    while  tiro_valido == False:
        linha = int(input("Linha: "))

        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Linha: "))

        coluna = int(input("Coluna: "))

        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Coluna: "))

        if tabuleiro_oponente[linha][coluna] in ("X", "-"):
            print(
                f"A posição linha {linha} e coluna {coluna} "
                "já foi informada anteriormente!"
            )
        else:
            tiro_valido = True

    tabuleiro_oponente = faz_jogada(
        tabuleiro_oponente, linha, coluna
    )

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False