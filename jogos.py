import jogo_da_forca
import adivinhacao_jogo

def escolhe_jogo():
    print("------------------------------ ")
    print("ESCOLHA SEU JOGO!")
    print("------------------------------\n")

    print("(1) - Jogo da Advinhação; (2) - Jogo da Forca")
    jogo = int(input("Digite sua escolha: "))
    
    if (jogo == 1):
        print("Você está jogando Adivinhação\n")
        adivinhacao_jogo.jogar()
    elif (jogo == 2):
        print("Você está jogando Forca")
        jogo_da_forca.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()
