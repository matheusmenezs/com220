import tkinter as tk
from tkinter import messagebox, simpledialog
import os.path
import pickle

class Produto():
    def __init__(self, codigo, descricao, valorUnitario):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorUnitario = valorUnitario
    
    def getCodigo(self): #Identifica cada produto
        return self.__codigo

    def getDescricao(self): #Descreve cada produto
        return self.__descricao

    def getValorUnitario(self): #Preço de cada produto 
        return self.__valorUnitario

class LimiteCadastraProduto(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Produto")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.frameValor = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameDescricao.pack()
        self.frameValor.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelCodigo.pack(side="left")  
        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")             

        self.labelDescricao = tk.Label(self.frameDescricao,text="Descrição: ")
        self.labelDescricao.pack(side="left")  
        self.inputDescricao = tk.Entry(self.frameDescricao, width=20)
        self.inputDescricao.pack(side="left")

        self.labelValor = tk.Label(self.frameValor,text="Valor: ")
        self.labelValor.pack(side="left")  
        self.inputValor = tk.Entry(self.frameValor, width=20)
        self.inputValor.pack(side="left")
    
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

class LimiteMostraProdutos():
    def __init__(self, str):
        messagebox.showinfo('Produto', str)

class CtrlProduto():
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal

        if not os.path.isfile("produto.pickle"):
            self.listaProdutos = []
        else:
            with open("pruduto.pickle", "rb") as f:
                self.listaPrudutos = pickle.load(f)
    
    def salvaProdutos(self):
        if len(self.listaProdutos) != 0:
            with open("pruduto.pickle","wb") as f:
                pickle.dump(self.listaProdutos, f)
        
    def cadastrarProduto(self):
        self.limiteCad = LimiteCadastraProduto(self)

    def enterHandler(self, event):
        codigo = self.limiteCad.inputCodigo.get()
        descricao = self.limiteCad.inputDescricao.get()
        valor = self.limiteCad.inputValor.get()
        
        produto = Produto(codigo, descricao, valor)
        self.listaProdutos.append(produto)
        self.limiteCad.mostraJanela('Sucesso', 'Produto cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteCad.inputCodigo.delete(0, len(self.limiteCad.inputCodigo.get()))
        self.limiteCad.inputDescricao.delete(0, len(self.limiteCad.inputDescricao.get()))
        self.limiteCad.inputValor.delete(0, len(self.limiteCad.inputValor.get()))

    def fechaHandler(self, event):
        self.limiteCad.destroy()

    def consultarProduto(self, codigo):
        res = "-----" + codigo + "-----\n\n" 
        for prod in self.listaProdutos:
            if prod.getCodigo() == codigo:
                res += 'Descrição: ' + prod.getDescricao() + '\nValor: R$' + prod.getValorUnitario() 
                break
        else: res = '--- Produto não cadastrado ---'
        self.limiteIns = LimiteMostraProdutos(res)

    def getCodigoProdutos(self):
        listaCodigos = []
        for cod in self.listaProdutos:
            listaCodigos.append(cod.getCodigo())
        return listaCodigos

    def getProduto(self, codigo):
        codSel = None
        for cod in self.listaProdutos:
            if (cod.getCodigo() == codigo):
                codSel = cod
        return codSel

