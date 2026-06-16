from sys import exit
import matplotlib.pyplot as plt
from networkx import Graph, draw

class Arquipelago:
    def __init__(self,n_conexoes: int, anos: int):
        self.n_conexoes: int = n_conexoes
        self.anos: int = anos
        self.rodovias: set[tuple] = set()
        self.grafo: dict[set, str] = {}
        self.n_loops: int = 0
    
    def pega_conexoes(self) -> None:
        """
        Pede ao usuário as conexões do arquipélago e as armazena no objeto `Arquipelago`. Rodovias são salvas
        em set exclusivo `self.rodovias` para serem verificadas uma a uma posteriormente.
        """
        for _ in range(self.n_conexoes):
            input_de_via: list = input("vértice 1, vértice 2, tipo de via: ").strip().split(" ") 
            v1, v2, tipo_de_via = input_de_via
            
            if tipo_de_via == "h": # conexao = 1 = hidrovia
                self.adiciona_conexao(v1, v2)

            elif tipo_de_via == "r":
                self.rodovias.add((v1, v2))
            else: # conexao = 2 = rodovia
                exit("Tipo de via incorreto! \"r\" ou \"h\"!")

        self.mostra_grafo("Somente hidrovias")
    
    def pega_ponta(self, visitados: set[str]) -> str | None:
        """
        Retorna vertice que ainda não foi visitado. Caso não haja, retorna `None`.
        """
        for vertice in self.grafo:
            if vertice not in visitados:
                return vertice
        return None

    def tem_loop(self) -> bool:
        """
        Verifica se há loop no grafo atual do arquipélago.
        """
        visitados: set[str] = set()

        while ponta:= self.pega_ponta(visitados):
            a_visitar: list[tuple] = [(None, ponta)] # (v_cauda, v_cabeca)
            
            while a_visitar:

                cauda, cabeca = a_visitar.pop() # pega ultimo vertice adicionado
                visitados.add(cabeca)

                for vizinho in self.grafo[cabeca]:
                    if vizinho == cauda:
                        continue
                    elif vizinho not in visitados:
                        a_visitar.append((cabeca, vizinho)) 
                    else:
                        return True
        return False

    def adiciona_conexao(self, v1: str, v2: str) -> None:
        """
        Pega os dados da conexão fornecida e a introduz ao arquipélago.
        """
        if self.grafo.get(v1, []):
            self.grafo[v1].add(v2)
        else:
            self.grafo[v1]: set = {v2}

        if self.grafo.get(v2, []):
            self.grafo[v2].add(v1)
        else:
            self.grafo[v2]: set = {v1}

    def remove_conexao(self, v1: str, v2: str) -> None:
        self.grafo[v1].remove(v2)
        self.grafo[v2].remove(v1)

    def checa_loop_de_rodovias(self) -> bool:
        """
        Adiciona cada rodovia ao grafo, mas a cada rodovia adicionada, o grafo é verificado novamente
        """
        for rodovia in self.rodovias:
            self.adiciona_conexao(*rodovia)
            self.mostra_grafo(f"Adicionada a rodovia entre {rodovia[0]} e {rodovia[1]}")

            if not self.tem_loop():
                continue # rodovia é mantida
            
            self.n_loops += 1 #tem loop
            if self.n_loops > self.anos: #verifica se nao cruzou o limite
                self.mostra_grafo(f"Loops de rodovia demais! Arquipélago não era simples", cor='red')
                return False #arquipelago não era simples
            self.remove_conexao(*rodovia)
            self.mostra_grafo(f"Removida a rodovia entre {rodovia[0]} e {rodovia[1]}")
        return True

    def era_simples(self) -> bool:
        """
        Verifica se arquipélago não tem loops de hidrovia e então checa as rodovias uma a uma
        em busca de loops. Caso haja loop de hidrovia ou mais loops de rodovia do que anos, retorna
        `False`. Caso contrário, retorna `True`
        """
        # cehcando primeiro somente com hidrovias
        if self.tem_loop():
            self.mostra_grafo(f"Há um loop de hidrovia! Arquipélago não era simples", cor='red')            
            return False
        else:
            # agora checa uma rodovia por vez
            return self.checa_loop_de_rodovias()
    
    def mostra_grafo(self, mensagem: str = "", cor: str = "blue") -> None:
        """
        Gera .png representando o grafo do arquipélago com todas as hidrovias e as 
        rodovias adicionadas até então.
        """
        g = Graph(self.grafo)
        draw(g, with_labels=True, node_color='skyblue')
        plt.figtext(0.5, 0.01, mensagem, wrap=True, horizontalalignment='center', fontsize=12, color=cor)
        plt.title(f"Anos: {self.anos}           Loops de rodovia: {self.n_loops}")
        plt.savefig("meu_grafo.png", format="PNG", dpi=300, bbox_inches="tight")
        plt.close()
        input("ENTER para continuar")