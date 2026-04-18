# aula para conhecer a usabilidade das tags
# brack: finaliza um bloco
# continue: passa para a proxima interação do loop
# pass: permite que o codigo continue executando sem erros
# else: while e for podem ser usados junto com o else
#quando termina a execução do while, ou seja, a condição for falsa, o else sera executado.
#quando o for terminar, o else sera executado

"""
nomes = ["Paula", "Ana", "Muller"]
#adicionar elemento à lista
novoName = input("Escerva um novo nome para registro: ")
nomes.append(novoName)
print(nomes)

listaNum = []
listaQuad = []
for i in range(10):
    listaNum.append(i)
    listaQuad.append(i**2)
print(listaNum)
print(listaQuad)


lista1 =[1, 2, 3]
lista2 =[10, 20, 30]
lista3 =[100, 200, 300]
listaGeral = []


for i in range(3):
    listaGeral.append(lista1[i])
    listaGeral.append(lista2[i])
    listaGeral.append(lista3[i])
print(listaGeral)

#extend(intervalo): união de listas
#remove(elemento) remove o primeiro elemento encontrado
lista1 =[1, 2, 3]
lista2 =[10, 20, 30]
c = []
c.extend(lista1+lista2)
print(c)


#index(x)
numeros =[10, 20, 30]
ind4 = numeros.index(20)
print(ind4)

#pop([x]) valor do indice que eu quero remover
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
print(numeros)
numeros.pop() #remove o ultimo da lista se não passar nenhum item
numeros.pop(5) #remove o 5
print(numeros)

#sort(chave, reverse) usado para ordem crescente ou decrescente
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
numeros.sort(reverse=True)
print(numeros)


#reverse() inverte a lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
numeros.reverse()
print(numeros)

#compreensao de lista
lista = []
for item in range(10):
    lista.append(item**2)
print(lista)

lista1 = [item**2 for item in range(10)]
print(lista1)

nomeLista = ['ana', 'paula', 'muller', 'giancoli']
res = []
for i in nomeLista:
    res.append(str(i).upper())
print(res)

res = [str(i).upper() for i in nomeLista]
print(res)

#[expr for item in lista if condicao]
res =[]
for i in range(20):
    if i%2==0:
        res.append(i)
print(res)

res = [n for n in range(20) if n % 2 == 0]
print(res)

numeros = []
res = []
for i in range(100):
    if i % 5 == 0:
        res.append(i)
print(res)

res = [i for i in range(100) if i % 5 == 0 and i % 6 ==0]
print(res)
"""

