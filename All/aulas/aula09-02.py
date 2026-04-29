import datetime
from datetime import date, datetime

hj = date.today()
"""
converter = hj.strftime("%m-%m-%Y") #mostrar a data para o usuario
print(converter)

diaA = int(input("Qual o dia do seu aniversario? "))
mesA = int(input("Qual o mes do seu aniverario? "))
aniversario = date(hj.year, mesA, diaA)
print(aniversario.strftime("%d-%m"))
if aniversario > date.today():
    diaFalta = aniversario - date.today()
    print(f"Faltam {diaFalta.days} dias para seu próximo aniversário")

if aniversario < date.today():
    print(f"Seu aniversário já passou, o proximo será em {date(hj.year+1, mesA, diaA)}")

if aniversario == date.today():
    print("Seu aniversário é hoje, parabéns")

"""

numero = int(input("Escreva um número: "))
somador = []
for i  in range(numero+1):
    somador.append(i)
    print(list(somador))