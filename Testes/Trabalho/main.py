import tkinter as tk
from tkinter import simpledialog
import artista as art
import album as alb
import playlist as pl

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)

        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)  

        self.artistaMenu.add_command(label='Cadastrar Artista', \
            command=self.controle.cadastrarArtista)  
        self.artistaMenu.add_command(label='Consultar Artista', \
            command=self.controle.consultarArtista) 
        self.menubar.add_cascade(label="Artista", \
            menu=self.artistaMenu)

        self.albumMenu.add_command(label='Cadastrar Álbum', \
            command=self.controle.cadastrarAlbum)  
        self.albumMenu.add_command(label='Consultar Álbum', \
            command=self.controle.consultarAlbum)        
        self.menubar.add_cascade(label='Álbum', \
            menu=self.albumMenu )

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
        
        self.ctrlArtista = art.ControleArtista(self)
        self.ctrlAlbum = alb.ControleAlbum(self)
        self.ctrlPlaylist = pl.CtrlPlaylist(self)

        self.limite = LimitePrincipal(self.root, self)
        self.root.title('Sistema')

        self.root.mainloop()

    def cadastrarArtista(self):
        self.ctrlArtista.cadastrarArtista()

    def consultarArtista(self):
        self.ctrlArtista.consultarArtista()

    def cadastrarAlbum(self):
        self.ctrlAlbum.cadastrarAlbum()

    def consultarAlbum(self):
        self.ctrlAlbum.consultarAlbum()

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
        self.root.destroy()

if __name__ == '__main__':
    C = ControlePrincipal()