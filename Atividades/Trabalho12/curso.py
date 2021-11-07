import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.constants import E
import os.path
import pickle

class Curso:
    def __init__(self, nome):
        self.__nome = nome
        self.__alunos = []

    def getNome(self):
        return self.__nome

    def getAlunos(self):
        return self.__alunos

class LimiteInsereCurso(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Disciplina")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameAno.pack()
        self.frameButton.pack()        

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelAno = tk.Label(self.frameAno, text="Ano da grade: ")
        self.labelNome.pack(side="left")
        self.labelAno.pack(side="left")
        
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraCursos():
    def __init__(self, str):
        messagebox.showinfo('Lista de Cursos', str)

class CtrlCurso():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        
        if not os.path.isfile("Curso.pickle"):
            self.listaCursos =  [
                Curso('SIN'),
                Curso('CCO'),
                Curso('EEL')
            ]
            self.ctrlPrincipal.ctrlGrade.criaGrade(2013, self.listaCursos[0])
            self.ctrlPrincipal.ctrlGrade.criaGrade(2010, self.listaCursos[1])
            self.ctrlPrincipal.ctrlGrade.criaGrade(2012, self.listaCursos[2])
        else:
            with open("Curso.pickle", "rb") as f1:
                self.listaCursos = pickle.load(f1)
    
    def salvaCursos(self):
        if len(self.listaCursos) != 0:
            with open("Curso.pickle","wb") as f1:
                pickle.dump(self.listaCursos, f1)

    def getListaCursos(self):
        return self.listaCursos

    def getListaNomeCursos(self):
        listaNome = []
        for cur in self.listaCursos:
            listaNome.append(cur.getNome())
        return listaNome

    def insereCursos(self):
        self.limiteIns = LimiteInsereCurso(self)

    def addDisciplina(self, cursoNome, disciplina):
        self.ctrlPrincipal.ctrlGrade.insereDisciplina(cursoNome, disciplina)
    
    def consultarCurso(self, nomeCurso):
        str = ""
        for curso in self.listaCursos:
            if curso.getNome() == nomeCurso:
                str = self.ctrlPrincipal.ctrlGrade.exibeDescricao(nomeCurso)

        self.limiteIns = LimiteMostraCursos(str)

    def enterHandler(self, event):
        nomeCurso = self.limiteIns.inputNome.get()
        ano = self.limiteIns.inputAno.get()
        
        curso = Curso(nomeCurso)
        self.ctrlPrincipal.ctrlGrade.criaGrade(ano, curso)
        
        self.listaCursos.append(curso)
        self.limiteIns.mostraJanela('Sucesso', 'Curso criada com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def insereAluno(self, event):
        alunoSel = self.limiteIns.listbox.get(tk.ACTIVE)
        aluno = self.ctrlPrincipal.ctrlAluno.getAluno(alunoSel)
        self.listaAlunosCurso.append(aluno)
        self.limiteIns.mostraJanela('Sucesso', 'Aluno matriculado')
        self.limiteIns.listbox.delete(tk.ACTIVE)
        
    def mostraCursos(self):
        str = ''
        for curso in self.listaCursos:
            str += 'Código: ' + curso.getCodigo() + '\n'
            str += 'Disciplina: ' + curso.getDisciplina().getCodigo() + '\n'
            str += 'Estudantes:\n'
            for estud in curso.getAlunos():
                str += estud.getNroMatric() + ' - ' + estud.getNome() + '\n'
            str += '------\n'

        self.limiteLista = LimiteMostraCursos(str)
    