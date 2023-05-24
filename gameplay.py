import random
import palavras_forca
from funcoes_forca import randompalavra

resposta_final=()
novo_jogo = 1

while novo_jogo == 1:
    letras_usuario = []
    chances = 5
    print("==========JOGO DA FORCA========== \n" #Menu e randomização da palavra
          "Temas para jogar\n"
          "[1] - Animais \n[2] - Carros \n[3] - Comidas\n[4] - Cidades")
    resp = int(input("Com qual tema você deseja jogar?"))
    palavra = randompalavra(resp)
    print(f"Muito bem, a palavra tem {len(palavra)} letras")
    while True:
        acertos = 0
        tentativa=input("Digite uma letra: ") #Gameplay e controle das chances
        letras_usuario.append(tentativa)
        for letra in palavra:
            if letra.lower() in letras_usuario:
                print(letra,end=" ")
                acertos+=1
            else:
                print("_", end= " ")
        #print(chances)
        print()
        if tentativa not in palavra:
            chances -= 1
        if acertos == len(palavra): #VERIFICAÇÃO DE GANHO ANTES DE ACABAR AS CHANCES
            print("PARABÉNS VOCÊ GANHOU!!!!")
            break
        if chances == 0: #Verificação se ganhou ou perdeu depois de todas as chances
            resposta_final=input("Todas as chances acabaram, mas vou te dar um bônus\n Qual a palavra?")
            if resposta_final == palavra.lower():
                print("PARABÉNS VOCÊ GANHOU!!!!")
            else:
                print(f"VOCÊ ERROU TAVA QUASE LÁ!!\n A palavra era {palavra}")
            break
    novo_jogo = int(input("Quer jogar novamente?\n"
                                "[1] - Sim?\n [2] Não? "))
    if novo_jogo == 2:
        print("jogo encerrado")













 







