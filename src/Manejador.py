# patron Cadena de responabilidad
from excepciones import *
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
        try:
            canciones = sesion.get_canciones_escuchadas()
            
            if not canciones:
                print("Aviso Manejador: La sesión no tiene canciones para calcular medias.")
                super().procesar(sesion)
                return

            
            suma_medias_canciones = 0
            canciones_validas = 0
                
            for cancion in canciones:
                try:
                    atributos = cancion.get_atributos_sonoros()
                    if not atributos:
                        raise AtributoInvalidoError(f"Canción '{cancion.get_titulo()}' no tiene atributos sonoros.")

                    if len(atributos) == 0:
                        raise AtributoInvalidoError(f"Diccionario de atributos vacío en '{cancion.get_titulo()}'.")

                    
                    media_cancion = sum(atributos.values()) / len(atributos) #calcular media de cada cancion
                    suma_medias_canciones += media_cancion #suma la media al cumulo
                    canciones_validas += 1

                except AtributoInvalidoError as e:
                    print(f"Error en dato: {e}")
    
                    continue #continua a la siguiente cancion

            if canciones_validas > 0:
                media_total_sesion = suma_medias_canciones / canciones_validas
                sesion.set_media_sonora({"media_general": media_total_sesion})
            else:
                raise RecomendadorError("No se pudo calcular ninguna media válida en esta sesión.")
                
        except Exception as e:
            print(f"Error inesperado en el procesado de la cadena: {e}")
            

        super().procesar(sesion)


class ManejadorSentimental(ManejadorEstadisticas):

    def procesar(self, sesion: object) -> None:
        try:
            canciones = sesion.get_canciones_escuchadas()
            
            if not canciones:
                print("Aviso Manejador: La sesión no tiene canciones para calcular medias.")
                super().procesar(sesion)
                return

            
            suma_medias_canciones = 0
            canciones_validas = 0
                
            for cancion in canciones:
                try:
                    atributos = cancion.get_atributos_sentimentales()
                    if not atributos:
                        raise AtributoInvalidoError(f"Canción '{cancion.get_titulo()}' no tiene atributos sonoros.")

                    if len(atributos) == 0:
                        raise AtributoInvalidoError(f"Diccionario de atributos vacío en '{cancion.get_titulo()}'.")

                    
                    media_cancion = sum(atributos.values()) / len(atributos) #calcular media de cada cancion
                    suma_medias_canciones += media_cancion #suma la media al cumulo
                    canciones_validas += 1

                except AtributoInvalidoError as e:
                    print(f"Error en dato: {e}")
    
                    continue #continua a la siguiente cancion

            if canciones_validas > 0:
                media_total_sesion = suma_medias_canciones / canciones_validas
                sesion.set_media_sonora({"media_general": media_total_sesion})
            else:
                raise RecomendadorError("No se pudo calcular ninguna media válida en esta sesión.")
                
        except Exception as e:
            print(f"Error inesperado en el procesado de la cadena: {e}")
            

        super().procesar(sesion)