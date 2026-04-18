"""
notas1 = {}
for k in range(3):
    nome = input("Nome: ")
    notas1[nome] = [float(input("Nota 1: ")), float(input("Nota 2: ")), float(input("Nota 3: "))]
print(notas1)
"""

p = set('abracadabra')
print(p)
k = set('alacazam')
print(k)

#o que existe em p, mas não existe em k (opeação de diferença p - k)
z = p - k
print(z)

#Elementos que existem em ambos p, ou k, ou em ambos (opeação união)
z = p | k
print(z)

#Elementos que existem em ambos p e k ( operação interseção p & k)
z = p & k

#Elementos que existem em p, ou em q, mas não é comum nos dois (operação de diferença entre p ^ k)
z = p ^ k