from funcoes import (posicao_valida, preenche_frota, posiciona_frota, faz_jogada,
                      define_posicoes, afundados)


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
                f"que possui tamanho {tamanho}."
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

print(frota)