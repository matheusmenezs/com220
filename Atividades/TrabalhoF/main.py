import tkinter as tk
from tkinter import messagebox, simpledialog
import artista as ar
import album as al
import playlist as pl
import musica as mu

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x300')
        self.menubar = tk.Menu(self.root)        
        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)    

        self.artistaMenu.add_command(label="Cadastrar", \
                    command=self.controle.insereArtistas)
        self.artistaMenu.add_command(label="Consultar", \
                    command=self.controle.consultarArtista)
        self.menubar.add_cascade(label="Artista", \
                    menu=self.artistaMenu)

        self.albumMenu.add_command(label="Cadastrar", \
                    command=self.controle.insereAlbuns)
        self.albumMenu.add_command(label="Consultar", \
                    command=self.controle.consultarAlbum)       
        self.menubar.add_cascade(label="Álbum", \
                    menu=self.albumMenu)

        self.playlistMenu.add_command(label="Cadastrar", \
                    command=self.controle.inserePlaylists)
        self.playlistMenu.add_command(label="Consultar", \
                    command=self.controle.consultarPlaylist)                        
        self.menubar.add_cascade(label="Playlist", \
                    menu=self.playlistMenu)        

        self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()
        
        self.ctrlArtista = ar.CtrlArtista(self)
        self.ctrlAlbum = al.CtrlAlbum(self)
        self.ctrlPlaylist = pl.CtrlPlaylist(self)
        self.ctrlMusica = mu.CtrlMusica(self)

        self.limite = LimitePrincipal(self.root, self) 
        
        self.root.title("Sistema")
        self.root.mainloop()
       
    def insereArtistas(self):
        self.ctrlArtista.insereArtistas()

    def consultarArtista(self):
        nomeArtista = simpledialog.askstring("Input", "Nome do Artista: ",
                                 parent=self.root)
        self.ctrlArtista.consultarArtista(nomeArtista)
    
    def insereAlbuns(self):
        self.ctrlAlbum.insereAlbuns()

    def consultarAlbum(self):
        nomeAlbum = simpledialog.askstring("Input", "Nome do Album: ",
                                 parent=self.root)
        self.ctrlAlbum.consultarAlbuns(nomeAlbum)

    def inserePlaylists(self):
        self.ctrlPlaylist.inserePlaylists()

    def consultarPlaylist(self):
        nomePlaylist = simpledialog.askstring("Input", "Nome da Playlist: ",
                                 parent=self.root)
        self.ctrlPlaylist.consultarPlaylists(nomePlaylist)
    
    def salvaDados(self):
        self.ctrlArtista.salvaArtistas()
        self.ctrlAlbum.salvaAlbuns()
        self.ctrlPlaylist.salvaPlaylists()
        self.ctrlMusica.salvaMusicas()
        self.root.destroy()
        
if __name__ == '__main__':
    c = ControlePrincipal()