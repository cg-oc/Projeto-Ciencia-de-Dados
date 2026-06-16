from arquipelago import Arquipelago

def main():
    n_conexoes, anos = map(int, input("Número de conexões, anos: ").split(" "))

    arquipelago = Arquipelago(n_conexoes, anos) # instancializa o objeto arquipelago

    arquipelago.pega_conexoes() # carrega dados do arquipelago
    if arquipelago.era_simples():
        arquipelago.mostra_grafo("Arquipélago era simples!")
        print("O arquipélago era simples!")
    else:
        print("O arquipélago não era simples!")
    
if __name__ == "__main__":
    main()