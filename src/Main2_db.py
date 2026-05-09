import sqlite3
from Clases import *
from Manejador import *
from Decorador import *
from Strategy import *
from Recomendador import *
import logging

logging.basicConfig(filename='sistema.log', level=logging.ERROR)

def cargar_todo_desde_db():
    """Carga canciones y crea objetos Cantante automáticamente."""
    try:
        conexion = sqlite3.connect('biblioteca.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM canciones")
        filas = cursor.fetchall()
        
        canciones_por_artista = {}
        todas_las_canciones = []

        for fila in filas:
            id_c, titulo, nombre_artista, f_str, ritmo, tono, escala = fila
            
            d, m, a = map(int, f_str.split('-'))
            obj_fecha = Fecha(d, m, a)
            
            attrs = {"ritmo": ritmo, "tono": tono, "escala": escala}
            
            nueva_cancion = Cancion(id_c, titulo, obj_fecha, attrs, {})
            todas_las_canciones.append(nueva_cancion)
            
            if nombre_artista not in canciones_por_artista:
                canciones_por_artista[nombre_artista] = []
            canciones_por_artista[nombre_artista].append(nueva_cancion)
            
        # Crear lista de objetos Cantante (usando la fecha de la primera canción como cumple ficticio)
        lista_objetos_cantantes = []
        for nombre, canciones in canciones_por_artista.items():
            nuevo_cantante = Cantante(nombre, Fecha(1,1,1980), canciones)
            lista_objetos_cantantes.append(nuevo_cantante)
            
        conexion.close()
        return todas_las_canciones, lista_objetos_cantantes

    except Exception as e:
        logging.error(f"Error al cargar base de datos: {e}")
        print(f"Error crítico al leer 'biblioteca.db': {e}")
        return [], []

def main2():
    print("=== EJECUTABLE 2: SISTEMA BASADO EN PERSISTENCIA (SQLITE) ===")
    
    canciones, cantantes = cargar_todo_desde_db()
    
    if not canciones:
        print("No hay datos disponibles para ejecutar.")
        return

    try:

        catalogo = CatalogoCanciones(canciones)
        catalogo_decorado = DecoradorArtistas(catalogo, cantantes)
        
        print(f" -> Catálogo listo: {len(canciones)} canciones y {len(cantantes)} artistas cargados.")

        # 3. Configuración del Recomendador
        recomendador = Recomendador.obtener_instancia(2)
        recomendador.set_catalogo(catalogo_decorado)
        
        # 4. Simulación de Sesión (escucha canciones)
        mi_sesion = Sesion()
        mi_sesion.agregar_cancion(canciones[0]) # Jesucristo Garcia
        mi_sesion.agregar_cancion(canciones[2]) # La vereda de la puerta de atras
        
        # cadena de responsabilidad
        ManejadorSonoro().procesar(mi_sesion)
        recomendador.set_sesion(mi_sesion)

        # 5. Ejecución de Estrategias
        print("\n--- RESULTADOS DE RECOMENDACIÓN ---")
        
        recomendador.set_estrategia(BusquedaAlfabetica())
        print(f"Estrategia Alfabética: {recomendador.recomendar()}")
        
        recomendador.set_estrategia(BusquedaTemporal())
        print(f"Estrategia Temporal: {recomendador.recomendar()}")

        recomendador.set_estrategia(BusquedaAleatoria())
        print(f"Estrategia Aleatoria: {recomendador.recomendar()}")

        recomendador.set_estrategia(EstrategiaMatchSimilitud())
        print(f"Estrategia match: {recomendador.recomendar()}")
        

    except Exception as e:
        print(f"Se produjo un error durante la ejecución: {e}")
        logging.error(f"Fallo en main2: {e}")

if __name__ == "__main__":
    main2()