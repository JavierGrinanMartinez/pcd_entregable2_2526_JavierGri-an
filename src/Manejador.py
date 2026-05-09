# patron Cadena de responabilidad

from abc import ABC, abstractmethod

class ManejadorEstadisticas(ABC):
    def __init__(self):
        self._siguiente = None

    def set_siguiente(self, manejador: 'ManejadorEstadisticas') -> 'ManejadorEstadisticas':
        self._siguiente = manejador
        return manejador

    @abstractmethod
    def procesar(self, sesion: object) -> None:
        if self._siguiente is not None:
            self._siguiente.procesar(sesion)


class ManejadorSonoro(ManejadorEstadisticas):
    def procesar(self, sesion: object) -> None:
        canciones = sesion.get_canciones_escuchadas()
        
        if canciones:
            suma_medias_canciones = 0
            
            for cancion in canciones:
                atributos = cancion.get_atributos_sonoros()
                if atributos:
                    media_cancion = sum(atributos.values()) / len(atributos) #calcular media de cada cancion
                    suma_medias_canciones += media_cancion #suma la media al cumulo
            
            media_total_sesion = suma_medias_canciones / len(canciones) #calcula la media de todo
            
            sesion.set_media_sonora({"media_general": media_total_sesion})
        
        super().procesar(sesion)


class ManejadorSentimental(ManejadorEstadisticas):
    def procesar(self, sesion: object) -> None:
        canciones = sesion.get_canciones_escuchadas()
        
        if canciones:
            suma_medias_canciones = 0
            
            for cancion in canciones:
                atributos = cancion.get_atributos_sentimentales()
                if atributos:
                    media_cancion = sum(atributos.values()) / len(atributos) #calcular media de cada cancion
                    suma_medias_canciones += media_cancion #suma la media al cumulo
            
            media_total_sesion = suma_medias_canciones / len(canciones) #calcula la media de todo
            
            sesion.set_media_sentimental({"media_general": media_total_sesion})
        
        super().procesar(sesion)