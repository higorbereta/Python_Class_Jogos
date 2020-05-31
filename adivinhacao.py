print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3

#chute_str = input("Digite seu número: ")
#chute = int(chute_str)

for rodada in range (1, total_tentativas + 1):
    print("Tentativas {} de {}: ".format(rodada, total_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    print("*********************************")
    print("Voce digitou ", chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        print("*********************************")
        continue

    acertou = numero_secreto == chute #Variável booleana
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Voce acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
            print("*********************************")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
            print("*********************************")
print("Fim do jogo")

