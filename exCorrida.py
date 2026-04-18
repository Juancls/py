corrida = {}

# Simulando o "Do-While" para cadastrar
while True:
    nome = input("Digite o nome do corredor (ou Enter para sair): ")
    if nome == '':  # Comparando com string vazia (o "null" que você buscou)
        break

    # Usamos [] para ser uma LISTA (ordenada e acessível por índice)
    t1 = float(input("Tempo 1: "))
    t2 = float(input("Tempo 2: "))
    t3 = float(input("Tempo 3: "))
    corrida[nome] = [t1, t2, t3]

print("\n--- Resultados ---")

# Percorrendo o dicionário
for nome in corrida.keys():
    # Acessando os itens da lista pelo índice
    # corrida[nome] é a lista, [0] é a primeira posição
    print(f"Corredor: {nome}")
    print(f"Volta 1: {corrida[nome][0]}s")
    print(f"Volta 2: {corrida[nome][1]}s")
    print(f"Volta 3: {corrida[nome][2]}s")
    print("-" * 20)

resultado = []

for nome in corrida:
    tempoTotal = sum(corrida[nome])
    resultado.append((nome, tempoTotal))

resultado.sort(key=lambda x: x[1])
posicoes = ["1º Lugar", "2º Lugar", "3º Lugar"]
print("------- Resultado ------")

for i in range(len(resultado)):
    if i < 3:
        nome, tempo = resultado[i]
        print(f"{posicoes[i]}: {nome} com {tempo:.2f}s")