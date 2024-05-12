def adj_para_incid(adj: list[list[int]], digrafo: bool, valorado: bool, num_arestas: int):
    # Populando a nova matriz com zeros
    incid = []
    for _ in range(len(adj)):
        incid.append([0] * num_arestas)
    indice_aresta = 0
    
    if digrafo:
        if valorado:
            for i in range(len(adj)):
                if adj[i][i] > 0:
                    incid[i][indice_aresta] = 0
                    indice_aresta += 1
                
                for j in range(len(adj)):
                    if adj[i][j] > 0 and i != j:
                        incid[i][indice_aresta] = adj[i][j]
                        incid[j][indice_aresta] = -adj[i][j]
                        indice_aresta += 1
        else:
            for i in range(len(adj)):
                if adj[i][i] > 0:
                    incid[i][indice_aresta] = 0
                    indice_aresta += 1
                
                for j in range(len(adj)):
                    if adj[i][j] > 0 and i != j:
                        for _ in range(adj[i][j]):
                            incid[i][indice_aresta] = 1
                            incid[j][indice_aresta] = -1
                            indice_aresta += 1
    else:
        if valorado:
            for i in range(len(adj)):
                # Lidando com laços
                if adj[i][i] != 0:
                    incid[i][indice_aresta] += adj[i][i]
                    indice_aresta += 1
                
                for j in range(i+i, len(adj)):
                    if adj[j][i] > 0:
                        incid[i][indice_aresta] += adj[j][i]
                        incid[j][indice_aresta] += adj[j][i]
                        indice_aresta += 1
        else:
            for i in range(len(adj)):
                # Lidando com laços
                if adj[i][i] != 0:
                    incid[i][indice_aresta] += adj[i][i]
                    indice_aresta += 1
                
                for j in range(i+1, len(adj)):
                    if adj[j][i] > 0:
                        for _ in range(adj[j][i]):
                            incid[i][indice_aresta] += 1
                            incid[j][indice_aresta] += 1
                            indice_aresta += 1
    return incid


def print_matriz(mat):
    for i in range(len(mat)):
        print(mat[i])


adj = [
    [0, 50, 30],
    [0, 0, 0],
    [0, 0, 0]]
incid = adj_para_incid(adj, True, True, 2)
print_matriz(incid)