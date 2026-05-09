from abc import ABC, abstractmethod

class Catalogo(ABC):
    @abstractmethod
    def obtener_catalogo(self) -> list:
        #Devuelve la lista de elementos del catálogo
        pass

class CatalogoCanciones(ComponenteCatalogo):
    def __init__(self, canciones: list):
        self._canciones = canciones

    def obtener_catalogo(self) -> list:
        return self._canciones

class DecoradorCatalogo(ComponenteCatalogo):

    def __init__(self, componente: Catalogo):
        self._componente = componente

    @abstractmethod
    def obtener_elementos(self) -> list:
        pass

class DecoradorArtistas(DecoradorCatalogo):
    def __init__(self, componente: Catalogo, cantantes: list):
        super().__init__(componente)
        self._cantantes = cantantes

    def obtener_elementos(self) -> list:
        # le añade a la lista los los cantantes
        # ejemplo: 
        # lista = [cancion1,cancion2,cancion3] -> lista_decorada [cancion1,cancion2,cancion3,cantante1,cantante2]
        return self._componente.obtener_elementos() + self._cantantes

class DecoradorPlaylists(DecoradorCatalogo):
    def __init__(self, componente: Catalogo, playlists: list):
        super().__init__(componente)
        self._playlists = playlists

    def obtener_elementos(self) -> list:
        # le añade a la lista las playlist
        # ejemplo: 
        # lista = [cancion1,cancion2,cancion3] -> lista_decorada [cancion1,cancion2,cancion3,playlist1,playlist2]
        return self._componente.obtener_elementos() + self._playlists