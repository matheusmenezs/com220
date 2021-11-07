import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
import os.path
import pickle

class Album:
    def __init__(self, titulo, ano, artista):
        self.__titulo = titulo
        self.__ano = ano
        self.__artista = artista
        self.__listaMusicas = []
        
    def getTitulo(self):
        return self.__titulo

    def getAno(self):
        return self.__ano

    def getArtista(self):
        return self.__artista

    def getMusicas(self):
        return self.__listaMusicas
    
    def addFaixa(self, musica):
        self.__listaMusicas.append(musica)
    
class LimiteInsereAlbuns(tk.Toplevel):
    def __init__(self, controle, listaArtistas):

        tk.Toplevel.__init__(self)
        self.geometry('250x150')
        self.title("Álbum")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameAno.pack()
        self.frameButton.pack()
      
        self.labelTitulo = tk.Label(self.frameTitulo,text="Título: ")
        self.labelTitulo.pack(side="left") 
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")             

        self.labelArtista = tk.Label(self.frameArtista,text="Artista: ")
        self.labelArtista.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtista, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaArtistas

        self.labelAno = tk.Label(self.frameAno,text="Ano: ")
        self.labelAno.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")           

        self.buttonSubmit = tk.Button(self.frameButton ,text="Cria Álbum")      
        self.buttonSubmit.pack(side="top")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonAdd= tk.Button(self.frameButton ,text="Add Música")      
        self.buttonAdd.pack(side="left")
        self.buttonAdd.bind("<Button>", controle.inserirMusica)
        
        self.buttonFecha = tk.Button(self.frameButton ,text="Lança Álbum")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraAlbuns():
    def __init__(self, str):
        messagebox.showinfo('Lista de Álbuns', str)
     
class CtrlAlbum():
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal

        if not os.path.isfile("album.pickle"):
            self.listaAlbuns =  []
        else:
            with open("album.pickle", "rb") as f:
                self.listaAlbuns = pickle.load(f)
    
    def salvaAlbuns(self):
        if len(self.listaAlbuns) != 0:
            with open("album.pickle","wb") as f:
                pickle.dump(self.listaAlbuns, f)
    
    def getAlbunsArtista(self, artista):
        listaTituloAlbuns = []
        for al in self.listaAlbuns:
            if al.getArtista().getNome() == artista:
                listaTituloAlbuns.append(al.getTitulo())
        return listaTituloAlbuns

    def getAlbumByName(self, titAlbum):
        AlSel = None
        for al in self.listaAlbuns:
            if al.getTitulo() == titAlbum:
                AlSel = al
        return AlSel

    def insereAlbuns(self):
        listaArtistas = self.ctrlPrincipal.ctrlArtista.getListaNomesArtistas()
        self.limiteIns = LimiteInsereAlbuns(self, listaArtistas)
       
    def consultarAlbuns(self, tituloAlbum):
        res = "----" + tituloAlbum + "----\n\n"
        for al in self.listaAlbuns:
            if al.getTitulo() == tituloAlbum:
                for mu in al.getMusicas():
                    res += mu.getTitulo() + ";\n"
        self.limiteIns = LimiteMostraAlbuns(res)

    def enterHandler(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        nomeArtista = self.limiteIns.escolhaCombo.get()
        ano = self.limiteIns.inputAno.get()
        artista = self.ctrlPrincipal.ctrlArtista.getArtista(nomeArtista)
        album = Album(titulo, ano, artista)
        self.listaAlbuns.append(album)
        self.ctrlPrincipal.ctrlArtista.addAlbum(nomeArtista, album)
        self.limiteIns.mostraJanela('Sucesso', 'Álbum criado com sucesso')
        
    def inserirMusica(self, event):
        tituloMusica = simpledialog.askstring('Música', 'Título:')
        tituloAlbum = self.limiteIns.inputTitulo.get()
        nomeArt = self.limiteIns.escolhaCombo.get()
        
        album = self.ctrlPrincipal.ctrlAlbum.getAlbumByName(tituloAlbum)
        artista = self.ctrlPrincipal.ctrlArtista.getArtista(nomeArt)
        
        musica = self.ctrlPrincipal.ctrlMusica.gravaMusica(tituloMusica, artista, album)
        album.addFaixa(musica)
        artista.addMusica(musica)
        self.limiteIns.mostraJanela('Sucesso', 'Música gravada com sucesso')

    def clearHandler(self, event):
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
        self.limiteIns.escolhaCombo.set("")

    def fechaHandler(self, event):
        self.limiteIns.mostraJanela('Sucesso', 'Álbum lançado com sucesso')
        self.limiteIns.destroy()
        