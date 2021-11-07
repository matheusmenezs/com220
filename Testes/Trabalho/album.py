import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import os.path
import pickle

class Album():
    def __init__(self, nome, artista, ano, faixas):
        self.__nome = nome
        self.__artista = artista 
        self.__ano = ano
        self.__faixas = faixas
        
    def getNome(self):
        return self.__nome

    def getArtista(self):
        return self.__artista

    def getAno(self):
        return self.__ano

    def getFaixas(self):
        return self.__faixas
    
class Musica:
    def __init__(self, titulo):
        self.__titulo = titulo

    def getTitulo(self):
        return self.__titulo

class LimiteCadastraAlbum(tk.Toplevel):
    def __init__(self, controle, lista):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Album")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameNome.pack()
        self.frameAno.pack()
        self.frameArtista.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Titulo:")
        self.labelNome.pack(side="left")  

        self.labelAno = tk.Label(self.frameAno, text="Ano:")
        self.labelAno.pack(side='left')

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")          

        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")       

        self.buttonSubmit = tk.Button(self.frameButton ,text="Inserir Música")      
        self.buttonSubmit.pack(side="top")
        self.buttonSubmit.bind("<Button>", controle.inserirFaixas)
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)
            
        self.labelArt = tk.Label(self.frameArtista,text="Escolha o artista: ")
        self.labelArt.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtista, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = lista

class LimiteConsultaAlbum():
    def __init__(self):
        self.answer = simpledialog.askstring('Consultar Album', 'Digite o Titulo: ')
      
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ControleAlbum():
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal

        if not os.path.isfile("album.pickle"):
            self.listaAlb =  []
        else:
            with open("album.pickle", "rb") as f:
                self.listaAlb = pickle.load(f)
    
    def salvaAlbuns(self):
        if len(self.listaAlb) != 0:
            with open("album.pickle","wb") as f:
                pickle.dump(self.listaAlb, f)
        
    def cadastrarAlbum(self):
        listaArt = self.ctrlPrincipal.ctrlArtista.getListaNomeArt()
        
        self.limiteCad = LimiteCadastraAlbum(self, listaArt)
        self.listaFaixas = []
        self.nroFaixas = 0
    
    def enterHandler(self, event):
        titulo = self.limiteCad.inputNome.get()
        nomeArt = self.limiteCad.escolhaCombo.get()
        ano = self.limiteCad.inputAno.get()
       
        album = Album(titulo, nomeArt, ano, self.listaFaixas)
        self.listaAlb.append(album)
        messagebox.showinfo('Cadastro', 'Album cadastrado com sucesso')
        self.clearHandler(event)

    def inserirFaixas(self, event):
        faixa = simpledialog.askstring('Inserir Músicas', 'Digite o Nome: ')
        music = Musica(faixa)
        self.listaFaixas.append(music)

    def clearHandler(self, event):
        self.limiteCad.inputNome.delete(0, len(self.limiteCad.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteCad.destroy()

    def consultarAlbum(self):
        consultaAlb = LimiteConsultaAlbum()
        answer = consultaAlb.answer

        for album in self.listaAlb:
            self.msg = 'Album: '
            if answer == str(album.getNome()):
                self.msg += album.getNome() + '\n'
                self.msg += '\nMúsicas:'
                for faixas in album.getFaixas():
                    self.msg +='\n' + faixas.getTitulo()
              
                consultaAlb.mostraJanela('Busca', self.msg)
                break
        else:
            self.msg = 'Album não cadastrado'
            consultaAlb.mostraJanela('Busca', self.msg)

    def getAlbum(self, nomeArt):
        albRet = []
        for alb in self.listaAlb:
            if alb.getArtista() == nomeArt:
                albRet.append(alb)
        return albRet



  


    


        


