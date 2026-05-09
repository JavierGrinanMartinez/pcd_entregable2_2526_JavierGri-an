class RecomendadorError(Exception):
    """Clase base para excepciones del Recomendador."""
    pass

class ElementoNoEncontradoError(RecomendadorError):
    """Se lanza cuando se busca una canción o artista que no existe."""
    def __init__(self, elemento, mensaje="El elemento no existe en el catálogo"):
        self.elemento = elemento
        self.mensaje = f"{mensaje}: {elemento}"
        super().__init__(self.mensaje)

class SesionVaciaError(RecomendadorError):
    """Se lanza cuando intentas recomendar sin haber escuchado nada antes."""
    pass

class AtributoInvalidoError(RecomendadorError):
    """Se lanza si los atributos sonoros/sentimentales no tienen el formato correcto."""
    pass