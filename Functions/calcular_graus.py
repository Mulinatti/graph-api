from typing import List
from Vertice import Vertice

def calcular_graus(adjacencias: List[List[int]], digrafo: bool) -> List[int]:
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
        for i in range(len(total_entrada)):
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