import heapq
import random

def prim(adj, valorado: bool):
    if valorado:

        n = len(adj)

        H = []
        n_vizinho = [[]*n for i in range(n)]
        
        for i in range(n):
            for j in range(n):
                if adj[i][j] == 0:
                    pass
                else:
                    a = i
                    b = j
                    c = adj[i][j]
                    n_vizinho[a].append((b, c))
                    
        raiz = random.randint(0, n-1)
        for (x, c) in n_vizinho[raiz]:
            heapq.heappush(H, (c, raiz, x))

        n_arvore = 0
        custo_total = 0
        visitados = [raiz]
        S = [[0]*n for i in range(n)]

        while n_arvore < n-1:
            while True:
                (c, a, b) = heapq.heappop(H)
                if b not in visitados:
                    break
            visitados.append(b)
            custo_total += c
            S[a][b] = S[b][a] = c
            n_arvore += 1
            for (x, c) in n_vizinho[b]:
                heapq.heappush(H, (c, b, x))

        def custo():
            return custo_total
        
        custo()

        return S
    
    else:
        return "Nao é possível usar o algoritmo de Prim em um grafo nao valorado"


    #print("Matriz da Árvore Mínima:")
    #for i in range(n):
     #   print()
      #  for j in range(n):
       #     print(S[i][j], end=" ")

    #print("\n\nO custo total da Árvore Geradora Mínima é de:", custo_total)

