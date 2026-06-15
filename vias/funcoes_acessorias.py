class Arquipelago:
    def __init__(self, n_ilhas: int, n_conexoes: int, anos: int):
        self.n_ilhas: int = n_ilhas
        self.n_conexoes: int = n_conexoes
        self.anos: int = anos
        self.rodovias: set[tuple] = set() # preciso mudar para set[tuple]
        self.grafo: dict = {}
        self.n_loops: int = 0
    
    def pega_conexoes(self):
        """
        Pede ao usuário as conexões do arquiélago e as armazena no objeto `Arquipelago`. Rodovias são salvas
        em set exclusivo `self.rodovias` para serem verificadas uma a uma posteriormente.
        """
        for _ in range(self.n_conexoes):
            input_de_via: list = input("Conexão: ").strip().split(" ") #type: ignore

            if input_de_via[-1] == "1":
                conexao: tuple = tuple(map(int, input_de_via)) # conexao deveria ser um tuple?
                self.adiciona_conexao(*conexao)

            else: # conexao = 2 = rodovia
                self.rodovias.add(tuple(input_de_via))
    
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
        """
        Pega os dados da conexão fornecida e a introduz ao arquipélago.
        """
        if self.grafo.get(v1, []):
            self.grafo[v1].update({v2: tipo_de_via})
        else:
            self.grafo[v1] = {v2: tipo_de_via}

        if self.grafo.get(v2, []):
            self.grafo[v2].update({v1: tipo_de_via})
        else:
            self.grafo[v2] = {v1: tipo_de_via}
    
    def checa_loop_de_rodovias(self) -> bool:
        for rodovia in self.rodovias:
            self.adiciona_conexao(*rodovia)
            
            if not self.tem_loop():
                continue # rodovia é mantida
            
            self.n_loops += 1 #tem loop
            if self.n_loops > self.anos: #verifica se nao cruzou o limite
                return False #arquipelago não era simples
            self.rodovias.remove(rodovia) # passa a desconsiderar rodovia que foi "destruída"
        return True

    def era_simples(self) -> bool:
        """
        Verifica se arquipélago não tem loops de hidrovia e então checa as rodovias uma a uma
        em busca de loops. Caso haja loop de hidrovia ou mais loops de rodovia do que anos, retorna
        `False`. Caso contrário, retorna `True`
        """
        # cehcando primeiro somente com hidrovias
        if self.tem_loop():
            return False
        else:
            # agora checa uma rodovia por vez
            return self.checa_loop_de_rodovias()