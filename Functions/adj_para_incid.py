import unittest

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
                    if adj[j][i] > 0 and i != j:
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


class TestAdjParaIncid(unittest.TestCase):
     def test_1(self):
          """Testar um grafo bem básico mesmo."""
          self.assertEqual(adj_para_incid([
               [0, 1, 0, 0],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [0, 0, 1, 0]
          ], False, False, 3), [
              [1, 0, 0],
              [1, 1, 0],
              [0, 1, 1],
              [0, 0, 1]
          ])
     
     def test_2(self):
          """Testar um grafo não valorado com laço."""
          self.assertEqual(adj_para_incid([
               [1, 1, 0],
               [1, 0, 1],
               [0, 1, 1]
          ], False, False, 4), [
              [1, 1, 0, 0],
              [0, 1, 1, 0],
              [0, 0, 1, 1]
          ])
     
     def test_3(self):
          """Testar um grafo com arestas múltiplas."""
          self.assertEqual(adj_para_incid([
               [0, 2, 2],
               [2, 0, 2],
               [2, 2, 0]
          ], False, False, 6), [
              [1, 1, 1, 1, 0, 0],
              [1, 1, 0, 0, 1, 1],
              [0, 0, 1, 1, 1, 1]
          ])
     
     def test_4(self):
          """Testar um grafo valorado."""
          self.assertEqual(adj_para_incid([
               [0, 20, 5],
               [20, 0, 15],
               [5, 15, 0]
          ], False, True, 3), [
              [20, 5, 0],
              [20, 0, 15],
              [0, 5, 15]
          ])
     
     def test_5(self):
          """Testar um grafo valorado e com laço."""
          self.assertEqual(adj_para_incid([
               [15, 3, 2],
               [3, 0, 0],
               [2, 0, 0]
          ], False, True, 3), [
              [15, 3, 2],
              [0, 3, 0],
              [0, 0, 2]
          ])
     
     def test_6(self):
          """Testar um digrafo bem simples mesmo."""
          self.assertEqual(adj_para_incid([
               [0, 1, 1],
               [0, 0, 0],
               [0, 0, 0]
          ], True, False, 2), [
              [1, 1],
              [-1, 0],
              [0, -1]
          ])
     
     def test_7(self):
          """Testar um digrafo com laço."""
          self.assertEqual(adj_para_incid([
               [1, 1, 0, 0],
               [0, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0]
          ], True, False, 4), [
              [0, 1, 0, 0],
              [0, -1, -1, 0],
              [0, 0, 1, -1],
              [0, 0, 0, 1]
          ])
     
     def test_8(self):
          """Testar um digrafo com aresta dupla."""
          self.assertEqual(adj_para_incid([
               [0, 1, 0],
               [1, 0, 0],
               [0, 0, 0]
          ], True, False, 2), [
              [1, -1],
              [-1, 1],
              [0, 0]
          ])
     
     def test_9(self):
          """Testar um digrafo com múltiplas arestas."""
          self.assertEqual(adj_para_incid([
               [0, 1, 0, 0],
               [1, 0, 1, 0],
               [0, 1, 0, 2],
               [0, 0, 2, 0]
          ], True, False, 8), [
              [1, -1, 0, 0, 0, 0, 0, 0],
              [-1, 1, 1, -1, 0, 0, 0, 0],
              [0, 0, -1, 1, 1, 1, -1, -1],
              [0, 0, 0, 0, -1, -1, 1, 1]
          ])
     
     def test_10(self):
          """Testar um digrafo com laço e arestas duplas."""
          self.assertEqual(adj_para_incid([
               [0, 0, 0],
               [0, 1, 1],
               [2, 1, 0]
          ], True, False, 5), [
              [0, 0, -1, -1, 0],
              [0, 1, 0, 0, -1],
              [0, -1, 1, 1, 1]
          ])
    
     def test_11(self):
         """Testar um digrafo valorado."""
         self.assertEqual(adj_para_incid([
             [0, 5, 0],
             [0, 0, 10],
             [0, 0, 0]
         ], True, True, 2), [
             [5, 0],
             [-5, 10],
             [0, -10]
         ])

if __name__ == '__main__':
     unittest.main(verbosity=2)

