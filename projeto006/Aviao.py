import Veiculo
class Aviao(Veiculo.Veiculo):
    def __init__(self, chassi, marca, modelo, ano, numeroDeSerie): 
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Aviao")
        self.numeroDeSerie = numeroDeSerie
        self.motorLigado = False
        self.emVoo = False
        
    def ligar( self ):
        self.motorLigado = True
        print("O avião está ligado")

    def desligar( self ):
        self.motorLigado = False
        print("O avião está desligado")

    def decolar( self ):
        self.emVoo = True

    def get_decolar(self):
        return self.emVoo

Aviaozinho = Aviao(None, "FicAir", "FicJet-2000", 2023, "ABC123XYZ456")
Aviaozinho.ligar()
Aviaozinho.decolar()
print(Aviaozinho.get_decolar())
print(Aviaozinho.get_tipo())
print(Aviaozinho.numeroDeSerie)
