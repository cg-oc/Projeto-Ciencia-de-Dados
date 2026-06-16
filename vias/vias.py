from funcoes_acessorias import Arquipelago
from networkx import Graph, draw


def main():
    # Input inicial
    n_conexoes, anos = map(int, input("Número de conexões, anos: ").split(" "))

    arquipelago = Arquipelago(n_conexoes, anos)
    # carrega dados do arquipelago
    arquipelago.pega_conexoes()
    if arquipelago.era_simples():
        print("S")
    else:
        print("N")
    
if __name__ == "__main__":
    main()