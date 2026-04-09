"""
nomes = ["lucas", "juan", "Carol", "ana", "daniel", "joao", "luigi", "leo"]

cont = 0
novos = []
novosInsert = []
for nome in nomes[:]:
    if len(nome) >= 5:
        cont += 1
        novos.append(nome)
        novosInsert.insert(0, nome)

print(cont)
print(novos)
print(novosInsert)
"""

"""
nomesCad = []
cont = 0
while len(nomesCad) < 5:
    nome = input("Digite um nome: ")
    nomesCad.insert(cont, nome)
    cont += 1
print(nomesCad)

nomes = []
for i in range(5):
    nomes.append(input("Nome: ").title())
print(nomes)


numeros = []
for i in range(0, 31, 5):
    numeros.append(i)

print(numeros)


nomes = ["lucas", "juan", "Carol", "ana", "daniel", "joao", "luigi", "leo"]
for i in range(len(nomes)):
    print(i, nomes[i])

idades = [10, 11, 12, 34]
soma = 0
for idade in idades:
    soma += idade
print(sum(idades))
print(len(idades))
print(f"{sum(idades)/len(idades):.2f}")

numero = [1, 2, 3, 4, 5]
ao_quadrado = lambda x: x**2 #lambda é uma função unica em linha, recebe um valor e ja retorna o mesmo
squared = list(map(ao_quadrado, numero))
print(squared)
"""

