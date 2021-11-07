import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Playlist:
    def __init__(self, nome, musicas):
        self.__nome = nome
        self.__musicas = musicas

    def getNome(self):
        return self.__nome

    def getMusicas(self):
        return self.__musicas

class LimiteInserePlaylist(tk.Toplevel):
    def __init__(self, controle, listaNomeArtistas, listaTituloMusicas):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Playlist")
        self.controle = controle

        self.frameNomePlaylist = tk.Frame(self)
        self.frameNomeArtista = tk.Frame(self)
        self.frameMusicas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNomePlaylist.pack()
        self.frameNomeArtista.pack()
        self.frameMusicas.pack()        
        self.frameButton.pack()

        self.labelNomePlaylist = tk.Label(self.frameNomePlaylist,text="Nome da Playlist: ")
        self.labelNomePlaylist.pack(side="left")
        self.inputNomePlaylist = tk.Entry(self.frameNomePlaylist, width=20)
        self.inputNomePlaylist.pack(side="left")

        self.labelNomeArtista = tk.Label(self.frameNomeArtista,text="Escolha o artista: ")
        self.labelNomeArtista.pack(side="left")
        self.escolhaNomeArtista = tk.StringVar()
        self.comboboxArtista = ttk.Combobox(self.frameNomeArtista, width = 15 , textvariable = self.escolhaNomeArtista)
        self.comboboxArtista.pack(side="left")
        self.comboboxArtista['values'] = listaNomeArtistas
          
        self.labelMusicas = tk.Label(self.frameMusicas,text="Escolha: ")
        self.labelMusicas.pack(side="left") 
        self.listbox = tk.Listbox(self.frameMusicas)
        self.listbox.pack(side="left")

        self.buttonBusca = tk.Button(self.frameButton ,text="Buscar Musicas Artista")           
        self.buttonBusca.pack(side="left")
        self.buttonBusca.bind("<Button>", controle.buscaMusicasArtista)

        self.buttonInsere = tk.Button(self.frameButton ,text="Add Musica")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereMusica)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Playlist")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaPlaylist)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraPlaylist():
    def __init__(self, str):
        messagebox.showinfo('Lista de turmas', str)

class CtrlPlaylist():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        
        self.listaMusicasPlaylist = []
        self.listaMusicasArtista = []
        if not os.path.isfile("playlist.pickle"):
            self.listaPlaylists =  []
        else:
            with open("playlist.pickle", "rb") as f1:
                self.listaPlaylists = pickle.load(f1)

    def salvaPlaylists(self):
        if len(self.listaPlaylists) != 0:
            with open("playlist.pickle","wb") as f1:
                pickle.dump(self.listaPlaylists, f1)
    
    def consultarPlaylists(self, nomePlaylist):
        res = ""
        for play in self.listaPlaylists:
            if play.getNome() == nomePlaylist:
                res = "----Playlist " + nomePlaylist + "-----\n" 
                res += "Musicas:\n\n"
                for mu in play.getMusicas():
                    res += mu.getTitulo() + ";\n"
        if res == "":
            res = 'Playlist inexistente'
        self.limiteIns = LimiteMostraPlaylist(res)

    def inserePlaylists(self):        
        self.listaMusicasPlaylist = []
        listaNomeArtistas = self.ctrlPrincipal.ctrlArtista.getListaNomesArtistas()
        self.listaMusicasArtista = []
        self.limiteIns = LimiteInserePlaylist(self, listaNomeArtistas, self.listaMusicasArtista)

    def buscaMusicasArtista(self, event):
        artSel = self.limiteIns.escolhaNomeArtista.get()
        listaNomeMusicasArt = self.ctrlPrincipal.ctrlArtista.getNomeMusicasArtista(artSel)
        for mu in listaNomeMusicasArt:
            self.limiteIns.listbox.insert(tk.END, mu)

    def insereMusica(self, event):
        musicaSel = self.limiteIns.listbox.get(tk.ACTIVE)
        musica = self.ctrlPrincipal.ctrlMusica.getMusica(musicaSel)
        self.listaMusicasPlaylist.append(musica)
        self.limiteIns.mostraJanela('Sucesso', 'Musica adicionada')
        self.limiteIns.listbox.delete(tk.ACTIVE)
        
    def criaPlaylist(self, event):
        nome = self.limiteIns.inputNomePlaylist.get()
        playlist = Playlist(nome, self.listaMusicasPlaylist)
        self.listaPlaylists.append(playlist)
        self.limiteIns.mostraJanela('Sucesso', 'Playlist criada com sucesso')
        self.limiteIns.destroy()
    