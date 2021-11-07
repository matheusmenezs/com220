import tkinter as tk
from tkinter import messagebox, simpledialog
import aluno as al
import disciplina as disc
import curso as cur
import historico as his
import grade as gra


class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.alunoMenu = tk.Menu(self.menubar)
        self.discipMenu = tk.Menu(self.menubar)
        self.cursoMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)    

        self.alunoMenu.add_command(label="Inserir Aluno", \
                    command=self.controle.insereAlunos)
        self.alunoMenu.add_command(label="Cadastrar Disciplina Cursada", \
                    command=self.controle.cadastrarDisciplinas)
        self.alunoMenu.add_command(label="Consultar Histórico", \
                    command=self.controle.consultarHistorico)
        self.menubar.add_cascade(label="Aluno", \
                    menu=self.alunoMenu)

        self.discipMenu.add_command(label="Insere", \
                    command=self.controle.insereDisciplinas)      
        self.menubar.add_cascade(label="Disciplina", \
                    menu=self.discipMenu)

        self.cursoMenu.add_command(label="Insere", \
                    command=self.controle.insereCursos)
        self.cursoMenu.add_command(label="Consultar Grade", \
                    command=self.controle.consultarCursos)                        
        self.menubar.add_cascade(label="Curso", \
                    menu=self.cursoMenu)        

        self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlHistorico = his.CtrlHistorico(self)
        self.ctrlAluno = al.CtrlAluno(self)
        self.ctrlGrade = gra.CtrlGrade()
        self.ctrlCurso = cur.CtrlCurso(self)
        self.ctrlDisciplina = disc.CtrlDisciplina(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Sistema acadêmico")
        self.root.mainloop()
       
    def insereAlunos(self):
        self.ctrlAluno.insereAlunos()
    def cadastrarDisciplinas(self):
        self.ctrlAluno.cadastrarDisciplina()
    def consultarHistorico(self):
        matAluno = simpledialog.askstring("Input", "Matricula: ",
                                parent=self.root)
        self.ctrlAluno.consultarHistorico(matAluno)

    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas()

    def insereCursos(self):
        self.ctrlCurso.insereCursos()
    def consultarCursos(self):
        nomeCurso = simpledialog.askstring("Input", "Nome do curso: ",
                                parent=self.root)
        self.ctrlCurso.consultarCurso(nomeCurso)
    
    def salvaDados(self):
        self.ctrlHistorico.salvaHistorico()
        self.ctrlAluno.salvaAlunos()
        self.ctrlGrade.salvaGrade()
        self.ctrlCurso.salvaCursos()
        self.ctrlDisciplina.salvaDisciplinas()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()