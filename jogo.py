import random
a = 5
a += 3

tentativas = 3

nome_de_usuario = input("Crie um nome de usuário: ")
senha = input("Crie uma senha: ")



while True > 0:
    acessar_com_nome_de_usuario = input("Insira seu nome de usuário: ")
    acessar_com_senha = input("Insira sua senha: ")

    if(acessar_com_nome_de_usuario == nome_de_usuario and acessar_com_senha == senha):
        print("Bem vindo ao game")
        break
    else:
        print(f"Usuário ou senha incorreto \nrestam {tentativas} tentativas")
        tentativas-= 1
        
        if(tentativas == 0):
            print("Acesso bloqueado!")
            break


pontos = 0 
tentativas = 10

numero = random.randint (1, 100)

while tentativas > 0:
    resposta_tentativa = int(input("Insira um número inteiro: "))

    if(resposta_tentativa == numero):
        pontos+= 1
        print(f"Certa resposta \nSeus pontos atuais são: {pontos}")
        break
    elif(resposta_tentativa > numero):
        tentativas-= 1
        print(f"Resposta incorreta, o número é menor! \nRestam {tentativas} tentativas")
    else:
        tentativas-= 1
        print(f"Resposta incorreta, o número é maior! \nRestam {tentativas} tentativas")

    if(tentativas == 0):
        print(f"Game over!! \nSeus pontos totais foram: {pontos}")
        break


tentativas = 9

numero = random.randint (1, 100)

while tentativas > 0:
    resposta_tentativa = int(input("Insira um número inteiro: "))

    if(resposta_tentativa == numero):
        pontos+= 3
        print(f"Certa resposta \nSeus pontos atuais são: {pontos}")
        break
    elif(resposta_tentativa > numero):
        tentativas-= 1
        print(f"Resposta incorreta, o número é menor! \nRestam {tentativas} tentativas")
    else:
        tentativas-= 1
        print(f"Resposta incorreta, o número é maior! \nRestam {tentativas} tentativas")

    if(tentativas == 0):
        print(f"Game over!! \nSeus pontos totais foram: {pontos}")
        break

tentativas = 8

numero = random.randint (1, 100)

while tentativas > 0:
    resposta_tentativa = int(input("Insira um número inteiro: "))

    if(resposta_tentativa == numero):
        pontos+= 5
        print(f"Certa resposta \nSeus pontos atuais são: {pontos}")
        break
    elif(resposta_tentativa > numero):
        tentativas-= 1
        print(f"Resposta incorreta, o número é menor! \nRestam {tentativas} tentativas")
    else:
        tentativas-= 1
        print(f"Resposta incorreta, o número é maior! \nRestam {tentativas} tentativas")

    if(tentativas == 0):
        print(f"Game over!! \nSeus pontos totais foram: {pontos}")
        break

tentativas = 7

numero = random.randint (1, 100)

while tentativas > 0:
    resposta_tentativa = int(input("Insira um número inteiro: "))

    if(resposta_tentativa == numero):
        pontos+= 10
        print(f"Certa resposta \nSeus pontos atuais são: {pontos}")
        break
    elif(resposta_tentativa > numero):
        tentativas-= 1
        print(f"Resposta incorreta, o número é menor! \nRestam {tentativas} tentativas")
    else:
        tentativas-= 1
        print(f"Resposta incorreta, o número é maior! \nRestam {tentativas} tentativas")

    if(tentativas == 0):
        print(f"Game over!! \nSeus pontos totais foram: {pontos}")
        break

tentativas = 6

numero = random.randint (1, 100)

while tentativas > 0:
    resposta_tentativa = int(input("Insira um número inteiro: "))

    if(resposta_tentativa == numero):
        pontos+= 10
        print(f"Certa resposta \nSeus pontos atuais são: {pontos}")
        break
    elif(resposta_tentativa > numero):
        tentativas-= 1
        print(f"Resposta incorreta, o número é menor! \nRestam {tentativas} tentativas")
    else:
        tentativas-= 1
        print(f"Resposta incorreta, o número é maior! \nRestam {tentativas} tentativas")

    if(tentativas == 0):
        print(f"Game over!! \nSeus pontos totais foram: {pontos}")
        break

tentativas = 5

numero = random.randint (1, 100)

while tentativas > 0:
    resposta_tentativa = int(input("Insira um número inteiro: "))

    if(resposta_tentativa == numero):
        pontos+= 15
        print(f"Certa resposta \nSeus pontos atuais são: {pontos}")
        break
    elif(resposta_tentativa > numero):
        tentativas-= 1
        print(f"Resposta incorreta, o número é menor! \nRestam {tentativas} tentativas")
    else:
        tentativas-= 1
        print(f"Resposta incorreta, o número é maior! \nRestam {tentativas} tentativas")

    if(tentativas == 0):
        print(f"Game over!! \nSeus pontos totais foram: {pontos}")
        break

