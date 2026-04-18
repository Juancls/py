class Candidato:
    def __init__(self, nome, idade, sexo, experiencia):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.experiencia = experiencia

    def mostrar(self):
        print(self.nome, self.sexo, self.idade, self.experiencia)

    def mediaIdades(self, somaIdadesF, somaIdadesM, qtdM, qtdH, mostrarRelatorio):
        expM = 0
        expH = 0
        somaIdadesM = 0
        somaIdadesF = 0
        qtdM = 0
        qtdH = 0
        homensMaior45 = 0
        mulheresMaior45 = 0
        mulheres21exp = 0

        for candidato in pessoas:
            # Conta totais por sexo
            if candidato.sexo.upper() == 'F':
                qtdM += 1
                if candidato.experiencia.upper() == 'S':
                    expM += 1
                    somaIdadesF += candidato.idade
                    if candidato.idade < 21:
                        mulheres21exp += 1
                if candidato.idade > 45:
                    mulheresMaior45 += 1

            if candidato.sexo.upper() == 'M':
                qtdH += 1
                if candidato.experiencia.upper() == 'S':
                    expH += 1
                    somaIdadesM += candidato.idade
                if candidato.idade > 45:
                    homensMaior45 += 1

        if mostrarRelatorio:
            print("\n--- RELATÓRIO FINAL ---")
            print(f"{qtdM} Mulheres cadastradas")
            print(f"{qtdH} Homens cadastrados")

            if expH > 0:
                print(f"A média de idade dos homens com experiência é: {somaIdadesM/expH:.2f}")
            else:
                print("Não houve homens com experiência para calcular a média.")

            if expM > 0:
                print(f"A média de idade das mulheres com experiência é: {somaIdadesF/expM:.2f}")
            else:
                print("Não houve mulheres com experiência para calcular a média.")

            print(f"Mulheres com menos de 21 anos e experiência: {mulheres21exp}")

            if qtdH > 0:
                print(f"A porcentagem de homens maiores que 45 anos é: {(homensMaior45/qtdH)*100:.2f}%")
            if qtdM > 0:
                print(f"A porcentagem de mulheres maiores que 45 anos é: {(mulheresMaior45/qtdM)*100:.2f}%")


pessoas = []
somaIdadesF = 0
somaIdadesM = 0
qtdM = 0
qtdH = 0

qtn = int(input("Quantas pessoas você quer cadastrar?: "))

for i in range(qtn):
    print(f"\nCadastro do {i+1}º candidato")
    nomeCand = input("Digite seu nome: ").title()
    idadeCand = int(input("Digite sua idade: "))
    sexoCand = input("Digite seu sexo M/F: ").upper()
    exp = input("Você possui experiencia? S/N: ").upper()

    novo_candidato = Candidato(nomeCand, idadeCand, sexoCand, exp)
    pessoas.append(novo_candidato)

print("\n--- LISTA DE CANDIDATOS ---")
for i, p in enumerate(pessoas):
    p.mostrar()
    # Passa True apenas para o último candidato da lista para exibir o relatório
    p.mediaIdades(somaIdadesF, somaIdadesM, qtdM, qtdH, i == (len(pessoas) - 1))