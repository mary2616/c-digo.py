import os
import random

os.system("cls")

#apresentação do jogo
print("\nBem vindo ao jogo de adivinhação!")

def escolher_dificuldade():

        dificuldade = input("Escolha a dificudae (fácil, médio, difícil): ").lower()
        if dificuldade == 'fácil':
                return random.ranint(1, 50) # return: retorna o número, dá um número
        elif dificuldade == 'médio':
                return random.ranint(1, 100) 
        elif dificuldade == 'difícil':
                return random.ranint(1, 250) 
        else:
                print("Escolha inválida. Temte novamente. :")

#número = escolha_dificuldade() # A variável recebe o número retornado
print(f"\nUm número foi gerado!")

def jogo_adivinhacao(): #def(Define a função)
        
        # O computador escolhe um número aleatório
        número = escolher_dificuldade()
        tentativa = 0
        certo = False

        #adivinhar o número
        print(f"Tente adivinhar o número. ")

#variável booleana
    while not certo:
        tentativa1 = int(input("\nDigite o seu palpite: "))
        tentativa += 1 

        if tentativa1 < numero:
            print("O número é maior. Tente novamente.")
            if abs(tentativa1 - numero) < 10: #Verifica se a diferença entre o palpite do jogador e o número correto é de 10 ou menos
                print("Você está bem perto!") 

        elif tentativa1 > numero:
            print("O número é menor. Tente novamente.")
            if abs(tentativa1 - numero) < 10: #Verifica se a diferença entre o palpite do jogador e o número correto é de 10 ou menos
                print("Você está bem perto")
        else:
            certo = True
            print(f"Parabéns! Você acertou o número em {tentativa} tentativas.") # f 

            while True:
               resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
               if resposta == "s":
                    break #recomeça o jogo
               elif resposta == "n":
                    print("Obrigado por jogar!")
                    return # para o jogo #return: encerra a execução, para o loop
               else:
                    print("\nResposta inválida. Digite uma das opções acima.")

jogo_adivinhacao() # para o jogo ser executado é preciso chamar a varia