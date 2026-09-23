# ============================================================
# Laboratório Avaliado 1 — Projeto e Análise de Algoritmos I
# UFRGS — Instituto de Informática
# ============================================================
# Nome: João Walter Backes Nunes
# Cartão: 00312383
# ============================================================
#
# Instruções:
#   - Complete as funções indicadas com "# TODO".
#   - Após cada função, indique a complexidade no comentário
#     marcado com "# Complexidade:".
#   - Execute com: python3 lab1.py
#   - Ao implementar uma função, o exemplo logo abaixo dela
#     imprimirá o resultado. Use isso para verificar sua lógica!
#
# Representações usadas neste lab:
#   - Lista de adjacência: dict mapeando vértice -> list[vértice]
#   - Matriz de adjacência: list[list[int]] onde M[i][j] = 1
#       se existe aresta {i,j}, 0 caso contrário.
#       Os vértices são inteiros 0..n-1.
# ============================================================


# ============================================================
# Grafos usados nos exemplos e testes
# ============================================================
#
#  G1 — Caminho P4          G2 — Triângulo C3
#
#   0 — 1 — 2 — 3            0
#                            / \
#                           1 — 2
#
#  G3 — Estrela K_{1,3}     G4 — Grafo com vértice isolado
#
#       1                    0 — 1    2    3 — 4
#       |
#   3 — 0 — 2
#
# ============================================================

G1_list = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
G1_n = 4

G2_list = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
G2_n = 3

G3_list = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0]}
G3_n = 4

G4_list = {0: [1], 1: [0], 2: [], 3: [4], 4: [3]}
G4_n = 5


# ============================================================
# Parte 1 — Conversões entre representações
# ============================================================


def adj_list_to_matrix(adj_list: dict[int, list[int]], n: int) -> list[list[int]]:
    """
    Converte uma lista de adjacência para uma matriz de adjacência.

    Parâmetros:
        adj_list : dict[int, list[int]]  — lista de adjacência (vértices 0..n-1)
        n        : int                   — número de vértices

    Retorna:
        list[list[int]]  — matriz de adjacência n x n

    Exemplo:
        adj_list = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}   (G1)
        n = 4
        resultado esperado:
            [[0, 1, 0, 0],
             [1, 0, 1, 0],
             [0, 1, 0, 1],
             [0, 0, 1, 0]]
    """
    # TODO: implemente esta função.

    # Ou

    matriz = [[0 for i in range(n)] for j in range(n)]  # Complexidade da linha = O(n²)

    for i in range(n):  # Complexidade: O(n)
        for vizinho in adj_list[i]:  # O(m)?
            matriz[i][vizinho] = 1
            matriz[vizinho][i] = 1
    return matriz
    pass

    # Complexidade: O(n²) (Fica a maior complexidade)


print("=" * 55)
print("  Parte 1 — Conversões")
print("=" * 55)
print()
print("adj_list_to_matrix(G1):")
print(" ", adj_list_to_matrix(G1_list, G1_n))
print("  esperado: [[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]]")
print()


def adj_matrix_to_list(matrix: list[list[int]]) -> dict[int, list[int]]:
    """
    Converte uma matriz de adjacência para uma lista de adjacência.

    Parâmetros:
        matrix : list[list[int]]  — matriz de adjacência n x n

    Retorna:
        dict[int, list[int]]  — lista de adjacência resultante

    Exemplo:
        matrix = [[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]]   (G1)
        resultado esperado:
            {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
    """
    # TODO: implemente esta função.
    adj = {}  # O(1)
    n = len(matrix)  # O(1)
    for i in range(n):  # O(n)
        adj[i] = []  # O(1)
        for j in range(n):  # O(n)
            if matrix[i][j] == 1:  # O(1)
                adj[i].append(j)  # O(1)??
    return adj
    pass
    # Como o for interior executa n vezes e o de fora n vezes, então ficará n²
    # Complexidade: O(n²)


G1_matrix = [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
print("adj_matrix_to_list(G1_matrix):")
print(" ", adj_matrix_to_list(G1_matrix))
print("  esperado: {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}")
print()


# ============================================================
# Parte 2 — Graus
# ============================================================


def grau_lista(adj_list: dict[int, list[int]], v: int) -> int:
    """
    Calcula o grau do vértice v usando a lista de adjacência.

    Parâmetros:
        adj_list : dict[int, list[int]]
        v        : int  — vértice de interesse

    Retorna:
        int  — grau de v
    """
    # TODO: implemente esta função.
    return len(adj_list[v])
    pass

    # Complexidade: O(1) Comentado em aula, toda lista tem uma propriedade que guarda o tamanho


def grau_matriz(matrix: list[list[int]], v: int) -> int:
    """
    Calcula o grau do vértice v usando a matriz de adjacência.

    Parâmetros:
        matrix : list[list[int]]
        v      : int  — vértice de interesse

    Retorna:
        int  — grau de v
    """
    # TODO: implemente esta função.
    cont = 0
    for i in matrix[v]:  # O(n)
        if i == 1:  # O(1)
            cont += 1  # O(1)
    return cont  # O(1)
    pass

    # Complexidade: O(n)


def sequencia_de_graus(adj_list: dict[int, list[int]]) -> list[int]:
    """
    Retorna os graus de todos os vértices em ordem não-decrescente.

    Parâmetros:
        adj_list : dict[int, list[int]]

    Retorna:
        list[int]  — sequência de graus ordenada

    Exemplo (G1):
        resultado esperado: [1, 1, 2, 2]
    """
    # TODO: implemente esta função.
    num_arestas = []  # O(1)
    for i in adj_list:  # O(n), para cada nodo, analisa a sua lista
        num_arestas.append(len(adj_list[i]))  # O(1)?
    num_arestas.sort()  # O(n log n) segundo o google
    return num_arestas  # O(1)
    pass

    # Complexidade: O(n log n)


print("=" * 55)
print("  Parte 2 — Graus")
print("=" * 55)
print()
print("grau_lista(G1, vértice 0):", grau_lista(G1_list, 0), "  (esperado: 1)")
print("grau_lista(G1, vértice 1):", grau_lista(G1_list, 1), "  (esperado: 2)")
print("grau_lista(G3, vértice 0):", grau_lista(G3_list, 0), "  (esperado: 3)")
print()
print("grau_matriz(G1, vértice 0):", grau_matriz(G1_matrix, 0), "  (esperado: 1)")
print("grau_matriz(G1, vértice 1):", grau_matriz(G1_matrix, 1), "  (esperado: 2)")
print()
print(
    "sequencia_de_graus(G1):", sequencia_de_graus(G1_list), "  (esperado: [1, 1, 2, 2])"
)
print("sequencia_de_graus(G2):", sequencia_de_graus(G2_list), "  (esperado: [2, 2, 2])")
print(
    "sequencia_de_graus(G3):", sequencia_de_graus(G3_list), "  (esperado: [1, 1, 1, 3])"
)
print()


# ============================================================
# Parte 3 — Propriedades básicas
# ============================================================


def eh_regular(adj_list: dict[int, list[int]]) -> bool:
    """
    Verifica se o grafo é regular (todos os vértices têm o mesmo grau).

    Parâmetros:
        adj_list : dict[int, list[int]]

    Retorna:
        bool  — True se regular, False caso contrário

    Exemplos:
        G2 (triângulo, todos com grau 2) -> True
        G1 (caminho, graus variados)     -> False
    """
    # TODO: implemente esta função.
    lista = sequencia_de_graus(adj_list)  # O(n log n)
    return len(set(lista)) == 1  # O(n)
    pass

    # Complexidade: O(n log n)


def conta_arestas(adj_list: dict[int, list[int]]) -> int:
    """
    Conta o número de arestas do grafo (não-dirigido).

    Lembrete: a aresta {u,v} aparece na lista de u E de v.
    Cuidado para não contar duas vezes!

    Parâmetros:
        adj_list : dict[int, list[int]]

    Retorna:
        int  — número de arestas

    Exemplos:
        G1 -> 3   G2 -> 3   G3 -> 3
    """
    # TODO: implemente esta função.
    lista = sequencia_de_graus(adj_list)  # O(n log n)
    soma = 0  # O(1)
    for (
        i
    ) in (
        lista
    ):  # O(n) executa o numero de graus de vezes, como todos os nodos tem grau, ent n vezes
        soma += i  # O(1)
    return soma / 2  # O(1)
    pass

    # Complexidade: O(n log n)


def vertices_isolados(adj_list: dict[int, list[int]]) -> list[int]:
    """
    Retorna a lista de vértices com grau 0.

    Parâmetros:
        adj_list : dict[int, list[int]]

    Retorna:
        list[int]  — vértices isolados, em qualquer ordem

    Exemplo (G4):
        G4 = {0:[1], 1:[0], 2:[], 3:[4], 4:[3]}
        resultado esperado: [2]
    """
    # TODO: implemente esta função.
    vazios = []  # O(1)
    for i in adj_list:  # O(n)
        if len(adj_list[i]) == 0:  # O(1)
            vazios.append(i)  # O(1)
    return vazios  # O(1)
    return []

    # Complexidade: O(n)


def vertice_de_grau_maximo(adj_list: dict[int, list[int]]) -> int:
    """
    Retorna o vértice de maior grau. Em empate, retorna o menor índice.

    Parâmetros:
        adj_list : dict[int, list[int]]

    Retorna:
        int  — vértice de grau máximo

    Exemplos:
        G1 -> 1  (grau 2; vértices 1 e 2 empatam, retorna 1)
        G3 -> 0  (grau 3)
    """
    # TODO: implemente esta função.
    num_arestas = []  # O(1)
    for i in adj_list:  # O(n)
        num_arestas.append(len(adj_list[i]))  # O(1)
    return num_arestas.index(max(num_arestas))  # O(n))
    pass

    # Complexidade: O(n)


print("=" * 55)
print("  Parte 3 — Propriedades básicas")
print("=" * 55)
print()
print("eh_regular(G2 — triângulo):", eh_regular(G2_list), "  (esperado: True)")
print("eh_regular(G1 — caminho)  :", eh_regular(G1_list), "  (esperado: False)")
print("eh_regular(G3 — estrela)  :", eh_regular(G3_list), "  (esperado: False)")
print()
print("conta_arestas(G1):", conta_arestas(G1_list), "  (esperado: 3)")
print("conta_arestas(G2):", conta_arestas(G2_list), "  (esperado: 3)")
print("conta_arestas(G3):", conta_arestas(G3_list), "  (esperado: 3)")
print()
print("vertices_isolados(G4):", vertices_isolados(G4_list), "  (esperado: [2])")
print("vertices_isolados(G2):", vertices_isolados(G2_list), "  (esperado: [])")
print()
print("vertice_de_grau_maximo(G1):", vertice_de_grau_maximo(G1_list), "  (esperado: 1)")
print("vertice_de_grau_maximo(G3):", vertice_de_grau_maximo(G3_list), "  (esperado: 0)")
print()


# ============================================================
# Parte 4 — Handshaking
# ============================================================


def verifica_handshaking(adj_list: dict[int, list[int]]) -> bool:
    """
    Verifica o Lema do Aperto de Mãos:
        Σ deg(v) = 2 * |E|

    Para um grafo simples não-dirigido bem formado, isso deve
    ser sempre verdade. Use esta função para validar a entrada.

    Dica: use conta_arestas() e grau_lista() que você já implementou.

    Parâmetros:
        adj_list : dict[int, list[int]]

    Retorna:
        bool  — True se o lema for satisfeito
    """
    # TODO: implemente esta função usando conta_arestas e grau_lista.
    soma_grau = 0
    for i in adj_list:  # O(n)
        soma_grau += len(adj_list[i])  # O(1)

    return soma_grau == 2 * conta_arestas(
        adj_list
    )  # O(n log n) por conta da função conta_arestas
    pass

    # Complexidade: O(n log n)


print("=" * 55)
print("  Parte 4 — Handshaking")
print("=" * 55)
print()
print("verifica_handshaking(G1):", verifica_handshaking(G1_list), "  (esperado: True)")
print("verifica_handshaking(G2):", verifica_handshaking(G2_list), "  (esperado: True)")
print("verifica_handshaking(G3):", verifica_handshaking(G3_list), "  (esperado: True)")
print("verifica_handshaking(G4):", verifica_handshaking(G4_list), "  (esperado: True)")
print()


# ============================================================
# ==================== TESTES FINAIS =========================
# ============================================================


def _titulo(s):
    print(f"\n{'='*55}")
    print(f"  {s}")
    print("=" * 55)


def _ok(descricao, obtido, esperado):
    status = "✓ OK" if obtido == esperado else "✗ FALHOU"
    print(f"  [{status}] {descricao}")
    if obtido != esperado:
        print(f"          esperado : {esperado}")
        print(f"          obtido   : {obtido}")


_titulo("Testes Finais — Parte 1")
G1_matrix_esp = [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
G2_matrix_esp = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
_ok("adj_list_to_matrix(G1)", adj_list_to_matrix(G1_list, G1_n), G1_matrix_esp)
_ok("adj_matrix_to_list(G1)", adj_matrix_to_list(G1_matrix_esp), G1_list)
_ok("adj_list_to_matrix(G2)", adj_list_to_matrix(G2_list, G2_n), G2_matrix_esp)
_ok("adj_matrix_to_list(G2)", adj_matrix_to_list(G2_matrix_esp), G2_list)

_titulo("Testes Finais — Parte 2")
_ok("grau_lista(G1, 0)", grau_lista(G1_list, 0), 1)
_ok("grau_lista(G1, 1)", grau_lista(G1_list, 1), 2)
_ok("grau_lista(G3, 0)", grau_lista(G3_list, 0), 3)
_ok("grau_lista(G3, 2)", grau_lista(G3_list, 2), 1)
_ok("grau_matriz(G1, 0)", grau_matriz(G1_matrix_esp, 0), 1)
_ok("grau_matriz(G1, 1)", grau_matriz(G1_matrix_esp, 1), 2)
_ok("sequencia_de_graus(G1)", sequencia_de_graus(G1_list), [1, 1, 2, 2])
_ok("sequencia_de_graus(G2)", sequencia_de_graus(G2_list), [2, 2, 2])
_ok("sequencia_de_graus(G3)", sequencia_de_graus(G3_list), [1, 1, 1, 3])

_titulo("Testes Finais — Parte 3")
_ok("eh_regular(G2)", eh_regular(G2_list), True)
_ok("eh_regular(G1)", eh_regular(G1_list), False)
_ok("eh_regular(G3)", eh_regular(G3_list), False)
_ok("conta_arestas(G1)", conta_arestas(G1_list), 3)
_ok("conta_arestas(G2)", conta_arestas(G2_list), 3)
_ok("conta_arestas(G3)", conta_arestas(G3_list), 3)
_ok("vertices_isolados(G4)", sorted(vertices_isolados(G4_list)), [2])
_ok("vertices_isolados(G2)", vertices_isolados(G2_list), [])
_ok("vertice_de_grau_maximo(G1)", vertice_de_grau_maximo(G1_list), 1)
_ok("vertice_de_grau_maximo(G3)", vertice_de_grau_maximo(G3_list), 0)

_titulo("Testes Finais — Parte 4")
_ok("verifica_handshaking(G1)", verifica_handshaking(G1_list), True)
_ok("verifica_handshaking(G2)", verifica_handshaking(G2_list), True)
_ok("verifica_handshaking(G3)", verifica_handshaking(G3_list), True)
_ok("verifica_handshaking(G4)", verifica_handshaking(G4_list), True)
print()
