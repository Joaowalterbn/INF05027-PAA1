# ============================================================
# Laboratório Avaliado 2 — Projeto e Análise de Algoritmos I
# UFRGS — Instituto de Informática
# ============================================================
# Nome: ______________________________________________________
# Cartão: ____________________________________________________
# ============================================================
#
# Instruções:
#   - Complete as funções indicadas com "# TODO".
#   - As funções de modelagem da grade (grid_para_grafo) e de
#     integração (analise_resgate) já são fornecidas prontas.
#   - Após cada função a ser implementada, indique a complexidade
#     no comentário marcado com "# Complexidade: O( )".
#     Use n para |V| (número de vértices) e m para |E| (número de arestas).
#   - Execute com: python3 lab2.py
#   - Ao implementar as funções, o script executará os testes e
#     avaliará o desempenho em um grafo em grade de 100x100,
#     gerando o arquivo "resultado_lab2.html" para inspeção visual.
#
# Regras:
#   - Não altere as assinaturas das funções nem as funções fornecidas.
#   - Utilize apenas a biblioteca padrão do Python (ex: collections.deque).
#     Não utilize bibliotecas externas como networkx ou numpy.
# ============================================================

from collections import deque
import time
import os

# Módulo visualizador auxiliar fornecido
try:
    from visualizador import gerar_visualizacao_html
except ImportError:
    gerar_visualizacao_html = None


# ============================================================
# Grafos didáticos usados nos exemplos e testes iniciais
# (Vistos na Aula 11)
# ============================================================
#
#  G1 — Caminho P4:       0 — 1 — 2 — 3
#
#  G2 — Triângulo C3:     0
#                        / \
#                       1 — 2
#
#  G3 — Desconexo (3 componentes):
#         0 — 1       2 — 3 — 4       5
#
# ============================================================

G1_list = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}

G2_list = {0: [1, 2], 1: [0, 2], 2: [0, 1]}

G3_list = {0: [1], 1: [0], 2: [3], 3: [2, 4], 4: [3], 5: []}


def init_visitados(g):
    """Dicionário mapeando todo nodo para False (não-visitado)."""
    return {n: False for n in g.keys()}


# ============================================================
# Parte 1 — BFS e Menor Caminho
# ============================================================


def bfs_caminho_minimo(grafo: dict, inicio, fim) -> tuple[int, list]:
    """
    Encontra o caminho com menor número de arestas entre 'inicio' e 'fim'
    utilizando busca em largura (BFS).

    Conceito da Aula 11:
      - A BFS percorre o grafo em níveis a partir de 'inicio'.
      - O nível em que 'fim' é visitado corresponde à distância mínima.
      - Para reconstruir a sequência de vértices do caminho, mantenha um
        dicionário de antecessores (parent), registrando o vértice que
        descobriu cada novo vizinho.
      - Ao alcançar 'fim', retorne pelos antecessores até 'inicio' e inverta
        a lista obtida.

    Parâmetros:
        grafo  : dict mapeando vértice -> lista de vizinhos
        inicio : vértice de partida
        fim    : vértice de destino

    Retorna:
        tuple[int, list] : (distancia, caminho)
            - distancia: int representando o número de arestas (-1 se inalcançável)
            - caminho: list de vértices de 'inicio' até 'fim' ([] se inalcançável)
                       Se inicio == fim, a distância é 0 e o caminho é [inicio].

    Exemplos:
        G1 = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
        bfs_caminho_minimo(G1, 0, 3) -> (3, [0, 1, 2, 3])
        bfs_caminho_minimo(G1, 2, 2) -> (0, [2])
        bfs_caminho_minimo(G3, 0, 5) -> (-1, [])
    """
    # TODO: implemente esta função usando BFS e dicionário de antecessores.
    if (
        inicio not in grafo or fim not in grafo
    ):  # Caso trivial de não ter um dos nodos # O(1)
        return (-1, [])  # O(1)

    if inicio == fim:  # O(1)
        return (0, [inicio])  # O(1)

    fila = deque([inicio])
    antecessor = {inicio: None}  # O(1)
    while fila:  # O(n)
        atual = fila.popleft()  # O(1)
        if atual == fim:  # O(1)
            break  # O(1)

        for vizinho in grafo.get(atual, []):  # O(m)
            if vizinho not in antecessor:  # O(1)
                antecessor[vizinho] = atual  # O(1)
                fila.append(vizinho)  # O(1)

    if fim not in antecessor:  # O(1)
        return [-1, []]  # O(1)

    caminho = []  # O(1)
    atual = fim  # O(1)
    while (
        atual is not None
    ):  # O(n) mas menos que n na verdade, pois percorre apenas o caminho do fim ao inicio
        caminho.append(atual)  # O(1)
        atual = antecessor[atual]  # O(1)
    caminho.reverse()  # O(?) Acho que n

    distancia = len(caminho) - 1  # O(1)
    return (distancia, caminho)  # O(1)

    # Complexidade: O(n + m)


print("=" * 60)
print("  Parte 1 — BFS e Menor Rota")
print("=" * 60)
print()
print("bfs_caminho_minimo(G1, 0, 3):")
print("  obtido  :", bfs_caminho_minimo(G1_list, 0, 3))
print("  esperado: (3, [0, 1, 2, 3])")
print()
print("bfs_caminho_minimo(G2, 0, 2):")
print("  obtido  :", bfs_caminho_minimo(G2_list, 0, 2))
print("  esperado: (1, [0, 2])")
print()


# ============================================================
# Parte 2 — Componentes Conexos
# ============================================================


def componentes_conexos(grafo: dict) -> list[list]:
    """
    Identifica todos os componentes conexos de um grafo não-dirigido.

    Conceito da Aula 11:
      - Itere sobre os vértices do grafo.
      - Para cada vértice ainda não visitado, inicie uma busca (BFS ou DFS)
        para determinar todos os vértices alcançáveis a partir dele.
      - O conjunto de vértices alcançáveis define um componente conexo.

    Parâmetros:
        grafo : dict mapeando vértice -> lista de vizinhos

    Retorna:
        list[list] : lista onde cada elemento é uma lista de vértices
                     pertencentes ao mesmo componente conexo.

    Exemplos:
        componentes_conexos(G1) -> [[0, 1, 2, 3]]
        componentes_conexos(G3) -> [[0, 1], [2, 3, 4], [5]]
    """
    # TODO: implemente esta função.
    visitados = init_visitados(grafo)
    componentes = []

    for nodo in grafo.keys():  # O(n)
        if not visitados[nodo]:  # O(1)
            caminho_atual = []  # O(1)
            stack = [nodo]  # O(1)
            visitados[nodo] = True  # O(1)

            while len(stack) > 0:  # O(m)
                n = stack.pop(-1)  # O(1)
                caminho_atual.append(n)  # O(1)
                for vizinho in grafo[n]:  # O(m)
                    if not visitados[vizinho]:  # O(1)
                        stack.append(vizinho)  # O(1)
                        visitados[vizinho] = True  # O(1)

            componentes.append(caminho_atual)  # O(1)
    return componentes  # O(1)

    # Complexidade: O(n + m)


print("=" * 60)
print("  Parte 2 — Componentes Conexos")
print("=" * 60)
print()
print("componentes_conexos(G1):")
print("  obtido  :", componentes_conexos(G1_list))
print("  esperado: [[0, 1, 2, 3]]")
print()
print("componentes_conexos(G3):")
print("  obtido  :", componentes_conexos(G3_list))
print("  esperado: [[0, 1], [2, 3, 4], [5]]")
print()


# ============================================================
# Funções Auxiliares Fornecidas
# (Não é necessário editar este bloco)
# ============================================================


def grid_para_grafo(grid: list[str]) -> tuple[dict, tuple | None, tuple | None]:
    """
    Converte uma grade de caracteres em uma lista de adjacência.
    Função auxiliar fornecida.

    Convenções da grade:
        '#' : obstáculo (não é vértice)
        '.' : célula livre (é vértice)
        'S' : ponto de partida (é vértice)
        'E' : ponto de destino (é vértice)

    Retorna:
        tuple[grafo, inicio, fim]:
            - grafo  : dict mapeando (r, c) -> lista de vizinhos [(r', c'), ...]
            - inicio : coordenada (r, c) de 'S' (ou None se ausente)
            - fim    : coordenada (r, c) de 'E' (ou None se ausente)
    """
    grafo = {}
    inicio = None
    fim = None

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            ch = grid[r][c]
            if ch != "#":
                coord = (r, c)
                grafo[coord] = []
                if ch == "S":
                    inicio = coord
                elif ch == "E":
                    fim = coord

    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r, c in grafo:
        for dr, dc in movimentos:
            vizinho = (r + dr, c + dc)
            if vizinho in grafo:
                grafo[(r, c)].append(vizinho)

    return (grafo, inicio, fim)


def analise_resgate(grid: list[str]) -> dict:
    """
    Analisa a solução do problema de busca no grid.
    """
    grafo, inicio, fim = grid_para_grafo(grid)

    if inicio is None or fim is None:
        distancia, caminho = -1, []
    else:
        distancia, caminho = bfs_caminho_minimo(grafo, inicio, fim)

    alcancavel = distancia != -1
    componentes = componentes_conexos(grafo)

    tamanho_zona_resgate = 0
    if inicio is not None:
        for comp in componentes:
            if inicio in comp:
                tamanho_zona_resgate = len(comp)
                break

    return {
        "alcancavel": alcancavel,
        "distancia": distancia,
        "caminho": caminho,
        "total_zonas": len(componentes),
        "tamanho_zona_resgate": tamanho_zona_resgate,
        "componentes": componentes,
    }


# ============================================================
# ==================== TESTES FINAIS =========================
# ============================================================


def _titulo(s):
    print(f"\n{'='*60}")
    print(f"  {s}")
    print("=" * 60)


def _ok(descricao, obtido, esperado):
    status = "✓ OK" if obtido == esperado else "✗ FALHOU"
    print(f"  [{status}] {descricao}")
    if obtido != esperado:
        print(f"          esperado : {esperado}")
        print(f"          obtido   : {obtido}")


_titulo("Testes Finais — Parte 1 (BFS Menor Caminho)")
dist_g1, cam_g1 = bfs_caminho_minimo(G1_list, 0, 3)
_ok("bfs_caminho_minimo(G1, 0, 3) - distância", dist_g1, 3)
_ok("bfs_caminho_minimo(G1, 0, 3) - caminho", cam_g1, [0, 1, 2, 3])

dist_g1_mesmo, cam_g1_mesmo = bfs_caminho_minimo(G1_list, 2, 2)
_ok(
    "bfs_caminho_minimo(G1, 2, 2) - mesmo vértice",
    (dist_g1_mesmo, cam_g1_mesmo),
    (0, [2]),
)

dist_g2, cam_g2 = bfs_caminho_minimo(G2_list, 0, 2)
_ok("bfs_caminho_minimo(G2, 0, 2) - distância", dist_g2, 1)
_ok("bfs_caminho_minimo(G2, 0, 2) - caminho direto", cam_g2, [0, 2])

dist_g3_inval, cam_g3_inval = bfs_caminho_minimo(G3_list, 0, 5)
_ok(
    "bfs_caminho_minimo(G3, 0, 5) - inalcançável",
    (dist_g3_inval, cam_g3_inval),
    (-1, []),
)


_titulo("Testes Finais — Parte 2 (Componentes Conexos)")
comps_g1 = [sorted(c) for c in componentes_conexos(G1_list)]
_ok("componentes_conexos(G1) - quantidade", len(comps_g1), 1)
if comps_g1:
    _ok("componentes_conexos(G1) - vértices", comps_g1[0], [0, 1, 2, 3])

comps_g3 = sorted([sorted(c) for c in componentes_conexos(G3_list)])
comps_g3_esp = sorted([[0, 1], [2, 3, 4], [5]])
_ok("componentes_conexos(G3) - componentes", comps_g3, comps_g3_esp)


_titulo("Testes Finais — Integração (Grade Didática)")
mapa_mini = ["S..#.", "#.##.", "..E#."]
analise_mini = analise_resgate(mapa_mini)
_ok("analise_resgate(mapa_mini) - alcancavel", analise_mini["alcancavel"], True)
_ok("analise_resgate(mapa_mini) - distancia", analise_mini["distancia"], 4)
_ok(
    "analise_resgate(mapa_mini) - caminho",
    analise_mini["caminho"],
    [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)],
)
_ok("analise_resgate(mapa_mini) - total_zonas", analise_mini["total_zonas"], 2)
_ok(
    "analise_resgate(mapa_mini) - tamanho_zona_resgate",
    analise_mini["tamanho_zona_resgate"],
    7,
)

mapa_bloqueado = ["S#.", "###", "..E"]
analise_bloq = analise_resgate(mapa_bloqueado)
_ok("analise_resgate(mapa_bloqueado) - inalcançável", analise_bloq["alcancavel"], False)
_ok("analise_resgate(mapa_bloqueado) - distancia -1", analise_bloq["distancia"], -1)


# ============================================================
# EXECUÇÃO NO GRAFO EM GRADE (100x100)
# ============================================================

_titulo("Execução no Grafo em Grade (100x100)")

caminho_mapa = os.path.join(os.path.dirname(__file__), "mapa_grande.txt")
if os.path.exists(caminho_mapa):
    with open(caminho_mapa, "r", encoding="utf-8") as f:
        grid_grande = [linha.strip() for linha in f if linha.strip()]

    print(
        f"  Grade carregada: {len(grid_grande)} linhas x {len(grid_grande[0])} colunas."
    )

    t0 = time.perf_counter()
    resultado_grande = analise_resgate(grid_grande)
    tempo_total = (time.perf_counter() - t0) * 1000

    grafo_g, _, _ = grid_para_grafo(grid_grande)
    num_vertices = len(grafo_g)
    num_arestas = sum(len(viz) for viz in grafo_g.values()) // 2 if grafo_g else 0

    print(f"  Grafo gerado: |V| = {num_vertices} vértices, |E| = {num_arestas} arestas")

    if resultado_grande["alcancavel"] or resultado_grande["total_zonas"] > 0:
        print(
            f"  Tempo de processamento (BFS + componentes conexos): {tempo_total:.2f} ms"
        )
        print(f"  Destino alcançável: {resultado_grande['alcancavel']}")
        print(f"  Menor distância até destino: {resultado_grande['distancia']} passos")
        print(f"  Total de componentes conexos: {resultado_grande['total_zonas']}")
        print(
            f"  Tamanho da componente da partida: {resultado_grande['tamanho_zona_resgate']} células"
        )

        if gerar_visualizacao_html is not None:
            arquivo_html = os.path.join(
                os.path.dirname(__file__), "resultado_lab2.html"
            )
            gerar_visualizacao_html(
                grid=grid_grande,
                caminho=resultado_grande["caminho"],
                componentes=resultado_grande["componentes"],
                arquivo_saida=arquivo_html,
            )
            print()
            print(f"  Visualização gerada em: {arquivo_html}")
    else:
        print()
        print("  Implemente as funções das Partes 1 e 2 para executar o teste")
        print("  na grade de 100x100 e gerar a visualização correspondente.")
else:
    print(f"  Arquivo {caminho_mapa} não encontrado.")
print()
