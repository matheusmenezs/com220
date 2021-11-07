import tkinter as tk
from tkinter import ttk, messagebox
import os.path
import pickle

class Artista:
    def __init__(self, nome):
        self.__nome = nome
        self.__listaMusicas = []
        self.__listaAlbuns = []
        
    def getNome(self):
        return self.__nome

    def getMusicas(self):
        return self.__listaMusicas

    def getAlbuns(self):
        return self.__listaAlbuns

    def addMusica(self, musica):
        self.__listaMusicas.append(musica)
    
    def addAlbum(self, album):
        self.__listaAlbuns.append(album)
    
class LimiteInsereArtistas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")  

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
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

class LimiteMostraArtistas():
    def __init__(self, str):
        messagebox.showinfo('Lista de Artistas', str)

class CtrlArtista():
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal
        
        if not os.path.isfile("artista.pickle"):
            self.listaArtistas = []
        else:
            with open("artista.pickle", "rb") as f:
                self.listaArtistas = pickle.load(f)
    
    def salvaArtistas(self):
        if len(self.listaArtistas) != 0:
            with open("artista.pickle","wb") as f:
                pickle.dump(self.listaArtistas, f)
    
    def getArtista(self, nomeArtista):
        arSel = None
        for a in self.listaArtistas:
            if(a.getNome() == nomeArtista):
                arSel = a
        return arSel

    def getListaNomesArtistas(self):
        listaNomes = []
        for ar in self.listaArtistas:
            listaNomes.append(ar.getNome())
        return listaNomes

    def getNomeMusicasArtista(self, nomeArtista):
        listaNomesMusicas = []
        for ar in self.listaArtistas:
            if ar.getNome() == nomeArtista:
                for mu in ar.getMusicas():
                    listaNomesMusicas.append(mu.getTitulo())
        return listaNomesMusicas

    def addAlbum(self, nomeArtista, album):
        for ar in self.listaArtistas:
            if ar.getNome() == nomeArtista:
                ar.addAlbum(album)

    def insereArtistas(self):
        self.limiteIns = LimiteInsereArtistas(self)
    
    def consultarArtista(self, nomeArtista):
        res = "---" + nomeArtista + "-----\n\n" 
        for a in self.listaArtistas:
            if a.getNome() == nomeArtista:
                for al in a.getAlbuns():
                    res += al.getTitulo() + ':\n\n'
                    for mu in al.getMusicas():
                        res += mu.getTitulo() + ';\n'
                    res += '---------------------\n'
                break
        else: res = '--- Artista não cadastrado ---'
        self.limiteIns = LimiteMostraArtistas(res)

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        artista = Artista(nome)
        self.listaArtistas.append(artista)
        self.limiteIns.mostraJanela('Sucesso', 'Artista cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
