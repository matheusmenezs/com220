class Veiculo:

    def __init__(self, marca, cor, motorLigado):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado

    def getMarca(self):
        return self.__marca

    def getCor(self):
        return self.__cor

    def isMotorLigado(self):
        return self.__motorLigado

    def ligaMotor(self):
        if self.__motorLigado == True:
            print('Motor já está ligado')
        else:
            self.__motorLigado = True
            print('O motor acaba de ser ligado')

class Carro(Veiculo):

    def __init__(self, marca, cor, motorLigado, portaMalasCheio):
        #chama o construtor da superclasse
        super().__init__(marca, cor, motorLigado)
        self.__portaMalasCheio = portaMalasCheio

    def isPortaMalasCheio(self):
        return self.__portaMalasCheio

    def enchePortaMalas(self):
        if(self.__portaMalasCheio == True):
            print('O porta malas já está cheio')
        else:
            self.__portaMalasCheio = True
            print('O pora malas acaba de ser cheio')

    def mostraAtributos(self):
        print('Este carro é um {} {}'.format(self.getMarca(), self.getCor()))
        if(self.isMotorLigado()):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')
        if(self.isPortaMalasCheio()):
            print('Seu porta malas está cheio')
        else:
            print('Seu porta malas está vazio')

class Motocicleta(Veiculo):

    def __init__(self, marca, cor, motorLigado, estilo):
        #chama o construtor da superclasse
        super().__init__(marca, cor, motorLigado)
        self.__estilo = estilo

    def getEstilo(self):
        return self.__estilo

    def mostraAtributos(self):
        print('Esta moto é uma {} {}'.format(self.getMarca(), self.getCor()))
        if(self.isMotorLigado()):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')

if __name__ == "__main__":
    m = Motocicleta('Honda', 'azul', False, 'naked')
    m.mostraAtributos()
    m.ligaMotor()
    m.mostraAtributos()
    print('------------')
    c = Carro('Chevroler', 'branco', False, False)
    c.mostraAtributos()
    c.enchePortaMalas()
    c.ligaMotor()
    c.mostraAtributos()

       