from Vertice import Vertice

def calcular_graus(adjacencias: list[list[int]], digrafo: bool) -> list[int]:
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
            for j in range(len(adjacencias)):
                # Adicionando os valores negativos na variável entrada e os potivos na variável saida
                if adjacencias[i][j] < 0:
                    entrada += adjacencias[i][j]
                else:
                    saida += adjacencias[i][j]
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
        for j in range(len(adjacencias)):
            # Para pegar os valores
            aux += adjacencias[i][j]
            # Adicionando o valor a lista
        soma_graus.append(aux)
        # Zerando o valor auxiliar antes da próxima iteração
        aux = 0
    return soma_graus