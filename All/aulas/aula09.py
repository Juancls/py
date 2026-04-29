#utilizando Alais(apelido) para algum import que possa ter o nome muito grande
#from datetime import date as dt
#dt()
"""
#função built-in
#funções regulares em função (return), procedimento (não tem, print)


#função regular com retorno e passagem de paramentros/argumetos
def somar(a, b):
    return a + b

k = int(input("Numero 1: "))
j = int(input("Numero 2: "))

#passagem de valores posicionais
#print(somar(k, j))

#passagem de valores nomeados
print(somar(b=k, a=j))


#função regular com retorno e sem passagem de parametro/argumentos
def somarAll():
    k = int(input("Numero 1: "))
    j = int(input("Numero 2: "))
    return k+j
print(somarAll())

#função procedimento (não tem retrono)
def convite(nomes):
    for nome in nomes:
        msg = "Oi " + str(nome).title() + ". Seja bem vindo!"
        print(msg)
listaNomes =["Ana", "Juan", "Karolina"]
convite(listaNomes)



#função que recebe varios argumentos
def carros(*marcas): # o "*" permite que varios argumetos sejam passados
    for i in marcas:
        print(i)

carros("Honda")
carros("VolksWagen", "Toyota", "GM", "Fiat")

def carros(**marcas): # quando tem dois "*", a função cria um dicionario
    fabricante = {}
    for key, value in marcas.items():
        fabricante[key] = value
    print(fabricante)

carros( nome ="Juan", fabricante = "Toyota", idade = "21", cidade= "Atibaia")
"""

