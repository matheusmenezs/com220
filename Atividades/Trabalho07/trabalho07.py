def mdc(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def mesmaFracao(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())    

class Fracao:
    
    def __init__(self, num, den):
        self.__num = num        
        self.__den = den     

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den       

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum   

    def __add__(self,outraFrac):
        novoNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum()
        novoDen = self.__den * outraFrac.getDen()
        divComum = mdc(novoNum, novoDen)
        novaFracao = Fracao(novoNum//divComum, novoDen//divComum)  
        resFracao =  novaFracao.getNum() / novaFracao.getDen()  

        if resFracao < 1:
            return novaFracao
        elif resFracao > 1:
            partInt = novaFracao.getNum() // novaFracao.getDen()
            novoNum2 = novaFracao.getNum() - novaFracao.getDen() * partInt
            fracMista = FracaoMista(partInt, novoNum2, novaFracao.getDen())
            return fracMista
        else:
            return 1
            

class FracaoMista(Fracao):

    def __init__(self, parteInteira, num, den):
        super().__init__(num, den)
        self.__parteInteira = parteInteira
    
    def getParteInteira(self):
        return self.__parteInteira

    def __str__(self):
        return str(self.__parteInteira) + ' ' + str(self.getNum()) + '/' + str(self.getDen())
    
    def __add__(self, outraFracMista):
        parteInteira = self.__parteInteira + outraFracMista.getParteInteira()
        novoNum = self.getNum() * outraFracMista.getDen() + self.getDen()  * outraFracMista.getNum()
        novoDen = self.getDen() * outraFracMista.getDen()
        divComum = mdc(novoNum, novoDen)
        novaFracao = FracaoMista(parteInteira, novoNum//divComum, novoDen//divComum)  
        resFracao =  novaFracao.getNum() / novaFracao.getDen()  

        partInt = novaFracao.getNum() // novaFracao.getDen()
        novoNum = novaFracao.getNum() - novaFracao.getDen() * partInt

        if resFracao > 1:
            fracaoMista = FracaoMista(parteInteira + partInt, novoNum, novaFracao.getDen())
            return fracaoMista
        elif resFracao < 1: 
            fracaoMista = FracaoMista(parteInteira, novoNum, novaFracao.getDen())
            return fracaoMista
        else:
            return parteInteira + 1
       


if __name__ == "__main__":
    frac1 = Fracao(7, 6) 
    frac2 = Fracao(13, 7)
    frac3 = frac1 + frac2
    print(frac3)

    print()
    frac1 = Fracao(1, 3)
    frac2 = Fracao(2, 3)
    frac3 = frac1 + frac2
    print(frac3)
    
    print()
    frac1 = FracaoMista(3, 1, 2)
    frac2 = FracaoMista(4, 2, 3)
    frac3 = frac1 + frac2
    print(frac3)
