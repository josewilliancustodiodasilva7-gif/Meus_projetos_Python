import random

pontos = 0
tentativas = 3

print("Jogo de matemática \n\tDe: José Willian")

def somar (a, b):
    print(f"Qual o resultado de {a} + {b}?")
    return(a + b)

def subtrair (a, b):
    print(f"Qual o resultado de {a} - {b}?")
    return(a - b)

def multiplicar (a, b):
    print(f"Qual o resultado de {a} X {b}?")
    return(a * b)

def dividir (a, b):
    print(f"Qual o resultado de {a} % {b}?")
    return(a / b)

def verificar_resposta (resposta, resultado):
    global pontos, tentativas
    
    if (resposta == resultado):
        pontos+= 10
        print(f"Certa resposta! \nVocê tem {pontos} pontos")
        
    else:
        tentativas-= 1
        print(f"Resposta errada! \nRestam apenas {tentativas} tentativas")

    if(tentativas == 0):
        print(f"Game over!! \nSeus pontos acumulados foram {pontos}")

while tentativas > 0:
    n1 = random.randint (1, 100)
    n2 = random.randint (1, 100)

    operacoes = [somar, subtrair, multiplicar, dividir]
    operacao_sorteada = random.choice(operacoes)

    resultado = operacao_sorteada(n1, n2)

    resposta = float(input("Insira sua resposta: "))

    verificar_resposta (resposta, resultado)
    