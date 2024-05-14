from Vertice import Vertice
import unittest

# Uma matriz é uma lista de listas de inteiros
type Matriz = list[list[int]]

def calcular_graus(adjacencias: Matriz, digrafo: bool) -> list[int]:
    soma_graus = []

    if digrafo:
        # Para armazenar os graus de entrada totais
        total_entrada = []
        # Para armazenar os graus de saída totais
        total_saida = []
        # Para armazenar temporariamente os valores de entrada e saída
        # antes deles serem anexados aos totais
        entrada, saida = 0, 0
        for i in range(len(adjacencias)):
            # Para impedir a lista de ir out of bounds
            if i >= len(adjacencias[i]):
                break
            for j in range(len(adjacencias)):
                # Adicionando os valores negativos na variável entrada e os potivos na variável saida
                if adjacencias[j][i] < 0:
                    entrada += adjacencias[j][i]
                else:
                    saida += adjacencias[j][i]
            total_entrada.append(entrada)
            total_saida.append(saida)
            # Reiniciando os valores auxiliares antes da próxima iteração
            entrada, saida = 0, 0
        for i in range(len(total_saida)):
            # Calculando o Grau total da vértice
            total = total_entrada[i] + total_saida[i]
            # Iterando o objeto Vertice usando os valores adquiridos previamente
            nome = Vertice(total_entrada[i], total_saida[i], total)
            # Adicionando o objeto a lista
            soma_graus.append(nome)
        return soma_graus

    soma_graus = []
    # Para armazenar temporariamente o valor do grau durante as iterações
    aux = 0
    for i in range(len(adjacencias)):
        # Para impedir que a lista dê out of bounds.
        if i >= len(adjacencias[i]):
            break
        for j in range(len(adjacencias)):
            # Para pegar os valores verticalmente, ao invês de horizontalmente
            aux += adjacencias[j][i]
        # Adicionando o valor a lista
        soma_graus.append(aux)
        # Zerando o valor auxiliar antes da próxima iteração
        aux = 0
    return soma_graus


class TestAdjParaIncid(unittest.TestCase):
     def test_1(self):
          """Testar um grafo bem básico mesmo."""
          self.assertEqual(calcular_graus([
               [0, 1, 0, 0],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [0, 0, 1, 0]
          ], False), [1, 2, 2, 1])
     
     def test_2(self):
          """Testar um grafo não valorado com laço."""
          self.assertEqual(calcular_graus([
               [1, 1, 0],
               [1, 0, 1],
               [0, 1, 1]
          ], False), [2, 2, 2])
     
     def test_3(self):
          """Testar um grafo com arestas múltiplas."""
          self.assertEqual(calcular_graus([
               [0, 2, 2],
               [2, 0, 2],
               [2, 2, 0]
          ], False), [4, 4, 4])
     
     def test_4(self):
          """Testar um grafo valorado."""
          self.assertEqual(calcular_graus([
               [0, 20, 5],
               [20, 0, 15],
               [5, 15, 0]
          ], False), [25, 35, 20])
     
     def test_5(self):
          """Testar um grafo valorado e com laço."""
          self.assertEqual(calcular_graus([
               [15, 3, 2],
               [3, 0, 0],
               [2, 0, 0]
          ], False), [20, 3, 2])
     
     def test_6(self):
          """Testar um digrafo bem simples mesmo."""
          self.assertEqual(calcular_graus([
               [0, 1, 1],
               [0, 0, 0],
               [0, 0, 0]
          ], True), [Vertice(0, 2, 2), Vertice(1, 0, 1), Vertice(1, 0, 1)])
     
     def test_7(self):
          """Testar um digrafo com laço."""
          self.assertEqual(calcular_graus([
               [1, 1, 0, 0],
               [0, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0]
          ], True), [Vertice(0, 1, 1), Vertice(2, 0, 2), Vertice(1, 0, 1), Vertice(0, 1, 1)])
     
     def test_8(self):
          """Testar um digrafo com aresta dupla."""
          self.assertEqual(calcular_graus([
               [0, 1, 0],
               [1, 0, 0],
               [0, 0, 0]
          ], True), [Vertice(1, 1, 0), Vertice(1, 1, 0), Vertice(0, 0, 0)])
     
     def test_9(self):
          """Testar um digrafo com múltiplas arestas."""
          self.assertEqual(calcular_graus([
               [0, 1, 0, 0],
               [1, 0, 1, 0],
               [0, 1, 0, 2],
               [0, 0, 2, 0]
          ], True), [Vertice(1, 1, 0), Vertice(2, 2, 0), Vertice(3, 3, 0), Vertice(2, 2, 0)])
     
     def test_10(self):
          """Testar um digrafo com laço e arestas duplas."""
          self.assertEqual(calcular_graus([
               [0, 0, 0],
               [0, 1, 1],
               [2, 1, 0]
          ], True), [Vertice(2, 0, 2), Vertice(1, 1, 0), Vertice(1, 3, 2)])
    
     def test_11(self):
         """Testar um digrafo valorado."""
         self.assertEqual(calcular_graus([
             [0, 5, 0],
             [0, 0, 10],
             [0, 0, 0]
         ], True), [Vertice(0, 5, 5), Vertice(5, 10, 5), Vertice(10, 0, 10)])


if __name__ == '__main__':
     unittest.main()
