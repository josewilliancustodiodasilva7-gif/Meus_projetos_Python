import random
import time

pontos = 0
tentativas = 8

print("Bem vindo(a) ao jogo de adivinhe o número!! Adivinhe o número inteiro de 1 a 100 \nBy: José Willian")

for numero in range (5, 0, -1):
    print(numero)
    time.sleep(1)
print("Comece")

resposta = random.randint(1, 100)

while tentativas >0: 
    resposta_tentativas = int(input("Insira um número inteiro: ")) 

    if(resposta_tentativas == resposta):
        pontos+= 1
        print(f"Certa resposta \nVocê tem {pontos} pontos")
        break
    elif(resposta_tentativas < resposta):
        tentativas-= 1
        print(f"Resposta incorreta, o número é maior \nrestam {tentativas} tentativas")
    else:
        tentativas-= 1 
        print(f"Resposta incorreta \nO número é menor \nRestam {tentativas} tentativas")

    if(tentativas == 0):
        print(f"Game over \nVocê fez {pontos} pontos")

    