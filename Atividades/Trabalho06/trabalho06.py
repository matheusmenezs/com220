class Curso:

    def __init__(self, nome):
        self.__nome = nome
        self.__alunos = []

    def getNome(self):
        return self.__nome
    
    def getAlunos(self):
        return self.__alunos
    
    def getGrade(self):
        return self.__grade

    def addGrade(self, grade): 
        self.__grade = grade

    def addAluno(self, aluno):
        self.__alunos.append(aluno)


class Disciplina:

    def __init__(self, codigo, nome, cargaHoraria, grade):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        self.__grade = grade

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getCargaHoraria(self):
        return self.__cargaHoraria

    def getGrade(self):
        return self.__grade

    def getCurso(self):
        return self.__grade.getCurso()


class Grade:

    def __init__(self, ano, curso):
        self.__ano = ano
        self.__curso = curso
        self.__disciplinas = []

    def getAno(self):
        return self.__ano

    def getCurso(self):
        return self.__curso

    def addDisc(self, disciplina):
        self.__disciplinas.append(disciplina)


class Aluno:

    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso
        self.__historico = Historico(self)

    def getNroMatric(self):
        return self.__nroMatric
    
    def getNome(self):
        return self.__nome

    def addDisciplina(self, disciplina):
        if (disciplina.getCurso() == self.__curso):
            self.__historico.addDiscObrigatorias(disciplina)
        else:
            self.__historico.addDiscEletivas(disciplina)
    
    def getHistorico(self):
        return self.__historico


class Historico:

    def __init__(self, aluno):
        self.__aluno = aluno
        self.__discObrigatorias = []
        self.__discEletivas = []
    
    def getDiscObrigatorias(self):
        return self.__discObrigatorias

    def getDiscEletivas(self):
        return self.__discEletivas

    def getAluno(self):
        return self.__aluno

    def getNomeAluno(self):
        return self.__aluno.getNome()

    def addDiscObrigatorias(self, disciplina):
        self.__discObrigatorias.append(disciplina)

    def addDiscEletivas(self, disciplina):
        self.__discEletivas.append(disciplina)
        

if __name__ == "__main__":

    curso1 = Curso("Sistemas de Informação")
    curso2 = Curso("Química Bacharelado")
    grade1 = Grade(2016, curso1)
    grade2 = Grade(2018, curso2)
    disc1 = Disciplina('COM110', 'Fundamentos de Programação', 64, grade1)
    disc2 = Disciplina('COM111', 'Algoritmos e Estutura de Dados I', 64, grade1)
    disc3 = Disciplina('COM220', 'Programação OO', 64, grade1)
    disc4 = Disciplina('COM210', 'Engenharia de Software', 64, grade1)
    disc5 = Disciplina('MAT001',"Cálculo I", 96, grade2)
    disc6 = Disciplina('QUI011',"Metodologia Científica", 64, grade2)
    disc7 = Disciplina('QUI017',"Química Geral Experimental", 32, grade2)
    
    aluno1 = Aluno(20192020, "Matheus Menezes", curso1)
    curso1.addAluno(aluno1)
    aluno1.addDisciplina(disc1)
    aluno1.addDisciplina(disc2)
    aluno1.addDisciplina(disc3)
    aluno1.addDisciplina(disc4)
    aluno1.addDisciplina(disc6)
    aluno1.addDisciplina(disc7)

    historico1 = aluno1.getHistorico()
    print('---------------------------------------- Histórico do Aluno ---------------------------------------- ')
    print('Aluno: {} - Matricula: {}'.format(historico1.getAluno().getNome(), historico1.getAluno().getNroMatric()))
    print('Disciplinas Obrigatótias: ')
    for discObr in historico1.getDiscObrigatorias():
        print(' {} - {} - Carga Horária: {}h'.format(discObr.getCodigo(), discObr.getNome(), discObr.getCargaHoraria()))
    print()
    print('Disciplinas Eletivas: ')
    for discEle in historico1.getDiscEletivas():
        print(' {} - {} - Carga Horária: {}h'.format(discEle.getCodigo(), discEle.getNome(), discEle.getCargaHoraria()))


