import tkinter as tk
from tkinter import simpledialog, messagebox
import album as ab
import os.path
import pickle

class Artista():
    def __init__(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

class LimiteCadastraArtista(tk.Toplevel):
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

class LimiteConsultaArtista():
    def __init__(self):
        self.answer = simpledialog.askstring('Consultar Artistas', 'Digite o Nome: ')
      
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ControleArtista():
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal
        self.listaArt = []

        if not os.path.isfile("artista.pickle"):
            self.listaArt =  []
        else:
            with open("artista.pickle", "rb") as f:
                self.listaArt = pickle.load(f)
    
    def salvaArtistas(self):
        if len(self.listaArt) != 0:
            with open("artista.pickle","wb") as f:
                pickle.dump(self.listaArt, f)
  
    def cadastrarArtista(self):
        self.limiteCad = LimiteCadastraArtista(self)

    def enterHandler(self, event):
        nome = self.limiteCad.inputNome.get()
        artista = Artista(nome)
        self.listaArt.append(artista)
        messagebox.showinfo('Cadastro', 'Artista cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteCad.inputNome.delete(0, len(self.limiteCad.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteCad.destroy()

    def consultarArtista(self):
        consultaArt = LimiteConsultaArtista()
        answer = consultaArt.answer
        album = []
        album = self.ctrlPrincipal.ctrlAlbum.getAlbum(str(answer))

        for artista in self.listaArt:
            self.msg = 'Artista: '
            if answer == str(artista.getNome()):
                self.msg += artista.getNome() 
    
                for alb in album:
                    self.msg += '\nÁlbum: ' + alb.getNome() 
                    self.msg += '\nMúsicas:'
                    for mus in alb.getFaixas():
                        music = ab.Musica(mus)
                        self.msg += '\n' + mus.getTitulo()
                consultaArt.mostraJanela('Busca', self.msg)
                break
        else:
            self.msg = 'Artista não cadastrado'
            consultaArt.mostraJanela('Busca', self.msg)

    def getListaNomeArt(self):
        listArt = []
        for art in self.listaArt:
            listArt.append(art.getNome())
        return listArt

    def getNomeMusicasArtista(self, nomeArtista):
        album = self.ctrlPrincipal.ctrlAlbum.getAlbum(str(nomeArtista))
        listaNomesMusicas = []
        for ar in self.listaArt:
            if ar.getNome() == nomeArtista:
                for alb in album:
                    for mus in alb.getFaixas():
                        music = ab.Musica(mus)
                        listaNomesMusicas.append(mus.getTitulo())
        return listaNomesMusicas   
        



        