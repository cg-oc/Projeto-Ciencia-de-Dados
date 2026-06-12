class Arquipelago:
    def __init__(self, n_ilhas: int, n_conexoes: int, anos: int):
        self.n_ilhas: int = n_ilhas
        self.n_conexoes: int = n_conexoes
        self.anos: int = anos
        self.visitados: list = []
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
    
    def pega_ponta(self) -> int | None:
        """
        Retorna vertice que está na ponta e ainda não foi visitado. 
        Caso não haja, retorna `None`.
        """
        for vertice in self.grafo:
            if vertice not in self.visitados:
                return vertice
        return None

def add_conexao(grafo: dict, v1: int, v2: int, tipo_de_via: int):
    if grafo.get(v1, []):
        grafo[v1].update({v2: int(tipo_de_via)})
    else:
        grafo[v1] = {v2: int(tipo_de_via)}

    if grafo.get(v2, []):
        grafo[v2].update({v1: int(tipo_de_via)})
    else:
        grafo[v2] = {v1: int(tipo_de_via)}
    return grafo
        

