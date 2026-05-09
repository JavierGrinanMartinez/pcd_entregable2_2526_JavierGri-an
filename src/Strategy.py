from abc import ABC, abstractmethod
import random
from excepciones import *

class EstrategiaBusqueda(ABC):
    @abstractmethod

    def buscar(self, catalogo: list, medias_sesion: dict) -> object:
        pass

  
class BusquedaAlfabetica(EstrategiaBusqueda):
    
    def buscar(self, catalogo: list, medias_sesion: dict) -> object:
        try:
            if not catalogo:
                raise ElementoNoEncontradoError("Catálogo", "La estrategia alfabética recibió una lista vacía.")
                    
            catalogo_ordenado = sorted(catalogo, key=str) # lo de key=str es para que ordene alfabeticamente, por eso hice los __str__
            
            return catalogo_ordenado[0]

        except Exception as e:
            raise RecomendadorError(f"Error en BusquedaAlfabetica: {e}")

class BusquedaTemporal(EstrategiaBusqueda):
    
    try:
        def buscar(self, catalogo: list, medias_sesion: dict) -> object:
            if not catalogo:
                raise ElementoNoEncontradoError("Catálogo", "La estrategia temporal recibió una lista vacía.")
                
            try: # Si un objeto no tiene get_fecha() o devuelve None, lambda fallará.
                catalogo_ordenado = sorted(catalogo, key=lambda item: item.get_fecha(), reverse=True)
            except AttributeError:
                raise AtributoInvalidoError("Uno de los elementos del catálogo no tiene el método get_fecha().")
            except TypeError:
                raise AtributoInvalidoError("Error al comparar fechas: asegúrate de que todas tengan el mismo formato.")
            
            return catalogo_ordenado[0]

    except (ElementoNoEncontradoError, AtributoInvalidoError) as e:
        raise e # Re-lanzamos nuestras excepciones específicas
    except Exception as e:
        raise RecomendadorError(f"Error inesperado en BusquedaTemporal: {e}")

class BusquedaAleatoria(EstrategiaBusqueda):
    
    def buscar(self, catalogo: list, medias_sesion: dict) -> object:
        try:
            if not catalogo:
                raise ElementoNoEncontradoError("Catálogo", "No se puede elegir un elemento aleatorio de un catálogo vacío.")
            
            return random.choice(catalogo)
            
        except ElementoNoEncontradoError as e:
            raise e
        