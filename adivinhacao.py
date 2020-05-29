print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

#chute_str = input("Digite seu número: ")
#chute = int(chute_str)

while(rodada <= total_tentativas):
    print("Tentativas {} de {}: ".format(rodada, total_tentativas))
    chute = int(input("Digite seu número: "))
    print("*********************************")
    print("Voce digitou ", chute)

    acertou = numero_secreto == chute #Variável booleana
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Voce acertou!")
        rodada = 4
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
            print("*********************************")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
            print("*********************************")
    rodada = rodada +1
print("Fim do jogo")

