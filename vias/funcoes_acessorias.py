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
                self.adiciona_conexao(*conexao)
            else: # conexao = 2 = rodovia
                self.rodovias.append(conexao)
    
    def pega_ponta(self, visitados: set) -> int | None:
        """
        Retorna vertice que está na ponta e ainda não foi visitado. 
        Caso não haja, retorna `None`.
        """
        for vertice in self.grafo:
            if vertice not in visitados:
                return vertice
        return None

    def tem_loop(self) -> bool:
        """
        Verifica se há loop no grafo atual do arquipélago.
        """
        # após add rodovia, devo priorizar a busca nos vertices conectados a fim de otimizar 
        visitados = set()

        while ponta:= self.pega_ponta(visitados):
            # vertice cauda, vertice cabeca
            a_visitar: list[tuple] = [(None, ponta)]
            
            while a_visitar:

                cauda, cabeca = a_visitar.pop() # pega ultimo adicionado
                visitados.add(cabeca)

                for vizinho in self.grafo[cabeca]:
                    if vizinho == cauda:
                        continue
                    elif vizinho not in visitados:
                        a_visitar.append((cabeca, vizinho)) #type: ignore
                    else:
                        return True
        return False
    def adiciona_conexao(self, v1: int, v2: int, tipo_de_via: int) -> None:
        if self.grafo.get(v1, []):
            self.grafo[v1].update({v2: tipo_de_via})
        else:
            self.grafo[v1] = {v2: tipo_de_via}

        if self.grafo.get(v2, []):
            self.grafo[v2].update({v1: tipo_de_via})
        else:
            self.grafo[v2] = {v1: tipo_de_via}

# def add_conexao(grafo: dict, v1: int, v2: int, tipo_de_via: int): #type: ignore
#     if grafo.get(v1, []):
#         grafo[v1].update({v2: int(tipo_de_via)})
#     else:
#         grafo[v1] = {v2: int(tipo_de_via)}

#     if grafo.get(v2, []):
#         grafo[v2].update({v1: int(tipo_de_via)})
#     else:
#         grafo[v2] = {v1: int(tipo_de_via)}
#     return grafo
        

