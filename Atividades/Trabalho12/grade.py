import os.path
import pickle

class Grade:
    def __init__(self, ano, curso):
        self.__ano = ano
        self.__curso = curso
        self.__disciplinas = []

    def getAno(self):
        return self.__ano

    def getCurso(self):
        return self.__curso

    def getDisciplinas(self):
        return self.__disciplinas

    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

class CtrlGrade:   
    def __init__(self):
        self.listaGrades = []

        if not os.path.isfile("Grade.pickle"):
            self.listaGrades = []
        else:
            with open("Grade.pickle", "rb") as f1:
                self.listaGrades = pickle.load(f1)
    
    def salvaGrade(self):
        if len(self.listaGrades) != 0:
            with open("Grade.pickle","wb") as f1:
                pickle.dump(self.listaGrades, f1)

    def criaGrade(self, ano, curso):
        grade = Grade(ano, curso)
        self.listaGrades.append(grade)

    def insereDisciplina(self, cursoNome, disciplina):
        for grade in self.listaGrades:
            curso = grade.getCurso()
            if curso.getNome() == cursoNome:
                grade.addDisciplina(disciplina)

    def procuraDisciplina(self, nomeCurso, codigoDisciplina):
        for grade in self.listaGrades:
            curso = grade.getCurso()
            if curso.getNome() == nomeCurso:
                for disciplina in grade.getDisciplinas():
                    if disciplina.getCodigo() == codigoDisciplina:
                        return 1
        return 0

    def exibeDescricao(self, nomeCurso):
        for grade in self.listaGrades:
            curso = grade.getCurso()
            if curso.getNome() == nomeCurso:
                res = "Grade:\n ==================================\n"
                for disciplina in grade.getDisciplinas():
                    res += "Disciplina: ["
                    res += disciplina.getCodigo() + "] "
                    res += disciplina.getNome() + "\n"
                    res += "Carga Horária: "
                    res += str(disciplina.getCargaHoraria()) + "h\n"
                    res += "==================================\n"
        return res