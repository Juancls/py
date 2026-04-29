class Carro:

    def _init_(self,fabricante,modelo,ano,chassi,cor="prata"):
        self.fabricante = fabricante
        self.modelo=modelo
        self.ano= int(ano)
        self.cor=cor
        self.chassi= int(chassi)
        self.hodometro=0
        self.tanque=5

    def info (self):
        print (f"Fabricante : {self.fabricante}\nModelo: {self.modelo}\n Ano {self.ano}\nCor : {self.ano}\n Chassi: {self.chassi}\n Hodometro: {self.hodrometro}km rodados \n Tamque: {self.tanque}")

    def ler_hodometro(self):
        print(f"Este caro tem {self.hodometro}km rodados.")

    def atualizar_hodometro (self, km):
        if self.hodometro < km:
            self.hodometro =km
        else:
            print ("Não poder reduzir o hodometro.È crime!")
        return f"{self.hodometro}km rodados!"

    def incrementar_hodometro(self, km):
        if km >=0 :
            self.hodometro +=km
        else:
            print("Não pode atualizar o hodrometro.E crime")
        return f"{self.hodometro} km rodados"

    def _str_(self):
        #e usado para retornar uma representação de string de um objeto.Quando existir os dois metodos,este prevalece
        return f"<Carro> Fabricante : {self.fabricante}\nModelo: {self.modelo}\n Ano {self.ano}\nCor : {self.ano}\n Chassi: {self.chassi}\n Hodometro: {self.hodrometro}km rodados \n Tamque: {self.tanque}"


    def _repr_(self):
        #E usado para retornar uma apresentação de um objeto e é normalmente utilizado para debug.
        return f" <Carro ({self.fabricante},{self.modelo},{self.ano},{self.chassi},{self.cor})>"


