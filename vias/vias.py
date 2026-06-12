# 1 -> hidrovia
# grafo não direcional
# não necessariamente há caminho entre a e b
from funcoes_acessorias import constroi_grafo
def main():
    # Input inicial
    ilhas, n_conexoes, anos = map(int, input("Ilhas, n_conexoes, anos: ").split(" "))

    grafo = constroi_grafo(n_conexoes)
    if navega_vertices(grafo, anos):
        print("S")
    else:
        print("N")

def busca_ponta(grafo: dict, vertices_visitados: list) -> str | None:
    """
    Retorna vertice que está na ponta e ainda não foi visitado. 
    Caso não haja, retorna `None`.
    """
    for vertice in grafo:
        if vertice not in vertices_visitados:
            return vertice
            
    return None

def navega_vertices(grafo: dict, anos: int) -> bool:
    """
    Busca um vértice ainda não visitado e então navega pelos vizinhos atrás de loops.
    Caso haja um loop de hidrovia, ou mais loops de rodovia do que K anos, retorna `False`.
    Senão, retorna `True`.
    """
    vertices_visitados: list = []
    contador: int = 0  

    while ponta:=busca_ponta(grafo, vertices_visitados):
        vertices_para_visitar = [ponta]
        while vertices_para_visitar:
            if contador > anos:
                return False
            posicao_atual = vertices_para_visitar.pop(0)
            vertices_visitados.append(posicao_atual)

            for vizinho in grafo[posicao_atual]:
                if vizinho in vertices_visitados:
                    if grafo[posicao_atual][vizinho] == 1:
                        return False
                    contador+=1
                else:
                    vertices_para_visitar.append(vizinho)

    return True

if __name__ == "__main__":
    main()