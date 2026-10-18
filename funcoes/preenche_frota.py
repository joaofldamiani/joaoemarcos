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
frota = {
  "navio-tanque":[
    [[6,1],[6,2],[6,3]]
  ]
}
nome_navio = 'navio-tanque'
linha = 4
coluna = 7
orientacao = 'vertical'
tamanho = 3

def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):

    frota[nome_navio] = define_posicoes(linha, coluna, orientacao, tamanho) #chave 'nome navio' receb valores da ultima funcao(contem as posicoes)

    return frota

print(preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho))


