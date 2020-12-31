import random

def jogo_forca():

    mensagem_inicio()
    palavra_secreta = arquivo_palavras()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    letras_incorretas = []
    enforcado = False
    acertou = False
    erros = 0

    #enquanto (True)
    while(not enforcado and not acertou):
        chute = pede_chute()
        if chute in palavra_secreta:
            letra_correta(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
            print("Letras erradas até o momento: \n", chute)

        enforcado = erros == 7
        acertou = "_" not in letras_acertadas
        if (enforcado):
            msg_loser(palavra_secreta)
        elif (acertou):
            msg_winner()

    print("Fim do jogo")

def mensagem_inicio():
    print("**********************************")
    print("*** Bem vindo ao jogo de Forca ***!")
    print("**********************************")

def arquivo_palavras(nome_arquivo="palavras.txt", primeira_linha=0): #parametro opcional (valor padrão)
    '''
    # Substitui o bloco abaixo, fazendo com que o arquivo seja sempre fechado.
    with open("palavra.txt", "r") as chamar_arquivo:
        palavras = []
        for linha in chamar_arquivo:
            palavras.append(linha.strip().upper())
        qnt = random.randrange(0,len(palavras))
'''
    chamar_arquivo = open(nome_arquivo, "r")
    palavras = []

    for linha in chamar_arquivo:
        palavras.append(linha.strip().upper())

    chamar_arquivo.close()

    # Comendo with substitui a necessidade do close(), porque caso ocorra algum problema com a execução do script antes do close, o SO ficará com o arquivo aberto.

    qnt = random.randrange(primeira_linha, len(palavras))
    palavra_secreta = palavras[qnt]

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for count in palavra]

def pede_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def letra_correta(palavra_secreta, chute, letra_informada):
    index = 0
    qnt_encontrada = 0
    for letra in palavra_secreta:
        if (letra == chute):
            letra_informada[index] = chute
            qnt_encontrada += 1
        index += 1
    print("Letra {} encontrada {} vezes na palavra.".format(chute, qnt_encontrada))
    print("Letras descobertas: \n", letra_informada)


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def msg_loser(palavra_secreta):
    print("Excedeu o número de tentativas. Você foi enforcado !")
    print("A palavra era {}".format(palavra_secreta))
    print("     _______________         ")
    print("    /               \       ")
    print("   /                 \      ")
    print("/\/                   \/\  ")
    print("\ |    XXX     XXX    | /   ")
    print(" \|   XXXXX   XXXXX   |/     ")
    print("  |    XXX     XXX    |      ")
    print("  |                   |      ")
    print("  \__      XXX      __/     ")
    print("    |\     XXX     /|       ")
    print("    | |           | |        ")
    print("    | I I I I I I I |        ")
    print("    |  I I I I I I  |        ")
    print("    \_             _/       ")
    print("      \_         _/         ")
    print("        \_______/           ")

def msg_winner():
    print("Você acertou toda a palavra secreta. Parabéns !")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

if(__name__ == "__main__"):
    jogo_forca()