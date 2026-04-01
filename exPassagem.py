assentosJanela = []
assentosCorredor = []
onibus = []

# Inicialização correta
for i in range(1, 11):
    if i % 2 == 0:
        assentosJanela.append(i)
    else:
        assentosCorredor.append(i)

onibus = sorted(assentosCorredor + assentosJanela)
poltrona = [0] * len(onibus)  # Cria a lista de ocupação com zeros

print(f"Poltronas disponíveis no ônibus: {onibus}")

while 0 in poltrona:
    escolhalocalPoltrona = input("\nJanela ou Corredor? ").strip().title()

    if escolhalocalPoltrona == "Corredor":
        print(f"Opções no corredor: {assentosCorredor}")
        escolha = int(input("N° poltrona: "))

        if escolha in assentosCorredor:
            indice = onibus.index(escolha)
            if poltrona[indice] == 1:
                print("❌ Poltrona ocupada!")
            else:
                poltrona[indice] = 1
                print("✅ Compra realizada com sucesso!")
        else:
            print("Esta poltrona não é no corredor!")

    elif escolhalocalPoltrona == "Janela":
        print(f"Opções na janela: {assentosJanela}")
        escolha = int(input("N° poltrona: "))

        if escolha in assentosJanela:
            indice = onibus.index(escolha)
            #Usar 'indice' em vez do número da poltrona
            if poltrona[indice] == 1:
                print("❌ Poltrona ocupada!")
            else:
                poltrona[indice] = 1
                print("✅ Compra realizada com sucesso!")
        else:
            print("Esta poltrona não é na janela!")

print("\n🚌 ÔNIBUS LOTADO! Não há mais assentos disponíveis.")