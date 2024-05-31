import heapq

def kruskal(adj, valorado: bool):
    if valorado:

        n = len(adj)

        H = []

        for i in range(n):
            for j in range(n):
                if adj[i][j] == 0:
                    pass
                else:
                    a = i
                    b = j
                    c = adj[i][j]
                    heapq.heappush(H, (c, a, b))

        C = [[]*n for i in range(n)]
        N = []

        for i in range(n):
            C[i].append(i)

        for i in range(n):
            N.append(i)

        n_arvore = 0
        custo_total = 0
        S = [[0]*n for i in range(n)]

        while n_arvore < n-1:
            c, a, b = heapq.heappop(H)
            if N[a] != N[b]:
                custo_total += c
                u = N[a]
                v = N[b]
                if v < u:
                    u, v = v, u

                for i in C[v]:
                    N[i] = u 

                C[u].extend(C[v])
                C[v] = []
                S[a][b] = S[b][a] = c          
                n_arvore += 1

    #print("Matriz da Árvore Mínima:")
    #for i in range(n):
    #    print()
     #   for j in range(n):
      #      print(S[i][j], end=" ")

    #print("\n\n", C)
    #print("\n\n", N)

    #print("\n\nO custo total da Árvore Geradora Mínima é de:", custo_total)

        return S
    
    else:
        return "Nao é possível usar o algoritmo de Kruskal em um grafo nao valorado"

