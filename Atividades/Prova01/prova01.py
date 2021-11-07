from abc import ABC, abstractmethod

class Funcionario:

    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensalFunc = []
 
    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getPontoMensalFunc(self):
        return self.__pontoMensalFunc

    def adicionaPonto(self, mes, ano, faltas, atrasos ):
        ponto = PontoFunc(mes, ano, faltas, atrasos)
        self.__pontoMensalFunc.append(ponto)
        
    def lancaFaltas(self, mes, ano, faltas):
        for ponto in self.__pontoMensalFunc:
            if (ponto.getMes() == mes and ponto.getAno() == ano):
                ponto.lancaFaltas(faltas)

    def lancaAtrasos(self, mes, ano, atrasos):
        for ponto in self.__pontoMensalFunc:
            if (ponto.getMes() == mes and ponto.getAno() == ano):
                ponto.lancaAtrasos(atrasos)

    def imprimeFolha(self, mes, ano):
        print('Código: {}'.format(self.__codigo))
        print('Nome: {}'.format(self.__nome))
        print('Salário: {}'.format(self.calculaSalario(mes, ano)))
        print('Bônus: {:.2f}'.format(self.calculaBonus(mes, ano)))  


    @abstractmethod
    def CalculaSalario(self):
        pass

    def CalculaBonus(self):
        pass
        

class PontoFunc:

    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos
    
    def getMes(self):
        return self.__mes

    def getAno(self):
        return self.__ano
    
    def getNroFaltas(self):
        return self.__nroFaltas

    def getNroAtrasos(self):
        return self.__nroAtrasos
    
    def lancaFaltas(self, nroFaltas):
        self.__nroFaltas += nroFaltas

    def lancaAtrasos(self, nroAtrasos):
        self.__nroAtrasos += nroAtrasos


class Professor(Funcionario):

    def __init__(self, codigo, nome, titulacao, salarioHora, nroHoras):
        super().__init__(codigo, nome)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroHoras = nroHoras   

    def getTitulacao(self):
        return self.__titulacao

    def getNroHoras(self):
        return self.__nroHoras

    def setSalarioHora(self, salarioHora):
        self.__salarioHora = salarioHora 

    def getSalarioHora(self):
        return self.__salarioHora

    def calculaSalario(self, mes, ano):
        for ficha in self.getPontoMensalFunc():
            if (ficha.getMes() == mes and ficha.getAno() == ano):
                nroFaltas = ficha.getNroFaltas()
        salProf = (self.__salarioHora * self.__nroHoras) - (self.__salarioHora * nroFaltas)
        return salProf

    def calculaBonus(self, mes, ano):
        n = 0
        porcBonus = 0.1
  
        for ficha in self.getPontoMensalFunc():
            if (ficha.getMes() == mes and ficha.getAno() == ano):
                nroAtrasos = ficha.getNroAtrasos()
        while(porcBonus != 0):
            if(nroAtrasos == n):
                porcBonus = porcBonus - (0.01 * n)
                break
            n = n + 1
        return (self.calculaSalario(mes, ano) * porcBonus)


class TecAdmin(Funcionario):

    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome) 
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal

    def getFuncao(self):
        return self.__funcao

    def getSalarioMensal(self):
        return self.__salarioMensal

    def calculaSalario(self, mes, ano):
        for ficha in self.getPontoMensalFunc():
            if (ficha.getMes() == mes and ficha.getAno() == ano):
                nroFaltas = ficha.getNroFaltas()
        salTec = self.__salarioMensal - ((self.__salarioMensal / 30)*nroFaltas)
        return salTec

    def calculaBonus(self, mes, ano):
        n = 0
        porcBonus = 0.08
        
        for ficha in self.getPontoMensalFunc():
            if (ficha.getMes() == mes and ficha.getAno() == ano):
                nroAtrasos = ficha.getNroAtrasos()
        while(porcBonus!=0):
            if(nroAtrasos == n):
                porcBonus = porcBonus - (0.01 * n)
                break
            n = n + 1
        return (self.calculaSalario(mes, ano) * porcBonus)
    
 
if __name__ == "__main__":

    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()