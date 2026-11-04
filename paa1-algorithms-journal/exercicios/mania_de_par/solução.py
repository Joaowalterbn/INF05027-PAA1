import heapq

def dijkstra(graph, source: str, destino):
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
    processado = {(v, p): False for v in graph.keys() for p in (0, 1)}
    dist = {(v,p): float("inf") for v in graph.keys() for p in (0, 1)}
    parent = {(v,p): None for v in graph.keys() for p in (0, 1)}

    dist[source, 0] = 0  # Origem começa com distância zero
    fila = [(0, source, 0)] # Dist, nodo e paridade

    while fila:  # enquanto fila não for vazia
        du, u, paridade = heapq.heappop(fila)  # extrai nodo com menor distância na fila
        if processado[u, paridade]:
            continue
        processado[u, paridade] = True

        if u == destino and paridade == 0:
            return du

        for v, wv in graph[u]:  # para cada vizinho v de u
            nova_paridade = 1 - paridade
            novo_dv = du + wv  # distância até u mais peso da aresta u-v
            if novo_dv < dist[v, nova_paridade]:  # se distância menor que a atual
                dist[v, nova_paridade] = novo_dv
                parent[v, nova_paridade] = u
                heapq.heappush(
                    fila, (novo_dv, v, nova_paridade)
                )  # coloca v na fila com sua distância atual da origem

    return -1

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
print(dijkstra(grafo, 1, C))
