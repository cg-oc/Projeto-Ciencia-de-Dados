from arquipelago import Arquipelago
from sys import exit

def main():
    while True:
        try:
            n_conexoes, anos = map(int, input("Número de conexões, anos: ").split(" "))
            break
        except ValueError:
            print("Input inválido!")
        except KeyboardInterrupt:
            exit("\nPrograma finalizado!")
    arquipelago = Arquipelago(n_conexoes, anos) # instancializa o objeto arquipelago

    if arquipelago.era_simples():
        print("O arquipélago era simples!")
    else:
        print("O arquipélago não era simples!")

    
if __name__ == "__main__":
    main()