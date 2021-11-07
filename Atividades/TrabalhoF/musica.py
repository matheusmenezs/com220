import os.path
import pickle

class Musica:
    def __init__(self, titulo, artista, album, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def getAlbum(self):
        return self.__album
        
    def getNroFaixa(self):
        return self.__nroFaixa

class CtrlMusica:
    def __init__(self, ctrlPrincipal):
        self.ctrlPrincipal = ctrlPrincipal
    
        if not os.path.isfile("musicas.pickle"):
            self.listaMusicas = []
        else:
            with open("musicas.pickle", "rb") as f1:
                self.listaMusicas = pickle.load(f1)

    def salvaMusicas(self):
        if len(self.listaMusicas) != 0:
            with open("musicas.pickle","wb") as f1:
                pickle.dump(self.listaMusicas, f1)

    def getMusica(self, nomeMusica):
        musicaSel = None
        for mu in self.listaMusicas:
            if mu.getTitulo() == nomeMusica:
                musicaSel = mu
        return musicaSel 

    def gravaMusica(self, titulo, artista, album):
        nroFaixa = len(self.listaMusicas)
        musica = Musica(titulo, artista, album, (nroFaixa+1))
        self.listaMusicas.append(musica)
        return musica