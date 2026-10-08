"""
Entrada:
    Valor de T
    Valor de N(Total de Renas) e M(Quantas vão puxar o trenó)
    Renas:
        Str(Nome) int(Peso) int(Idade) float(Altura)

Saída:
    Cenário {i} i -> i valor de T do loop atual
    1 - Primeira rena com menor peso
    Caso de empate -> Deve-se olhar para a idade e ordenar de forma ascendente
    Caso de empate 2 -> Deve-se ordenar baseado na altura de forma ascendente
    Caso de empate 3 -> Ordem alfabética(Dar to lower e comparar letra a letra os valores do char)

"""


class Rena:
    def __init__(self, nome, peso, idade, altura):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.altura = altura


T = int(input())

for cenario in range(T):
    N, M = map(int, input().split())
    ranking = []
    for rena in range(N):
        dados = input().split()
        ranking.append(Rena(dados[0], int(dados[1]), int(dados[2]), float(dados[3])))

    ranking.sort(key=lambda r: (-r.peso, r.idade, r.altura, r.nome))
    print(f"CENARIO {{{cenario + 1}}}")

    for pos in range(M):
        print(f"{pos + 1} - {ranking[pos].nome}")
