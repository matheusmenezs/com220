from operator import itemgetter
import os.path
import pickle

class Historico:
    def __init__(self, aluno):
        self.__aluno = aluno
        self.__disciplinas = []

    def getAluno(self):
        return self.__aluno
    def getDisciplinas(self):
        return self.__disciplinas

    def addDisciplina(self, registro):
        self.__disciplinas.append(registro)

class CtrlHistorico:
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal
        
        if not os.path.isfile("Historico.pickle"):
            self.listaHistoricos = []
        else:
            with open("Historico.pickle", "rb") as f1:
                self.listaHistoricos = pickle.load(f1)
    
    def salvaHistorico(self):
        if len(self.listaHistoricos) != 0:
            with open("Historico.pickle","wb") as f1:
                pickle.dump(self.listaHistoricos, f1)

    def criaHistorico(self, aluno):
        his = Historico(aluno)
        self.listaHistoricos.append(his)
    
    def addRegistro(self, matAluno, codDisciplina, ano, semestre, nota):
        disciplina = self.ctrlPrincipal.ctrlDisciplina.getNomeDisciplinaCod(codDisciplina)
        registro = {}
        
        registro['ano'] = ano
        registro['semestre'] = semestre
        registro['disciplina'] = disciplina
        registro['nota'] = nota
        if int(nota)>=6:
            registro['situacao'] = 'Aprovado'
        else:
            registro['situacao'] = 'Reprovado'
        
        for hist in self.listaHistoricos:
            al = hist.getAluno()
            if str(matAluno) == str(al.getNroMatric()):
                nomeCurso = al.getCurso()
                if((self.ctrlPrincipal.ctrlGrade.procuraDisciplina(nomeCurso, codDisciplina)) == 1):
                    registro['tipo'] = 'o'
                else:
                    registro['tipo'] = 'e'
                hist.addDisciplina(registro)

    def count(self, matAluno):
        cc = 0
        for his in self.listaHistoricos:
            aluno = his.getAluno()
            if aluno.getNroMatric() == matAluno:
                cc += 1

    def imprimirHistorico(self, matAluno):
        qtdDis = self.count(matAluno)
        res = ""
        o = 0
        e = 0
        auxAno = 0
        auxSem = 0
        for his in self.listaHistoricos:
            aluno = his.getAluno()
            if str(aluno.getNroMatric()) == str(matAluno):
                discips = his.getDisciplinas()
                discips.sort(key=itemgetter('ano', 'semestre'))
                for dis in discips:
                    if(dis['ano'] != auxAno or dis['semestre'] != auxSem):
                        res+= "-------------------------------\n"
                        res += "Ano/Semestre: " + dis['ano']
                        res += "/" + dis['semestre'] 
                        res+= "\n-------------------------------\n"
                    res += "Disciplina: " + dis['disciplina'].getNome() + "\n"
                    res += "Nota: " + str(dis['nota']) + "\n"
                    res += "Situação: " + dis['situacao'] + "\n\n"

                    ch = str(dis['disciplina'].getCargaHoraria())

                    for i in range (2,len(ch)):
                        ch = ch.replace(ch[i], '')

                    if(dis['tipo'] == 'e'):
                        e+= int(ch)
                    elif(dis['tipo'] == 'o'):
                        o+= int(ch)

                    auxAno = dis['ano']
                    auxSem= dis['semestre']
        res += "\nCarga Horária obrigatória: " + str(o) + "h\n"
        res += "Carga Horária eletiva: " + str(e) + "h\n"
        return res 