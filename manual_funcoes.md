# MANUAL PARA UTILIZAÇAO DAS FUNÇÕES QUE COMPÕE O GRAFO

### Funções

- adj_para_incid
- calcular_graus
- contar_arestas

## Adjacência para Incidência

Função que transforma a matriz de adjacência informada e retorna a sua matriz de incidência.

`adj_para_incid(matriz_adj: List[List[int]], digrafo: bool, valorado: bool) -> List[List[int]]`

**UTILIZAÇÃO**

```python
Functions.adj_para_incid import adj_para_incid

#matriz de um grafo simples
matriz = [
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
]

adj_para_incid(matriz, False, False)
```
```python
#Output
[1, 1, 0] 
[1, 0, 1]
[0, 1, 1]
```

## Calcular Graus

`calcular_graus(matriz_adj: List[List[int]], digrafo: bool, valorado: bool) -> Vertice[]`

**UTILIZAÇÃO**

```python
from Functions.calcular_graus import calcular_graus

#matriz de um digrafo
matriz = [
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
]

calcular_graus(matriz, True, False)
```
```python
#Output
[
  Vertice(grau_entrada=2, grau_saida=2, grau_total=0), 
  Vertice(grau_entrada=2, grau_saida=2, grau_total=0), 
  Vertice(grau_entrada=2, grau_saida=2, grau_total=0)
]
```
<br>

> [!NOTE]
> A funçao retornará um objeto do tipo `Vertice`, que é apenas uma classe para guardar as informações do grau de entrada e saída caso seja um digrafo.

<br>

## Contar Arestas

`contar_arestas(matriz_adj: List[List[int]], digrafo: bool, valorado: bool) -> int`

**UTILIZAÇÃO**

```python
from Functions.contar_arestas import contar_arestas

#matriz de um grafo
matriz = [
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0]
]

contar_arestas(matriz, False, False)

#Output: 3
```
