from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
        
        
    def getNome(self):
        return self.__nome

    def getTelefone(self):
        return self.__telefone

    def setNome(self, nome):
        self.__nome = nome

    def setTelefone(self, telefone):
        self.__telefone = telefone
      

    @abstractmethod
    def getSalario(self):
        pass


class EmpMensalista(EmpDomestica):
    def __init__(self, nome, telefone, salarioMensal):
        super().__init__(nome, telefone)
        self.__salarioMensal = salarioMensal

    def getSalario(self):
        return self.__salarioMensal


class EmpDiarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, salarioDia):
        super().__init__(nome, telefone)
        self.__salarioDia = salarioDia
        self.__diasTrabalhados = diasTrabalhados

    def getSalario(self):
        return self.__salarioDia * self.__diasTrabalhados


class EmpHorista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, salarioHora):
        super().__init__(nome, telefone)
        self.__salarioHora = salarioHora
        self.__horasTrabalhadas = horasTrabalhadas

    def getSalario(self):
        return self.__salarioHora * self.__horasTrabalhadas


if __name__ == "__main__":
    
    print('-------------------- Lista de empregadas -------------------- ')
    print()
    emp1 = EmpMensalista('Maria Betania', '123456789', 1000)
    emp2 = EmpDiarista('Joana Silva', '987654321', 20, 55)
    emp3 = EmpHorista('Marcia Aparecida', '147896321', 160, 10)
    emps = [emp1, emp2, emp3]
    for emp in emps:
      print ('Nome: {} - Telefone: {} - Salario: R${}'.format(emp.getNome(), emp.getTelefone(), emp.getSalario()))

    melhorOpc = emp1 
    for emp in emps:
        if(emp.getSalario() < melhorOpc.getSalario()):
            melhorOpc = emp

    print('\nA empregada mais barata para a república é: {} - Telefone: {} - Salário: R${}'.format(melhorOpc.getNome(), melhorOpc.getTelefone(), melhorOpc.getSalario()))


    
   
    
      

    


