from abc import ABC, abstractmethod 

class Professor:

    def __init__(self, nome, matricula, cargaHoraria):
       self.__nome = nome
       self.__matricula = matricula
       self.__cargaHoraria = cargaHoraria

    def getNome(self):
        return self.__nome

    def getMatricula(self):
        return self.__matricula

    def getCargaHoraria(self):
        return self.__cargaHoraria
    
    @abstractmethod
    def getSalario(self):
        pass

