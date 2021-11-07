import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os.path
import pickle

class CupomFiscal():
    def __init__(self, nroCupom):
        
        self.__nroCupom = nroCupom
        self.__itensCupom = []

    def getNroCupom(self):
        return self.__nroCupom

    def getItensCupom(self):
        return self.__itensCupom

    def addItensCupom(self, item):
        self.__itensCupom.append(item)


class LimiteCriaCupom(tk.Toplevel):
    def __init__(self, controle, listaCupons):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Cupom Fiscal")
        self.controle = controle

        self.frameCupom = tk.Frame(self)
        self.frameItem = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCupom.pack()
        self.frameItem.pack()
        self.frameButton.pack()
      
        self.labelCupom = tk.Label(self.frameCupom,text="Nro Cupom: ")
        self.labelCupom.pack(side="left")  
        self.inputCupom = tk.Entry(self.frameCupom, width=20)
        self.inputCupom.pack(side="left")             

        self.labelItem = tk.Label(self.frameItem,text="Produto: ")
        self.labelItem.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameItem, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCupons

        self.buttonAdd = tk.Button(self.frameButton, text="Add Produto")      
        self.buttonAdd.pack(side="left")
        self.buttonAdd.bind("<Button>", controle.addProduto)

        self.buttonFecha = tk.Button(self.frameButton, text="Fechar Cupom")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fecharCupom)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultarCupom():
    def __init__(self, str):
        messagebox.showinfo('Produto', str)

class CtrlCupom():
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal

        if not os.path.isfile("cupom.pickle"):
            self.listaCupons = []
        else:
            with open("cupom.pickle", "rb") as f:
                self.listaCupons = pickle.load(f)
        
        self.listaProds = []

    def salvaCupons(self):
        if len(self.listaCupons) != 0:
            with open("cupom.pickle","wb") as f:
                pickle.dump(self.listaCupons, f)

    def criaCupom(self):
        listaCupons = self.ctrlPrincipal.ctrlProduto.getCodigoProdutos()
        self.limiteCria = LimiteCriaCupom(self, listaCupons)

    def addProduto(self, event):
        codigo = self.limiteCria.escolhaCombo.get()
        produto = self.ctrlPrincipal.ctrlProduto.getProduto(codigo)
        
        self.listaProds.append(produto)
        
        self.limiteCria.mostraJanela('Sucesso', 'Produto adicionado com sucesso')

    def fecharCupom(self, event):
        nro = self.limiteCria.inputCupom.get()
        cupom = CupomFiscal(nro)

        for prods in self.listaProds:
            cupom.addItensCupom(prods)
            
        self.listaCupons.append(cupom)
        self.limiteCria.mostraJanela('Sucesso', 'Cupom criado com sucesso')
        self.limiteCria.destroy()
        
    def consultarCupom(self, nro):
        res = "-----" + nro + "-----\n\n" 
        total = 0
        for cupom in self.listaCupons:
            if cupom.getNroCupom() == nro:
                for item in cupom.getItensCupom():
                    res += 'Código: '+ item.getCodigo() + '\nDescrição: ' + item.getDescricao() + '\nValor: R$' + item.getValorUnitario() + '\n\n'
                    total += int(item.getValorUnitario())
                res += '\nValor total: R$' + str(total) 
            break
        else: res = '--- Cupom não cadastrado ---'
        self.limiteIns = LimiteConsultarCupom(res)

 

