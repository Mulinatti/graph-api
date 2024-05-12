from dataclasses import dataclass

@dataclass
class Vertice:
    """Classe de dados necessária para armazenar
       os graus de entrada e de saída de um vértice."""
    grau_entrada: int
    grau_saida: int
    grau_total: int
