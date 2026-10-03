class Carro:
    def __init__  (self, nome, ano, km_rodados):
        self.nome = nome
        self.ano = ano
        self.km_rodados = km_rodados

carro = Carro ("Honda Civic", "2020", "0Km")

print(carro.nome)
print(carro.km_rodados)
print(carro.ano)