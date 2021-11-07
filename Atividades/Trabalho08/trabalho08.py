from abc import ABC, abstractmethod

class TitulacaoInvalida(Exception): #Titulacao deve ser doutor
    pass

class IdadeProfInvalida(Exception): #Idade >= 30
    pass

class CursoInvalido(Exception): #Curso deve ser CCO ou SIN
    pass

class IdadeAlunoInvalida(Exception): #Idade >= 18
    pass

class CpfDuplicado(Exception): #Cpf deve ser diferente
    pass

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf
    
    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getIdade(self):
        return self.__idade
    
    def getCpf(self):
        return self.__cpf

    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao
    
    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereço: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('CPF: {}'.format(self.getCpf()))
        print('Titulação: {}'.format(self.getTitulacao())) 

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso
    
    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereço: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('CPF: {}'.format(self.getCpf()))
        print('Curso: {}'.format(self.getCurso())) 


if __name__ == "__main__":
    aluno1 = Aluno("Pedro", "Centro", 17, 123456, "CCO") #Idade inválida
    aluno2 = Aluno("Julia", "Bps", 19, 123456, "ECO") #Curso inválido
    aluno3 = Aluno("João", "Açude", 20, 456789, "SIN") #OK
    aluno4 = Aluno("Matheus", "Morro Chiq", 22, 456789, "SIN") #Cpf repetido
    aluno5 = Aluno("Caio", "Cruzeiro", 18, 963123, "CCO") #OK
    prof1 = Professor("Luis", "Pinheirinho", 27, 14789, "Doutor") #Idade inválida
    prof2 = Professor("Elisa", "Varginha", 30, 987456, "Doutor") #OK
    prof3 = Professor("Leonardo", "Bps", 32, 147987, "Mestre") #Titulação inválida
    prof4 = Professor("José", "Avenida", 30, 456789, "Doutor") #Cpf igual ao do aluno
    prof5 = Professor("Antonio", "Centro", 35, 369874, "Doutor") #OK

    listaAl = [aluno1, aluno2, aluno3, aluno4, aluno5] 
    listaProf = [prof1, prof2, prof3, prof4, prof5]  
    cadastro = [] #Cadastro de alunos e professores
    cadcpf = {}  #Cpf de professores e alunos 

    print('------------- Falhas -------------')
    for aluno in listaAl:

        try:
            if aluno.getCpf() in cadcpf:
                raise CpfDuplicado
            if aluno.getIdade() < 18:  
                raise IdadeAlunoInvalida()  
            if aluno.getCurso() != "SIN" and aluno.getCurso() != "CCO":
                raise CursoInvalido
            else:
                cadcpf[aluno.getCpf()] = aluno
                cadastro.append(aluno)   

        except CpfDuplicado:
            print("CPF aluno repetido: %d" % aluno.getCpf())
        except IdadeAlunoInvalida:
            print("Idade aluno inválida: %d" % aluno.getIdade())
        except CursoInvalido:
            print("Curso inválido: %s" % aluno.getCurso())

    print()
    for prof in listaProf:
        
        try:
            if prof.getCpf() in cadcpf:
                raise CpfDuplicado
            if prof.getIdade() < 30:  
                raise IdadeProfInvalida()          
            if prof.getTitulacao() != "Doutor":
                raise TitulacaoInvalida
            else:
                cadcpf[prof.getCpf()] = prof
                cadastro.append(prof)   

        except CpfDuplicado:
            print("CPF professor repetido: %s" % prof.getCpf())
        except IdadeProfInvalida:
            print("Idade professor inválida: %d" % prof.getIdade())
        except TitulacaoInvalida:
            print("Titulação inválida: %s" % prof.getTitulacao())

    print()
    print('------ Pessoas cadastradas ------')
    for pessoa in cadastro:
        pessoa.printDescricao()
        print()
   

   

 