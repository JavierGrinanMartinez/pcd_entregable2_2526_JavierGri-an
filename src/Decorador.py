from abc import ABC, abstractmethod
from excepciones import *

class Catalogo(ABC):
    @abstractmethod
    def obtener_elementos(self) -> list:
        #Devuelve la lista de elementos del catálogo
        pass

class CatalogoCanciones(Catalogo):
    def __init__(self, canciones: list):
        if canciones is None:
            raise AtributoInvalidoError("La lista inicial de canciones no puede ser None")
        self._canciones = canciones

    def obtener_elementos(self) -> list:
        return self._canciones

class DecoradorCatalogo(Catalogo):

    def __init__(self, componente: Catalogo):
        if componente is None:
            raise RecomendadorError("No se puede crear un decorador sin componente")
        self._componente = componente

    @abstractmethod
    def obtener_elementos(self) -> list:
        pass

    def obtener_elementos(self) -> list:

        # le añade a la lista los los cantantes
        # ejemplo: 
        # lista = [cancion1,cancion2,cancion3] -> lista_decorada [cancion1,cancion2,cancion3,cantante1,cantante2]

        try:
            elementos_base = self._componente.obtener_elementos()
            # Validación de seguridad: nos aseguramos de que ambos sean listas antes de sumar
            if not isinstance(elementos_base, list):
                raise AtributoInvalidoError("El componente decorado no devolvió una lista válida.")
            
            return elementos_base + self._cantantes
        except Exception as e:
            raise RecomendadorError(f"Error al decorar con artistas: {e}")

class DecoradorArtistas(DecoradorCatalogo):
    def __init__(self, componente: Catalogo, cantantes: list):
        super().__init__(componente)
        if not isinstance(cantantes, list):
            raise AtributoInvalidoError("El decorador de artistas requiere una lista de cantantes.")
        self._cantantes = cantantes

    def obtener_elementos(self) -> list:

        # le añade a la lista los cantantes
        # ejemplo:
        # lsita = [cancion1, cancion2, cancion3] ->[cancion1, cancion2, cancion3, artista1, artista2]

        try:
            elementos_base = self._componente.obtener_elementos()
            if not isinstance(elementos_base, list):
                raise AtributoInvalidoError("El componente decorado no devolvió una lista válida.")
            
            return elementos_base + self._cantantes
        except Exception as e:
            raise RecomendadorError(f"Error al decorar con artistas: {e}")

class DecoradorPlaylists(DecoradorCatalogo):
    def __init__(self, componente: Catalogo, playlists: list):
            super().__init__(componente)
            if not isinstance(playlists, list):
                raise AtributoInvalidoError("El decorador de playlists requiere una lista de objetos playlist.")
            self._playlists = playlists

    def obtener_elementos(self) -> list:

        # le añade a la lista las playlist
        # ejemplo: 
        # lista = [cancion1,cancion2,cancion3] -> lista_decorada [cancion1,cancion2,cancion3,playlist1,playlist2]

        try:
            elementos_base = self._componente.obtener_elementos()
            if not isinstance(elementos_base, list):
                raise AtributoInvalidoError("El componente decorado no devolvió una lista válida.")
                
            return elementos_base + self._playlists
        except Exception as e:
            raise RecomendadorError(f"Error al decorar con playlists: {e}")