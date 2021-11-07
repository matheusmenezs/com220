import tkinter as tk
from tkinter import simpledialog
import cupom as cup
import produto as pro

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)    

        self.produtoMenu = tk.Menu(self.menubar)
        self.cupomMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)    

        self.produtoMenu.add_command(label="Cadastrar", \
                    command=self.controle.cadastrarProduto)
        self.produtoMenu.add_command(label="Consultar", \
                    command=self.controle.consultarProduto)
        self.menubar.add_cascade(label="Produto", \
                    menu=self.produtoMenu)

        self.cupomMenu.add_command(label="Criar", \
                    command=self.controle.criaCupom)
        self.cupomMenu.add_command(label="Consultar", \
                    command=self.controle.consultarCupom)       
        self.menubar.add_cascade(label="Cupom Fiscal", \
                    menu=self.cupomMenu)

        self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProduto = pro.CtrlProduto(self)
        self.ctrlCupom = cup.CtrlCupom(self)

        self.limite = LimitePrincipal(self.root, self) 
        self.root.title("Sistema")
        self.root.mainloop()
       
    def cadastrarProduto(self):
        self.ctrlProduto.cadastrarProduto()
    
    def consultarProduto(self):
        codigoProduto = simpledialog.askstring("Input", "Código do Produto: ",
                                 parent=self.root)
        self.ctrlProduto.consultarProduto(codigoProduto)

    def criaCupom(self):
        self.ctrlCupom.criaCupom()

    def consultarCupom(self):
        nroCupom = simpledialog.askstring("Input", "Nro do Cupom: ",
                                 parent=self.root)
        self.ctrlCupom.consultarCupom(nroCupom)

    def salvaDados(self):
        self.ctrlProduto.salvaProdutos()
        self.ctrlCupom.salvaCupons()
        self.root.destroy()
        
if __name__ == '__main__':
    c = ControlePrincipal()