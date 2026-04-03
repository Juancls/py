notas = {}

print("Cadastro de notas de alunos")
while True:
    nome = input("Nome aluno: ")  # guarda o nome
    if nome == '': #verifica se a entrada foi vazio, se for, o codigo encerra e pula para o proximo bloco
        break
    else:
        notas[nome] = [float(input(f"Nota primeira avaliação: ")),
                   float(input(f"Nota segunda avaliação: "))]  # cadastra o nome e coloca duas notas para o mesmo


print( "Deseja ver a nota de qual aluno: ")
for nome in notas.keys(): #para cada nome contido nas keys(nomes) do dicionario irá executar algo
    print(f"- {nome}") #printa os nomes
escolha = input("")
if escolha in notas: #verifica se o nomes escolhido esta no dicionario
    print(f"As notas do aluno {escolha} são: ")
    for i in range(2):
        print(notas[escolha][i]) #print de todas as notas
    print(f"A media do {escolha} é: ")
    print((notas[escolha][0]+notas[escolha][1])/2) #print com a media das notas
else:
    print(f"Nenhum aluno com o nome {escolha} cadastrado")