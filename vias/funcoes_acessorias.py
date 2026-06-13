class Arquipelago:
    def __init__(self, n_ilhas: int, n_conexoes: int, anos: int):
        self.n_ilhas: int = n_ilhas
        self.n_conexoes: int = n_conexoes
        self.anos: int = anos
        self.rodovias: list = []
        self.grafo: dict = {}
    
    def pega_conexoes(self):
        for _ in range(self.n_conexoes):
            conexao: list = input("Conexão: ").strip().split(" ")
            if conexao[-1] == "1":
                conexao = list(map(int, conexao))
                add_conexao(self.grafo, *conexao)
            else: # conexao = 2 = rodovia
                self.rodovias.append(conexao)
    
    def pega_ponta(self, visitados: list) -> int | None:
        """
        Retorna vertice que está na ponta e ainda não foi visitado. 
        Caso não haja, retorna `None`.
        """
        for vertice in self.grafo:
            if vertice not in visitados:
                return vertice
        return None

    def tem_loop(self, conexao_add=None) -> bool:
        """
        Verifica se há loop no grafo atual do arquipélago.
        """
        # após add rodovia, devo priorizar a busca nos vertices conectados a fim de otimizar 
        visitados: list = []

        while ponta:= self.pega_ponta(visitados):
            visitados.append(ponta)
            a_visitar: list = [vizinho for vizinho in self.grafo[ponta]]

            while a_visitar:
                vertice_atual = a_visitar.pop() # pega ultimo adicionado
                if vertice_atual not in visitados:
                    visitados.append(vertice_atual)
                else:
                    return True
        return False

def add_conexao(grafo: dict, v1: int, v2: int, tipo_de_via: int): #type: ignore
    if grafo.get(v1, []):
        grafo[v1].update({v2: int(tipo_de_via)})
    else:
        grafo[v1] = {v2: int(tipo_de_via)}

    if grafo.get(v2, []):
        grafo[v2].update({v1: int(tipo_de_via)})
    else:
        grafo[v2] = {v1: int(tipo_de_via)}
    return grafo
        

