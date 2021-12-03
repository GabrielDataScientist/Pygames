import random 

def jogar():
   
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    acertou = False
    enforcou = False
    erros = 0

    while (not acertou and not enforcou):
        chute = tenta_chute()

        if (chute in palavra_secreta):
           marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
       imprime_mensagem_vencedor()
    else:
       imprime_mensagem_perdedor()
    
    print("Fim de Jogo!")

def imprime_mensagem_abertura():
    print("------------------------------ ")
    print("Jogo da Forca!")
    print("------------------------------ ")
    print("\n")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras_advinhar = [linha.strip() for linha in arquivo]#compreensão de lista. Recebe as palavras do arquivo txt.
    arquivo.close()

    escolhe_palavra = random.randrange(0, len(palavras_advinhar))#Escolhe aleatoriamente uma palavra com base na sua posição dentro da lista
    palavra_secreta = palavras_advinhar[escolhe_palavra].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra] 

def tenta_chute():
    chute = input("Tente adivinhar uma letra: ")
    chute = chute.strip().upper() #O strip() remove espaços em branco
    return chute

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0 #Índice para incrementar a iterção em cima da palavra, já que a palavra não é lista.
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()): #upper() torna as letras maiúsculas
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Você ganhou!")

def imprime_mensagem_perdedor():
    print("Você perdeu!")

if (__name__ == "__main__"):
    jogar()