def jogo_forca():

    print("**********************************")
    print("*** Bem vindo ao jogo de Forca ***!")
    print("**********************************")

    palavra_secreta = input("Palavra secreta: ").upper()
    letras_acertadas = []

    for count in palavra_secreta:
        letras_acertadas.append("_")

    enforcado = False
    acertou = False
    chances = 4

    #enquanto (True)
    while(not enforcado and not acertou):
        chute = input("Você ainda pode errar {} vezes. Digite uma letra: ".format(chances))
        chute = chute.strip().upper()

        index = 0
        qnt_encontrada = 0

        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if (letra == chute):
                    letras_acertadas[index] = chute
                    qnt_encontrada += 1
                index += 1
            print("Letra {} encontrada {} vezes na palavra.".format(chute, qnt_encontrada))
            print("Letras descobertas: \n", letras_acertadas)
        else:
            print("Letra {} não encontrada na palavra secreta!".format(chute))
            chances -= 1

        qnt_encontrada = 0



        enforcado = chances == 0
        acertou = "_" not in letras_acertadas

    if (enforcado):
        print("Excedeu o número de tentativas. Você foi enforcado !")
    elif (acertou):
        print("Você acertou toda a palavra secreta. Parabéns !")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogo_forca()