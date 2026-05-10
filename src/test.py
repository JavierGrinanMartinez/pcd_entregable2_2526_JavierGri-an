import pytest
from Clases import Cancion, Sesion, Fecha, Cantante, Playlist
from Manejador import ManejadorSonoro
from Decorador import CatalogoCanciones, DecoradorArtistas, DecoradorPlaylists
from Strategy import BusquedaAlfabetica, BusquedaAleatoria
from Recomendador import Recomendador
from excepciones import AtributoInvalidoError, SesionVaciaError

# --- TESTS DE CLASES BÁSICAS ---

def test_creacion_cancion():
    fecha = Fecha(10, 5, 2026)
    so = {"ritmo": 0.5}
    se = {"felicidad": 0.8}
    cancion = Cancion(1, "La vereda de la puerta de atras", fecha, so, se)
    assert cancion.get_titulo() == "La vereda de la puerta de atras"
    assert cancion.get_atributos_sonoros()["ritmo"] == 0.5

# --- TESTS DE MANEJADOR (CHAIN OF RESP) ---

def test_calculo_media_manejador_sonoro():
    sesion = Sesion()
    # Canción 1: media 0.2 | Canción 2: media 0.8 -> Media total 0.5
    c1 = Cancion(1, "C1", None, {"r": 0.1, "t": 0.3}, {})
    c2 = Cancion(2, "C2", None, {"r": 0.7, "t": 0.9}, {})
    sesion.agregar_cancion(c1)
    sesion.agregar_cancion(c2)
    
    manejador = ManejadorSonoro()
    manejador.procesar(sesion)
    
    assert sesion.get_media_sonora()["media_general"] == pytest.approx(0.5)

# --- TESTS DE DECORADOR ---

def test_decorador_artistas_añade_elementos():
    base = CatalogoCanciones(["Cancion A"])
    decorado = DecoradorArtistas(base, ["Artista X"])
    resultado = decorado.obtener_elementos()
    assert len(resultado) == 2
    assert "Artista X" in resultado

def test_decorador_playlists_añade_elementos():
    base = CatalogoCanciones(["C1"])
    decorado = DecoradorPlaylists(base, ["Playlist Rock"])
    assert "Playlist Rock" in decorado.obtener_elementos()

# --- TESTS DE STRATEGY ---

def test_estrategia_alfabetica():
    estrategia = BusquedaAlfabetica()
    catalogo = ["Zahara", "Arde Bogotá", "Extremoduro"]
    # Al ser strings, sorted los ordena por letra
    assert estrategia.buscar(catalogo, {}) == "Arde Bogotá"

def test_estrategia_aleatoria_devuelve_algo():
    estrategia = BusquedaAleatoria()
    catalogo = ["C1", "C2", "C3"]
    resultado = estrategia.buscar(catalogo, {})
    assert resultado in catalogo

# --- TESTS DE RECOMENDADOR (SINGLETON Y LÓGICA) ---

def test_recomendador_instancia_unica():
    r1 = Recomendador.obtener_instancia(1)
    r2 = Recomendador.obtener_instancia(1)
    assert r1 is r2

# --- TESTS DE EXCEPCIONES ---

def test_excepcion_crear_decorador_sin_componente():
    with pytest.raises(Exception): # Debería lanzar RecomendadorError según tu lógica
        DecoradorArtistas(None, ["Artista"])
