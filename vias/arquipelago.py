from sys import exit
import matplotlib.pyplot as plt
from networkx import Graph, draw

class Arquipelago:
    """
    Representa um arquipélago como grafos para verificar as conexões entre suas ilhas.

    Permite verificar laços e adicionar conexões entre suas ilhas, mantendo salvo os dados do grafo
    correspondente a cada alteração.

    Attributes:
        self.n_conexoes (int): Quantas conexões há entre linhas.
        self.anos (int): Período de estudo do arquipélago.
        self.rodovias (set[tuple]): Guarda os pares de ilhas conectadas por cada rodovia.
        self.grafo (dict[str, set]): Dicionário que representa o grafo.
        self.n_loops (int): Qunatos laços de rodovia já foram detectados.
    """
    def __init__(self, n_conexoes: int, anos: int):
        self.n_conexoes: int = n_conexoes
        self.anos: int = anos
        self.rodovias: set[tuple] = set()
        self.grafo: dict[str, set] = {}
        self.n_loops: int = 0

    def era_simples(self) -> bool:
        """
        Verifica se arquipélago não tem loops de hidrovia e então checa as rodovias uma a uma
        em busca de loops. Caso haja loop de hidrovia ou mais loops de rodovia do que anos, retorna
        `False`. Caso contrário, retorna `True`
        """
        self.pega_conexoes() # carrega dados do arquipelago

        if self.tem_loop(): # checando primeiro somente com hidrovias
            self.mostra_grafo(f"Há um loop de hidrovia! Arquipélago não era simples", cor='red')            
            return False
        else:
            # agora checa uma rodovia por vez
            return not self.tem_loop_de_rodovias()
    
    def pega_conexoes(self) -> None:
        """
        Pede ao usuário as conexões do arquipélago e as armazena no objeto `Arquipelago`. Rodovias são salvas
        em set exclusivo `self.rodovias` para serem verificadas uma a uma posteriormente.
        """
        while True:
            try:
                for _ in range(self.n_conexoes):
                    input_de_via: list = input("vértice 1, vértice 2, tipo de via: ").strip().split(" ") 
                    v1, v2, tipo_de_via = input_de_via
                    
                    if tipo_de_via == "h": # conexao = 1 = hidrovia
                        self.adiciona_conexao(v1, v2)

                    elif tipo_de_via == "r":
                        self.rodovias.add((v1, v2))
                    else: 
                        raise ValueError
                break

            except ValueError:
                print("Input inválido!")
            except KeyboardInterrupt:
                exit("\nPrograma finalizado!")

        self.mostra_grafo("Somente hidrovias") # Gera PNG

    def tem_loop_de_rodovias(self) -> bool:
        """
        Adiciona uma rodovia por vez e busca por algum laço no grafo a cada adição. Se encontrar laço, 
        aumenta a contagem de laços em 1.\n
        Saída: Se a contagem for maior que Q anos, retorna `False`, senão, `True`.
        """
        for rodovia in self.rodovias:
            self.adiciona_conexao(*rodovia)
            self.mostra_grafo(f"Adicionada a rodovia entre {rodovia[0]} e {rodovia[1]}")

            if not self.tem_loop():
                continue # rodovia é mantida
            
            self.n_loops += 1 #tem loop
            if self.n_loops > self.anos: #verifica se nao cruzou o limite
                self.mostra_grafo(f"Loops de rodovia demais! Arquipélago não era simples", cor='red')
                return True #arquipelago não era simples
            self.remove_conexao(*rodovia)
            self.mostra_grafo(f"Removida a rodovia entre {rodovia[0]} e {rodovia[1]}")
            
        return False

    def tem_loop(self) -> bool:
        """
        Verifica se há loop no grafo atual do arquipélago.\n
        Saída: `True` se houver loop ou `False` caso contrário
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
        
    def pega_ponta(self, visitados: set[str]) -> str | None:
        """
        Busca vértice do grafo que ainda não foi visitado.\n
        Entrada:
            Conjunto de strings representando quais vértices já foram visitados
        Saída:
            Vértice que ainda não foi visitado. Caso não haja, retorna `None`.
        """
        for vertice in self.grafo:
            if vertice not in visitados:
                return vertice
        return None

    def adiciona_conexao(self, v1: str, v2: str) -> None:
        """
        Pega dois vértices e adiciona cada um ao conjunto correspondente do outro no grafo.
        Entrada: Dois vértices do grafo, que são strings.
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
        """
        Pega dois vértices e exclui cada um do do conjunto correspondente do outro no grafo
        Entrada:
            Dois vértices do grafo, que são strings.
        """
        self.grafo[v1].remove(v2)
        self.grafo[v2].remove(v1)
    
def mostra_grafo(self, mensagem: str = "", cor: str = "blue") -> None:
    """
    Gera .png representando o grafo do arquipélago com todas as hidrovias e as 
    rodovias adicionadas até então.
    Entrada: Uma mensagem em string que será mostrada no fundo do .png e o nome de uma cor em string.
    """
    g = Graph(self.grafo)
    draw(g, with_labels=True, node_color='skyblue')
    plt.figtext(0.5, 0.01, mensagem, wrap=True, horizontalalignment='center', fontsize=12, color=cor)
    plt.title(f"Anos: {self.anos}              Loops de rodovia encontrados: {self.n_loops}")
    plt.savefig("meu_grafo.png", format="PNG", dpi=300, bbox_inches="tight")
    plt.close()
    input("ENTER para continuar")