import heapq

C, V = map(int, input().split())
grafo = {i: [] for i in range(1, C + 1)}
custo_total = 0

for v in range(V):
    dados = []

    while not dados:
        dados = input().split()

    origem, destino, custo = map(int, dados)
    grafo[origem].append((destino, custo))
    grafo[destino].append((origem, custo))

print(grafo)

print(custo_total)


def dijkstra(graph: Dict, source: str) -> Tuple[Dict, Dict]:
    """
    Dijkstra O((|E| + |V|) log |V|) com heap binário.

    Parâmetros:
      graph: dicionário (lista de adjacência) representando grafo valorado com arestas não-negativas.
      source: nó de origem.

    Retorna:
      dist: dicionário com a menor distância da origem para cada nó.
            Para nós inalcançáveis, distância = float('inf').
      parent: dicionário com o predecessor imediato no caminho mínimo
              (None para a origem e para nós inalcançáveis).
    """

    # Inicialização
    processado = {v: False for v in graph.keys()}
    dist = {v: float("inf") for v in graph.keys()}
    parent = {v: None for v in graph.keys()}

    dist[source] = 0  # Origem começa com distância zero

    fila = [(0.0, source)]

    while fila:  # enquanto fila não for vazia
        du, u = heapq.heappop(fila)  # extrai nodo com menor distância na fila

        if processado[u]:
            continue
        processado[u] = True

        for v, wv in graph[u]:  # para cada vizinho v de u
            novo_dv = du + wv  # distância até u mais peso da aresta u-v
            if novo_dv < dist[v]:  # se distância menor que a atual
                dist[v] = novo_dv
                parent[v] = u
                heapq.heappush(
                    fila, (novo_dv, v)
                )  # coloca v na fila com sua distância atual da origem

    return dist, parent
