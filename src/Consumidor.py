import json
from kafka import KafkaConsumer

import Clases, Decorador, Manejador, Recomendador, Strategy
from Clases import *
from Manejador import *
from Decorador import *
from Recomendador import *
from Strategy import *

def iniciar_consumidor():
    Fecha1 = Clases.Fecha(12,2,2025)
    Fecha2 = Clases.Fecha(1,7,2021)
    Fecha3 = Clases.Fecha(2,2,1999)
    Fecha4 = Clases.Fecha(15,4,2025)
    Fecha5 = Clases.Fecha(9,4,1995)
    Fecha6 = Clases.Fecha(12,9,2005)
    Fecha7 = Clases.Fecha(31,1,2025)

    atributoSO1 = {"ritmo": 0.2, "tono": 0.10, "escala": 0.45}
    atributoSO2 = {"ritmo": 0.85, "tono": 0.90, "escala": 0.70}
    atributoSO3 = {"ritmo": 0.50, "tono": 0.15, "escala": 0.30}
    atributoSO4 = {"ritmo": 0.35, "tono": 0.60, "escala": 0.50}

    atributoSE1 = {"felicidad": 0.7, "tristeza": 0.9, "otro": 0.1}
    atributoSE2 = {"felicidad": 0.95, "tristeza": 0.05, "otro": 0.3}
    atributoSE3 = {"felicidad": 0.10, "tristeza": 0.85, "otro": 0.6}
    atributoSE4 = {"felicidad": 0.40, "tristeza": 0.40, "otro": 0.90}

    cancion1 = Cancion(1,"Jesucristo Garcia",Fecha1,atributoSO1,atributoSE1) 
    cancion2 = Cancion(2,"So payaso",Fecha2,atributoSO2,atributoSE2)
    cancion3 = Cancion(3,"Fiesta pagana",Fecha3,atributoSO3,atributoSE3)
    cancion4 = Cancion(4,"Molinos de viento",Fecha4,atributoSO4,atributoSE4)

    base_datos_canciones = {
        "Jesucristo Garcia": cancion1,
        "So payaso": cancion2,
        "Fiesta pagana": cancion3,
        "Molinos de viento": cancion4
    }

    canciones_Extremoduro = [cancion1, cancion2]
    canciones_magodeoz = [cancion3, cancion4]
    cantante1 = Cantante("Extremoduro",Fecha5,canciones_Extremoduro)
    cantante2 = Cantante("Mago de oz",Fecha6,canciones_magodeoz)
    lista_canciones_playlist = [cancion1, cancion2, cancion3, cancion4]
    playlist1 = Playlist("Rock Español",Fecha7,lista_canciones_playlist)

    mi_catalogo = CatalogoCanciones([cancion1, cancion2])
    mi_catalogo = DecoradorArtistas(mi_catalogo, [cantante1, cantante2])
    mi_catalogo = DecoradorPlaylists(mi_catalogo, [playlist1])

    mi_sesion = Sesion()
    eslabon_sonoro = ManejadorSonoro()
    
    recomendador = Recomendador.obtener_instancia(1)
    recomendador.set_sesion(mi_sesion)
    recomendador.set_catalogo(mi_catalogo)
    recomendador.set_estrategia(BusquedaAlfabetica()) 

    consumidor = KafkaConsumer(
        'historial_escuchas',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest', 
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for mensaje in consumidor:
        datos = mensaje.value
        titulo = datos.get("titulo_cancion")
        
        print(f"[NUEVO MENSAJE] El usuario ha escuchado: '{titulo}'")
        
        cancion_real = base_datos_canciones.get(titulo)
        
        if cancion_real:
            mi_sesion.agregar_cancion(cancion_real)
            eslabon_sonoro.procesar(mi_sesion)
            medias_actuales = mi_sesion.get_media_sonora()
            siguiente_cancion = recomendador.recomendar()
            
            print(f"Medias recalculadas: {medias_actuales}")
            print(f"EL RECOMENDADOR SUGIERE: {siguiente_cancion}\n")
        else:
            print("Cancion no encontrada en el catalogo.")

if __name__ == "__main__":
    iniciar_consumidor()