N = int(input())

for caso in range(N):
    V, E = map(int, input().split())
    grafo = {chr(ord("a") + i): [] for i in range(V)}
    componentes = []

    print(f"Case #{caso + 1}:")

    for _ in range(E):
        origem, destino = input().split()
        grafo[origem].append(destino)
        grafo[destino].append(origem)

    visitados = set()

    for vertice in grafo:
        if vertice not in visitados:
            componente_atual = []
            pilha = [vertice]
            visitados.add(vertice)

            while pilha:
                x = pilha.pop()
                componente_atual.append(x)

                for vizinho in grafo[x]:
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        pilha.append(vizinho)

            componente_atual.sort()
            componentes.append(componente_atual)
            print(",".join(componente_atual) + ",")

    print(f"{len(componentes)} connected components\n")
