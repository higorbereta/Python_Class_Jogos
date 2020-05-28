print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

#chute_str = input("Digite seu número: ")
#chute = int(chute_str)

chute = int(input("Digite seu número: "))
print("Voce digitou ", chute)

acertou = numero_secreto == chute
maior = chute > numero_secreto

if (acertou):
    print("Voce acertou!")
else:
    if(maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    else:
        print("Você errou! O seu chute foi menor do que o número secreto.")
print("Fim do jogo")