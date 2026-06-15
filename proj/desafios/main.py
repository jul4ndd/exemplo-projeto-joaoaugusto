from src.Estacionamento import Estacionamento
from src.Vaga import Vaga
from src.Veiculo import Veiculo

if __name__ == "__main__":
    
    control = 0
    while(True):

        if control == 0:
            print(" ------------ BEM VINDO ------------ ")
        else:
            print(" ----------------------------------- ")
            print(" 1 - Estacionar veículo: ")
            print(" 2 - Verificar tempo estacionado: ")
            print(" 3 - Checkout: ")
            print(" 4 - Mostrar veículos estacionados: ")
            print(" 5 - Sair! ")
        
        choice:int = int(input("\n Escolha uma opção: "))

        control = 1

        if choice == 5:
            break

        if choice == 1:
            numero_vaga = int(input("Digite o número da vaga (1-10): "))

        if choice == 2:
            # Chama a função aqui
            pass
