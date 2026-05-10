import asyncio
import os
import sqlite3
from datetime import datetime
import random
from Clases import *
from Manejador import *
from Decorador import *
from Strategy import *
from Recomendador import *

# --- CARGA AUTÓNOMA A PRUEBA DE TERMINAL ---
def cargar_db_independiente():
    ruta_actual = os.path.dirname(__file__)
    ruta_db = os.path.join(ruta_actual, 'biblioteca.db')
    
    try:
        conexion = sqlite3.connect(ruta_db)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM canciones")
        filas = cursor.fetchall()
        
        canciones = []
        canciones_por_artista = {}
        
        for fila in filas:
            id_c, titulo, nombre_artista, f_str, ritmo, tono, escala = fila
            d, m, a = map(int, f_str.split('-'))
            attrs = {"ritmo": ritmo, "tono": tono, "escala": escala}
            
            cancion = Cancion(id_c, titulo, Fecha(d, m, a), attrs, {})
            canciones.append(cancion)
            
            if nombre_artista not in canciones_por_artista:
                canciones_por_artista[nombre_artista] = []
            canciones_por_artista[nombre_artista].append(cancion)
            
        cantantes = []
        for nombre, lista_c in canciones_por_artista.items():
            cantantes.append(Cantante(nombre, Fecha(1,1,1980), lista_c))
            
        conexion.close()
        return canciones, cantantes
    except Exception as e:
        print(f"Error cargando DB en main_async: {e}")
        return [], []

# --- LÓGICA DE ASINCRONÍA Y MATCH ---
async def productor_usuario(cola, lista_ids):
    print("[Usuario] Iniciando sesión de escucha...")
    for id_cancion in lista_ids:
        await asyncio.sleep(2) 
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tupla_evento = (id_cancion, fecha_hora_actual)
        
        print(f"\n[Evento de Streaming] -> {tupla_evento}")
        await cola.put(tupla_evento)

async def consumidor_sistema(cola, sesion, recomendador, todas_las_canciones):
    manejador = ManejadorSonoro()
    
    while True:
        id_recibido, fecha_hora = await cola.get()
        cancion_escuchada = next((c for c in todas_las_canciones if c.get_id_cancion() == id_recibido), None)
        
        if cancion_escuchada:
            print(f"    Canción identificada: {cancion_escuchada.get_titulo()}")
            sesion.agregar_cancion(cancion_escuchada)
            manejador.procesar(sesion)
            
            media_actual = sesion.get_media_sonora().get('media_general', 0)
            print(f"    Nueva media de la sesión: {media_actual:.3f}")
            
            match_encontrado = recomendador.recomendar()
            print(f"    MATCH ENCONTRADO (Similitud): {match_encontrado} ")
        else:
            print(f"    Error: El ID {id_recibido} no existe.")
        
        cola.task_done()

async def main_async():
    print("=== EJECUTABLE 3: SISTEMA DE MATCHING POR STREAMING ===")
    cola_eventos = asyncio.Queue()
    mi_sesion = Sesion()
    
    # Carga segura
    canciones_db, cantantes_db = cargar_db_independiente()
    
    if not canciones_db:
        print("ERROR: No se ha podido cargar la base de datos.")
        return

    # Configurar Recomendador
    catalogo_decorado = DecoradorArtistas(CatalogoCanciones(canciones_db), cantantes_db)
    recomendador = Recomendador.obtener_instancia(3)
    recomendador.set_catalogo(catalogo_decorado)
    recomendador.set_estrategia(EstrategiaMatchSimilitud())
    recomendador.set_sesion(mi_sesion)

    # Simular usuario con 4 canciones que sí existan
    cantidad = min(4, len(canciones_db))
    ids_a_escuchar = [c.get_id_cancion() for c in random.sample(canciones_db, cantidad)]

    try:
        tarea = asyncio.create_task(consumidor_sistema(cola_eventos, mi_sesion, recomendador, canciones_db))
        await productor_usuario(cola_eventos, ids_a_escuchar)
        await cola_eventos.join()
        tarea.cancel()
        print("\n=== FIN DE LA SIMULACIÓN ===")
    except Exception as e:
        print(f"Error durante la simulación: {e}")

if __name__ == "__main__":
    asyncio.run(main_async())