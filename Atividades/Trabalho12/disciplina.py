import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Disciplina:

    def __init__(self, codigo, nome, cargaHoraria, curso):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        self.__curso = curso

    def getCodigo(self):
        return self.__codigo
    def getNome(self):
        return self.__nome
    def getCargaHoraria(self):
        return self.__cargaHoraria
    def getCurso(self):
        return self.__curso

class LimiteInsereDisciplinas(tk.Toplevel):
    def __init__(self, controle, listaCodCursos):
        
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Disciplina")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameCargaHoraria = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameCargaHoraria.pack()
        self.frameCurso.pack()
        self.frameButton.pack()

        self.labelCursos = tk.Label(self.frameCurso,text="Código do curso: ")
        self.labelCursos.pack(side="top")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameCurso, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="top")
        self.combobox['values'] = listaCodCursos

        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelCargaHoraria = tk.Label(self.frameCargaHoraria, text="Carga Horária: ")
        self.labelCodigo.pack(side="top")
        self.labelNome.pack(side="top")
        self.labelCargaHoraria.pack(side="top")  

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="top")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="top")

        self.inputCargaHoraria = tk.Entry(self.frameCargaHoraria, width=20)
        self.inputCargaHoraria.pack(side="top")

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

class LimiteMostraDisciplinas():
    def __init__(self, str):
        messagebox.showinfo('Lista de disciplinas', str)

      
class CtrlDisciplina():       
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal
        
        if not os.path.isfile("Disciplina.pickle"):
            disciplina1 = Disciplina('COM112', 'Alg. Est. Dados 2', 64, 'SIN')
            disciplina2 = Disciplina('MAT011', 'Álgebra Linear', 64, 'CCO')
            disciplina3 = Disciplina('ELE101', 'Introdução a Engenharia Elétrica', 48, 'ENG')
        
            self.ctrlPrincipal.ctrlCurso.addDisciplina('SIN', disciplina1)
            self.ctrlPrincipal.ctrlCurso.addDisciplina('CCO', disciplina2)
            self.ctrlPrincipal.ctrlCurso.addDisciplina('ENG', disciplina3)
            
            self.listaDisciplinas =  [disciplina1, disciplina2, disciplina3]
        else:
            with open("Disciplina.pickle", "rb") as f:
                self.listaDisciplinas = pickle.load(f)

    def salvaDisciplinas(self):
        if len(self.listaDisciplinas) != 0:
            with open("disciplina.pickle","wb") as f:
                pickle.dump(self.listaDisciplinas, f)

    def getListaDisciplinas(self):
        return self.listaDisciplinas

    def getNomeDisciplinaCod(self, codDisc):
        discRet = None
        for disc in self.listaDisciplinas:
            if disc.getCodigo() == codDisc:
                discRet = disc
        return discRet

    def getListaCodDisciplinas(self):
        listaCod = []
        for disc in self.listaDisciplinas:
            listaCod.append(disc.getCodigo())
        return listaCod

    def insereDisciplinas(self):
        listaCodCursos = self.ctrlPrincipal.ctrlCurso.getListaNomeCursos()
        self.limiteIns = LimiteInsereDisciplinas(self, listaCodCursos) 

    def mostraDisciplinas(self):
        str = 'Código -- Nome\n'
        for disc in self.listaDisciplinas:
            str += disc.getCodigo() + ' -- ' + disc.getNome() + '\n'
        self.limiteLista = LimiteMostraDisciplinas(str)

    def enterHandler(self, event):
        cursoSel = self.limiteIns.escolhaCombo.get()
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        cargaHoraria = self.limiteIns.inputCargaHoraria.get()

        disciplina = Disciplina(codigo, nome, cargaHoraria, cursoSel)
        self.listaDisciplinas.append(disciplina)
        self.limiteIns.mostraJanela('Sucesso', 'Disciplina cadastrada com sucesso')
        
        self.ctrlPrincipal.ctrlCurso.addDisciplina(cursoSel, disciplina)
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.escolhaCombo.set(" ")
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputCargaHoraria.delete(0, len(self.limiteIns.inputCargaHoraria.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    