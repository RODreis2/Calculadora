
import os
import random

JogarNovamente = "s"
Jogadas = 0
QuemJoga = 2
MaxJogadas = 9
vit = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
while True:
    def tela():
        global velha
        global jogadas
        os.system("cls")
    print("    0   1   2")
    print("0:  ",velha[0][0],"|",velha[0][1],"|",velha[0][2])
    print("   -------------")
    print("1:  ",velha[1][0],"|",velha[1][1],"|",velha[1][2])
    print("   -------------")
    print("2:  ",velha[2][0],"|",velha[2][1],"|",velha[2][2])
    print("Jogadas: "+ str(Jogadas))
    tela()
    linha = int(input("digite a linha: "))
    coluna = int(input("digite o a coluna: "))


    def verifica_vitoria(velha):
        for row in velha:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]

        for col in range(3):
            if velha[0][col] == velha[1][col] == velha[2][col] and velha[0][col] != " ":
                return velha[0][col]

        if velha[0][0] == velha[1][1] == velha[2][2] and velha[0][0] != " ":
            return velha[0][0]

        if velha[0][2] == velha[1][1] == velha[2][0] and velha[0][2] != " ":
            return velha[0][2]

        return None

    while linha < 0 or linha > 2:
        linha = int(input("Digite um numero valido para a linha: "))

    while coluna < 0 or coluna > 2:
        coluna = int(input("Digite um numero valido para a coluna: "))

    while velha[linha][coluna] != " ":
        print("você selecionou uma posição que já está ocupada")
        linha = int(input("Digite uma numero valido para a linha: "))
        coluna = int(input("Digite um numero valido para a coluna: "))

    velha[linha][coluna] = "x"
    tela()

    winner = verifica_vitoria(velha)
    if winner:
        print("o X venceu!")
        tela()
        break

    linhabot = random.randint(0,2)
    colunabot = random.randint(0,2)

    while velha[linhabot][colunabot] != " ":
        linhabot = random.randint(0,2)
        colunabot = random.randint(0,2)
    velha[linhabot][colunabot] = "o"

    winner = verifica_vitoria(velha)
    if winner:
        tela()
        print("o O venceu!")
        break




