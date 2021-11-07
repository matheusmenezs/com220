from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, listaDisc):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__listaDisc = listaDisc

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getIdade(self):
        return self.__idade

    def getListaDisc(self):
        return self.__listaDisc

    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao, listaDisc):
        super().__init__(nome, endereco, idade, listaDisc)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereço: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Titulação: {}'.format(self.getTitulacao()))
        print('Disciplinas ministradas:')
        listaDisc = self.getListaDisc()
        for disc in listaDisc:
            print('Nome: {} - Carga horária: {}'.format(disc.getNomeDisc(), disc.getCargaHoraria()))
            
class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso, listaDisc):
        super().__init__(nome, endereco, idade, listaDisc)
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereço: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Curso: {}'.format(self.getCurso()))
        print('Disciplinas cursadas:')
        listaDisc = self.getListaDisc()
        for disc in listaDisc:
            print('Nome: {} - Carga horária: {}'.format(disc.getNomeDisc(), disc.getCargaHoraria()))        


class Disciplina():
    def __init__(self, nomeDisc, cargaHoraria):
        self.__nomeDisc = nomeDisc
        self.__cargaHoraria = cargaHoraria

    def getNomeDisc(self):
        return self.__nomeDisc

    def getCargaHoraria(self):
        return self.__cargaHoraria

if __name__ == "__main__":
    disc1 = Disciplina('Programacao OO', 64)
    disc2 = Disciplina('Estruturas de Dados', 64)
    disc3 = Disciplina('Bancod de Dados', 64)
    listaDisc1 = [disc1, disc2]
    listaDisc2 = [disc2, disc3]

    prof = Professor('Joao', 'Av. BPS 1303', 35, 'doutorado', listaDisc1)       
    prof.printDescricao()
    print()
    aluno = Aluno('Pedro', 'Av. Cesario Alvim', 20, 'SIN', listaDisc2)
    aluno.printDescricao()