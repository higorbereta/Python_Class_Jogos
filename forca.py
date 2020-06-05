def jogo_forca():

    print("**********************************")
    print("*** Bem vindo ao jogo de Forca ***!")
    print("**********************************")

    palavra_secreta = "Canada"
    enforcado = False
    acertou = False

    #enquanto (True)
    while(not enforcado and not acertou):
        chute = input("Digite uma letra: ")

        for letter in palavra_secreta:
            index = 1
            if (letter == chute):
                print("Encontrada a {} na posição {}".format(letter,index))
            else:
                print("Letra não encontrada")
            index = index + 1

        type(chute)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogo_forca()