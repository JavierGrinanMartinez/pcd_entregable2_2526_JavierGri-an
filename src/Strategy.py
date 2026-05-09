from abc import ABC, abstractmethod
import random

class EstrategiaBusqueda(ABC):
    @abstractmethod

    def buscar(self, catalogo: list, medias_sesion: dict) -> object:
        pass

  
class BusquedaAlfabetica(EstrategiaBusqueda):
    
    def buscar(self, catalogo: list, medias_sesion: dict) -> object:
        if not catalogo:
            return None
                
        catalogo_ordenado = sorted(catalogo, key=str) # lo de key=str es para que ordene alfabeticamente, por eso hice los __str__
        
        return catalogo_ordenado[0]

class BusquedaTemporal(EstrategiaBusqueda):
    
    def buscar(self, catalogo: list, medias_sesion: dict) -> object:
        if not catalogo:
            return None
            
        catalogo_ordenado = sorted(catalogo, key=lambda item: item.get_fecha(), reverse=True)
        
        return catalogo_ordenado[0]

class BusquedaAleatoria(EstrategiaBusqueda):
    
    def buscar(self, catalogo: list, medias_sesion: dict) -> object:
        elemento_elegido = random.choice(catalogo)
        
        return elemento_elegido