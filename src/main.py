# --- IMPORTES ---
# Aquí tendrás que importar tus clases dependiendo de cómo hayas llamado a tus archivos
# Ejemplo: from modelo import Cancion, Cantante, Playlist, Sesion
# Ejemplo: from patrones import BusquedaAlfabetica, BusquedaAleatoria, ManejadorSonoro...
# Ejemplo: from recomendador import Recomendador

import Clases, Decorador, Manejador, Recomendador, Strategy
from Clases import *
from Manejador import *
from Decorador import *
from Recomendador import *
from Strategy import *

Fecha1 = Clases.Fecha(12,2,2025)
Fecha2 = Clases.Fecha(1,7,2021)
Fecha3 = Clases.Fecha(2,2,1999)
Fecha4 = Clases.Fecha(15,4,2025)
Fecha5 = Clases.Fecha(9,4,1995)
Fecha6 = Clases.Fecha(12,9,2005)
Fecha7 = Clases.Fecha(31,1,2025)

# --- ATRIBUTOS SONOROS (SO) ---

atributoSO1 = {
    "ritmo": 0.2,
    "tono": 0.10,
    "escala": 0.45
}

# Canción rápida y aguda
atributoSO2 = {
    "ritmo": 0.85,
    "tono": 0.90,
    "escala": 0.70
}

# Canción de ritmo medio, muy grave
atributoSO3 = {
    "ritmo": 0.50,
    "tono": 0.15,
    "escala": 0.30
}

# Canción acústica o chill
atributoSO4 = {
    "ritmo": 0.35,
    "tono": 0.60,
    "escala": 0.50
}


# --- ATRIBUTOS SENTIMENTALES (SE) ---

atributoSE1 = {
    "felicidad": 0.7,
    "tristeza": 0.9,
    "otro": 0.1
}

# Canción muy alegre, cero tristeza
atributoSE2 = {
    "felicidad": 0.95,
    "tristeza": 0.05,
    "otro": 0.3
}

# Canción deprimente o melancólica
atributoSE3 = {
    "felicidad": 0.10,
    "tristeza": 0.85,
    "otro": 0.6
}

# Canción neutra o épica (fuerte en "otro")
atributoSE4 = {
    "felicidad": 0.40,
    "tristeza": 0.40,
    "otro": 0.90
}



def main():
    print("=== INICIANDO PRUEBA DEL RECOMENDADOR MVP ===")

    print("\n1. CREANDO DATOS DE PRUEBA...")
    # Ajusta estos datos según los parámetros que pidan tus clases
    cancion1 = Cancion(1,"Jesucristo Garcia",Fecha1,atributoSO1,atributoSE1) # Imagina que tiene atributos y fecha por dentro
    cancion2 = Cancion(2,"So payaso",Fecha2,atributoSO2,atributoSE2)

    cancion3 = Cancion(2,"Fiesta pagana",Fecha3,atributoSO3,atributoSE3)
    cancion4 = Cancion(2,"Molinos de viento",Fecha4,atributoSO4,atributoSE4)

    canciones_Extremoduro = [cancion1, cancion2]
    canciones_magodeoz = [cancion3,cancion4]

    cantante1 = Cantante("Extremoduro",Fecha5,canciones_Extremoduro)
    cantante2 = Cantante("Mago de oz",Fecha6,canciones_magodeoz)


    lista_canciones_playlist = [cancion1, cancion2, cancion3, cancion4]

    playlist1 = Playlist("Rock Español",Fecha7,lista_canciones_playlist)

    lista_canciones = [cancion1, cancion2]
    lista_cantantes = [cantante1]
    lista_playlists = [playlist1]


    print("\n2. PROBANDO LA SESIÓN Y CADENA DE RESPONSABILIDAD...")
    mi_sesion = Sesion()
    # Asumiendo que tienes un método para añadir canciones a la sesión
    mi_sesion.agregar_cancion(cancion1) 
    mi_sesion.agregar_cancion(cancion2)

    # Creamos y ejecutamos la cadena matemática
    eslabon_sonoro = ManejadorSonoro()
    # Si tienes el sentimental: eslabon_sonoro.set_siguiente(eslabon_sentimental)
    eslabon_sonoro.procesar(mi_sesion)
    
    print(f" -> Medias calculadas: {mi_sesion.get_media_sonora()}")


    print("\n3. PROBANDO EL CATÁLOGO (DECORATOR)...")
    mi_catalogo = CatalogoCanciones(lista_canciones)
    mi_catalogo = DecoradorArtistas(mi_catalogo, lista_cantantes)
    mi_catalogo = DecoradorPlaylists(mi_catalogo, lista_playlists)
    
    print(f" -> Total de elementos en el catálogo: {len(mi_catalogo.obtener_elementos())}")


    print("\n4. CONECTANDO EL RECOMENDADOR...")
    id_usuario = 1
    recomendador = Recomendador.obtener_instancia(id_usuario)
    
    # Le enchufamos las piezas
    recomendador.set_sesion(mi_sesion)
    recomendador.set_catalogo(mi_catalogo)
    print(" -> Recomendador configurado con éxito.")


    print("\n5. PROBANDO ESTRATEGIAS (STRATEGY)...")
    
    # Búsqueda Alfabética
    recomendador.set_estrategia(BusquedaAlfabetica())
    resultado_alfabetico = recomendador.recomendar()
    print(f" -> Recomendación Alfabética: {resultado_alfabetico}") 
    # Debería salirte 'A Dios le pido' o algo similar

    # Búsqueda Aleatoria
    recomendador.set_estrategia(BusquedaAleatoria())
    resultado_aleatorio = recomendador.recomendar()
    print(f" -> Recomendación Aleatoria: {resultado_aleatorio}")

    print("\n=== PRUEBA FINALIZADA ===")

if __name__ == "__main__":
    main()