import Veiculo
class Carro ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, potencia, tipoCarro ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Carro")
        self.potencia = potencia
        self.tipoCarro = tipoCarro
        self.marcha = 0
        self.velocidade = 0
        self.farolLigado = False
    def ligar( self ):
        return self.marcha
    
    def desligar( self ):
        self.marcha = 0

    def acelerar( self ):
        self.velocidade = 60

    def get_acelerar ( self ):
        return self.velocidade
    
    def ligarFarol( self ):
        self.farolLigado = True

    def get_ligarFarol(self):
        return self.farolLigado
    
""" Aqui comeca o teste """
CarroNovo = Carro('8885AZKG01Z12A33921312', 'JAC', 'J3', '2022', 2.0, 'HATCH')
print(CarroNovo.ligar())
CarroNovo.ligarFarol()
print(CarroNovo.get_ligarFarol())
CarroNovo.acelerar()
print(CarroNovo.get_acelerar())
print(CarroNovo.get_tipo())
print(CarroNovo.potencia)
print(CarroNovo.tipoCarro)
