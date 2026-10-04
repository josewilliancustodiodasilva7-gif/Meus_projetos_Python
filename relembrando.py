print("Estrutura de decisão; Estrutura de repetição; def; listas.")

idade = (int(input("Insira sua idade: ")))

if(idade <= 12):
    print("Criança")
elif (idade <= 18):
    print("Adolescente")
elif (idade <= 49):
    print("Adulto")
else:
    print("Idoso")

palavra = input("Insira uma palavra: ")
x = 0

for i in palavra:
    x+= 1 

print(f"Sua palavra tem {x} letras (contando com os espaços)")

usuario = input("Crie um nome de usuário: ")
senha = input("Crie uma senha: ")
tentativas = 3

while True:
    usuario_tentativa = input("Insira seu usuário: ")
    senha_tentativa = input("Insira sua senha: ")

    if(usuario_tentativa == usuario and senha_tentativa == senha):
        print("Acesso concedido")
        break
    else:
        print("Usuário ou senha incorreto!")
        tentativas-= 1

    if(tentativas == 0):
        print("Acesso bloqueado!!")
        break

def informacoes (nome, idade, cpf):
    print(f"Seu nome é {nome}")
    print(f"Sua idade é {idade}")
    print(f"Seu CPF é {cpf}")

informacoes ("José", "16 anos", "555.555-55")


lista_de_compras = ["Banana", "Uva", "Manga", "Ovo"]

lista_de_compras.sort()
print(lista_de_compras)

lista_de_compras.append("Lasanha")

lista_de_compras.sort()


lista_de_compras.reverse()

print(lista_de_compras)