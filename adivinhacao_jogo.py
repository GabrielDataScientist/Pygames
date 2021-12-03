import random

def jogar():
    print("------------------------------ ")
    print("Esse é um jogo de advinhação!")
    print("------------------------------ ")

    total_tentativas = 0
    pontos = 1000
    numero_secreto = random.randrange(1, 101)

    print("Escolha o nível de dificuldade", numero_secreto)
    print("(1) - Fácil; (2) - Médio; (3) - Difícil\n")
    nivel = int(input("Digite aqui o nível escolhido: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 51

    print(numero_secreto)
    print("Você tem 1000 pontos!")
    print("Digite um número entre 1 e 100")
    #numero_secreto = int(input("Digite um número secreto: "))

    for rodada in range(1, total_tentativas + 1):
        #print("Rodada {} de {}".format(rodada, total_tentativas))
        print(f"Rodada {rodada} de {total_tentativas}")
        tentativa = int(input("Agora digite um número para tentar advinhar o número secreto: "))
        
        if tentativa < 1 or tentativa > 100:
            print("Você deve digitar um número entre 1 e 100, somente.")
            continue #continua a iteração. Volta no FOR/WHILE e continua a contagem

        acertou = tentativa == numero_secreto
        maior = tentativa > numero_secreto
        menor = tentativa < numero_secreto
        #errou = tentativa != numero_secreto

        if (acertou):
            print("Parabéns, você acertou!")  
            break #sai do laço
        else:
            if(maior):
                print("Hmmm... o número digitado foi maior que o número secreto. Tente novamente.\n")
            elif(menor):
                print("Hmmm.... o número digitado foi menor que o número secreto. Tente novamente.\n")
        pontuacao = abs(numero_secreto - tentativa)#A função ABS retorna o valor absoluto
        pontos = pontos - pontuacao

    print("O número secreto é: ", numero_secreto) 
    print("Sua pontuação final é de: ", pontos)            
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()