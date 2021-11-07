import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Aluno:
    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso

    def getNroMatric(self):
        return self.__nroMatric

    def getNome(self):
        return self.__nome
    
    def getCurso(self):
        return self.__curso


class LimiteInsereAlunos(tk.Toplevel):
    def __init__(self, controle, listaNomeCursos):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Alunos")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameCurso.pack()
        self.frameButton.pack()
        
        self.labelNro = tk.Label(self.frameNro,text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")  

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             

        self.labelAluno = tk.Label(self.frameCurso,text="Curso: ")
        self.labelAluno.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameCurso, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNomeCursos

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

class LimiteCadastraDisciplina(tk.Toplevel):
    def __init__(self, controle, listaCodDiscip, listaNroMatric):
        
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Disciplina")
        self.controle = controle

        self.frameAluno = tk.Frame(self)
        self.frameDisciplina = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameSemestre = tk.Frame(self)
        self.frameNota = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameAluno.pack()
        self.frameDisciplina.pack()
        self.frameAno.pack()
        self.frameSemestre.pack() 
        self.frameNota.pack()       
        self.frameButton.pack()

        self.labelAluno = tk.Label(self.frameAluno,text="Aluno: ")
        self.labelAluno.pack(side="top")
        self.escolhaCombo2 = tk.StringVar()
        self.combobox2 = ttk.Combobox(self.frameAluno, width = 15 , textvariable = self.escolhaCombo2)
        self.combobox2.pack(side="top")
        self.combobox2['values'] = listaNroMatric
          
        self.labelEst = tk.Label(self.frameDisciplina,text="Escolha a disciplina: ")
        self.labelEst.pack(side="top")
        self.escolhaCombo3 = tk.StringVar()
        self.combobox3 = ttk.Combobox(self.frameDisciplina, width = 15, textvariable = self.escolhaCombo3)
        self.combobox3.pack(side="top")
        self.combobox3['values'] = listaCodDiscip

        self.labelAno = tk.Label(self.frameAno, text="Ano: ")
        self.labelSemestre = tk.Label(self.frameSemestre, text="Semestre [1 ou 2]: ")
        self.labelNota = tk.Label(self.frameNota, text="Nota: ")
        self.labelAno.pack(side="top")
        self.labelSemestre.pack(side="top")
        self.labelNota.pack(side="top")

        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="top")
        self.inputSemestre = tk.Entry(self.frameSemestre, width=20)
        self.inputSemestre.pack(side="left") 
        self.inputNota = tk.Entry(self.frameNota, width=20)
        self.inputNota.pack(side="left") 

        self.buttonInsere2 = tk.Button(self.frameButton ,text="Inserir Disciplina")           
        self.buttonInsere2.pack(side="left")
        self.buttonInsere2.bind("<Button>", controle.insereDisciplina)  

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)  

class LimiteMostraAluno():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)
     
class CtrlAluno():
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal

        if not os.path.isfile("Aluno.pickle"):
            aluno = Aluno(1, 'João', 'SIN')
            self.ctrlPrincipal.ctrlHistorico.criaHistorico(aluno)
            self.listaAlunos =  [aluno]
        else:
            with open("Aluno.pickle", "rb") as f:
                self.listaAlunos = pickle.load(f)

    def salvaAlunos(self):
        if len(self.listaAlunos) != 0:
            with open("Aluno.pickle","wb") as f:
                pickle.dump(self.listaAlunos, f)

    def getAluno(self, nroMatric):
        alRet = None
        for al in self.listaAlunos:
            if al.getNroMatric() == nroMatric:
                alRet = al[0]
        return alRet

    def getListaNroMatric(self):
        listaNro = []
        for al in self.listaAlunos:
            listaNro.append(al.getNroMatric())
        return listaNro

    def insereAlunos(self):
        listaCursos = self.ctrlPrincipal.ctrlCurso.getListaNomeCursos()
        self.limiteIns = LimiteInsereAlunos(self, listaCursos) 

    def cadastrarDisciplina(self):
        listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        self.listaNroMatric = self.getListaNroMatric()
        self.limiteIns = LimiteCadastraDisciplina(self, listaCodDisc, self.listaNroMatric)

    def insereDisciplina(self, event):
        matAluno = self.limiteIns.escolhaCombo2.get()
        codDisciplina = self.limiteIns.escolhaCombo3.get()
        ano = self.limiteIns.inputAno.get()
        semestre = self.limiteIns.inputSemestre.get()
        nota = self.limiteIns.inputNota.get()
        
        self.ctrlPrincipal.ctrlHistorico.addRegistro(matAluno, codDisciplina, ano, semestre, nota)
        self.limiteIns = self.fechaHandler(event)

    def consultarHistorico(self, matAluno):
        str = ""
        str = self.ctrlPrincipal.ctrlHistorico.imprimirHistorico(matAluno)
        self.limiteIns = LimiteMostraAluno(str)

    def mostraAlunos(self):
        str = 'Nro Matric. -- Nome\n'
        for est in self.listaAlunos:
            str += est.getNroMatric() + ' -- ' + est.getNome() + '\n'       
        self.limiteLista = LimiteInsereAlunos(str)

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        nomeCurso = self.limiteIns.escolhaCombo.get()
        aluno = Aluno(nroMatric, nome, nomeCurso)
        
        self.ctrlPrincipal.ctrlHistorico.criaHistorico(aluno)

        self.listaAlunos.append(aluno)
        self.limiteIns.mostraJanela('Sucesso', 'Aluno cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.escolhaCombo.set("")

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    