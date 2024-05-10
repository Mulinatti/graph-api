# MANUAL PARA UTILIZAÇAO DAS CLASSES QUE COMPÕE O GRAFO

### Classes

- Grafo Abstrato
- Grafo
- Digrafo
- Vertice

## Grafo Abstrato


> [!WARNING]
> A classe `GrafoAbstrato` não deve ser instanciada diretamente.

<br>

<p style="font-weight: 500; font-size: 1.25rem; text-decoration: underline;">Atributos</p>

`mat_adj: [[int]]`: Armazena a matriz de adjacência do grafo.

`mat_incid: [[int]]`: Armazena a matriz de incidência do grafo.

`num_vertices: int`: Quantidade de vértices do grafo.




<br>


<p style="font-weight: 500; font-size: 1.25rem; text-decoration: underline;">Métodos</p>

`contar_arestas(matriz_adj)`: Recebe uma **matriz de adjacências** e retorna o **número de arestas** presente no grafo.

`adj_para_incid(matriz_adj)`: Recebe uma **matriz de adjacências** e aplica um algoritmo que converte essa a **matriz de adjacência** para uma **matriz de incidência**.

> [!NOTE]
> Os métodos acima são concretos nas classes filhas desta, levando em consideraçao a diferença entre **grafos** e **digrafos**

<br>

## Grafo

> [!NOTE]
> A classe `Grafo` herda da classe `GrafoAbstrato`.

<br>

<p style="font-weight: 500; font-size: 1.25rem; text-decoration: underline;">Atributos</p>

`lista_de_graus[int]`: Lista de inteiros que armazena o grau de cada vértice do grafo.


<p style="font-weight: 500; font-size: 1.25rem; text-decoration: underline;">Métodos</p>

`calcular_graus(mat_adj)`: Recebe uma matriz de adjacências e calcula os graus de cada vértice do grafo, e atribui a `lista_de_graus`.

<p style="font-weight: 500; font-size: 1.25rem; text-decoration: underline;">Utilização</p>

```python
#matriz de adjacencias
matrix = [
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
]

#instacia da classe grafo
graph = Grafo(matrix)

print(graph.num_vertices) #Output = 3
```

## Digrafo



> [!NOTE]
> A classe `Digrafo` herda da classe `GrafoAbstrato`.

<br>

<p style="font-weight: 500; font-size: 1.25rem; text-decoration: underline;">Atributos</p>

`lista_de_graus[Vertice]`: Lista de dados da classe `Vertice` que armazena o grau de cada vértice do grafo.

<p style="font-weight: 500; font-size: 1.25rem; text-decoration: underline;">Métodos</p>

`calcular_graus(mat_adj)`: Recebe uma matriz de adjacências e calcula os graus de cada vértice do grafo, e atribui a `lista_de_graus`.

<p style="font-weight: 500; font-size: 1.25rem; text-decoration: underline;">Utilização</p>

```python
#matriz de adjacencias
matrix = [
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
]

#instacia da classe grafo
digraph = Digrafo(matrix)

print(digraph.num_vertices) #Output = 3
```

## Vertice

Classe de dados declarada com `@dataclass`, serve apenas para armazenar os graus dos vértices.

<p style="font-weight: 500; font-size: 1.25rem; text-decoration: underline;">Atributos</p>

`grau_entrada: int`: Indica os graus de entrada.

`grau_saida: int`: Indica os graus de esaída.

`grau_total: int`: Indica o total de graus do vértice.
