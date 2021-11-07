import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class Cliente():
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
    
    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email



class View():
    def __init__(self, janelaPrincipal, controller):
        
        self.controller = controller
        self.janela = tk.Frame(janelaPrincipal)
        self.janela.pack()

        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
    
        self.frame1.pack()
        self.frame2.pack()

        self.label1 = tk.Label(self.frame1, text = 'Nome:')
        self.label2 = tk.Label(self.frame2, text = 'E-mail:')

        self.label1.pack(side = 'left')
        self.label2.pack(side = 'left')

        self.entry1 = tk.Entry(self.frame1)
        self.entry2 = tk.Entry(self.frame2)

        self.entry1.pack()
        self.entry2.pack()

        self.buttom1 = tk.Button(self.janela, text = 'consultar', command=controller.consultar)
        self.buttom1.pack(side = 'left')



       
class Controller():
    def __init__(self):
        self.root = tk.Tk()   #Cria janela principal
        self.root.geometry('300x100')
        self.listaClientes = []

        self.view = View(self.root, self)  #self.root: Janela principal para view /   self: passa uma instancia do controller para View.

        self.root.mainloop()

    def consultar(self):
        answer = simpledialog.askstring("Código", "Digite o código:")
        



if __name__ == '__main__':
    c = Controller()
