import Veiculo
class Caminhao(Veiculo.Veiculo):
    def __init__(self, chassi, marca, modelo, ano, capacidadeDeCarga, numDeEixos, tipoDeCombustivel): 
        super().__init__(marca, modelo, ano, chassi)
        super().set_tipo("Caminhao")
        self.capacidadeDeCarga = capacidadeDeCarga
        self.numDeEixos = numDeEixos
        self.tipoDeCombustivel = tipoDeCombustivel
        self.marcha = 0
        self.velocidade = 0
        self.farolLigado = False

    def ligar( self ):
        self.marcha = 1

    def desligar( self ):
        self.marcha = 0

    def get_marcha ( self ):
        return self.marcha
    
    def acelerar( self ):
        self.velocidade = 60

    def get_acelerar ( self ):
        return self.velocidade
    
    def ligarFarol( self ):
        self.farolLigado = True

    def get_ligarFarol(self):
        return self.farolLigado

Caminhaozinho = Caminhao("Volkswagen","VW 9.170 DRC 4X2",'2023','1A3N6B9C4D2E5F8G', 20, 4, "diesel")
Caminhaozinho.ligar()
print(Caminhaozinho.get_marcha())
Caminhaozinho.ligarFarol()
print(Caminhaozinho.get_ligarFarol())
Caminhaozinho.acelerar()
print(Caminhaozinho.get_acelerar())
print(Caminhaozinho.get_tipo())
print(Caminhaozinho.numDeEixos)
print(Caminhaozinho.tipoDeCombustivel)
