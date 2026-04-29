"""
#função não nomeada (anonima) - Lambda
#recebe qualquer numero de argumentos mas contem somente uma expressão
#retornar objetos de funções
#usar em periodos curtos
#lambda<argumento> : expressão

#função regular que retorna o resto da divisão por 2. Se for 0, o numero é par, se for um, é impar
def par(num):
    return num%2

x = par(10)
if x == 0:
    print("Par")
else:
    print("Impar")

lambda  num: num%2

def multa(numero):
    return lambda x: x*numero #o "x" é o valor de cada culta, passado pelo variavel

m10 = multa(10) #aqui a variavel se torna uma função, por isto é preciso passar um parametro ao utilizar para realziar o calculo
print(f'O valor da multa é de R${m10(1000)}')
m50 = multa(50)
print(f'O valor da multa é de R${m50(100)}')

#função filter
#filter(objeto, interavel)
#objeto deve ser uma função lambda que retorna um valor Booleano (true ou false)

numeros = [2, 4, 6, 8, 10, 45, 32, 78, 21, 0]
filtrar = list(filter(lambda x: x >= 7, numeros))
print(filtrar)

fatiar = filtrar[2:4]
print(fatiar)

mapear = list(map(lambda x: x%2, numeros))
print(mapear)

#formula para calcular juros compostos
#p = montante parcial (investimento inicial)
#r = taxa de juros nominal anula (como decimal)
#n = numero de vezes que os juros compostos por ano
#t = numero de anos

def montante(p, r, n, t):
    a = p * (1 + r/n) ** (n * t)
    
    return a
"""
jurosComp = lambda p, r, n, t,: p * (1 + r/n) ** (n * t)
print(f"Total de juros acumulados R${jurosComp(1000, .08, 12, 5):.2f}")