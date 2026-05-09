from excepciones import *


class Recomendador:


    _instancias = {} 

    def __init__(self, id_usuario: int):
        self._id_usuario = id_usuario
        self._sesion_actual = None
        self._estrategia = None
        self._catalogo_activo = None

    @classmethod
    def obtener_instancia(cls, id_usuario: int):
        """
        Si id_usuario no tiene una instancia creada se le crea 1
        siempre devuelve la instancia para ese usuario
        """
        if id_usuario not in cls._instancias:
            cls._instancias[id_usuario] = cls(id_usuario)
        
        return cls._instancias[id_usuario]


# --- GETTERS ---
    
    def get_catalogo(self):
        return self._catalogo_activo

# --- SETTERS ---

    @classmethod
    def set_instancia(cls, id_usuario: int, instancia):
        """
        Permite establecer manualmente la instancia de un usuario.
        """
        cls._instancias[id_usuario] = instancia

    def set_estrategia(self, estrategia):
        """
        Establece la estrategia de búsqueda
        """
        self._estrategia = estrategia

    def set_catalogo(self, catalogo):
        """
        Establece el catálogo
        """
        self._catalogo_activo = catalogo

    # 3. Añadido: El setter para la sesión que faltaba
    def set_sesion(self, sesion):
        """
        Establece la sesión activa del usuario
        """
        self._sesion_actual = sesion


# --- METODOS ---
    def recomendar(self) -> object:
        """
        Conecta el Decorator, la Sesion y el Strategy para devolver una recomendación.
        """

        if self._catalogo_activo is None:
            raise RecomendadorError("No se puede recomendar: El catálogo no ha sido inicializado.")

        if self._estrategia is None:
            raise RecomendadorError("No se puede recomendar: Falta definir la estrategia de búsqueda.")
            
        if self._sesion_actual is None:
            raise RecomendadorError("No se puede recomendar: No hay una sesión activa.")

        if not self._sesion_actual.get_canciones_escuchadas():
                raise SesionVaciaError("La sesión no tiene canciones escuchadas para generar una media.")



        # 2. PATRÓN DECORATOR: saca la lista catalogo
        lista_catalogo = self._catalogo_activo.obtener_elementos()
        if not lista_catalogo:
                raise ElementoNoEncontradoError("Catálogo", "El catálogo está vacío.")

        # 3. PATRÓN CHAIN OF RESP: Saca los calculos
        diccionario_medias = self._sesion_actual.get_media_sonora()
        if not diccionario_medias:
                raise AtributoInvalidoError("Las medias sonoras no se han calculado correctamente.")

        # 4. PATRÓN STRATEGY: Le pasamos la lista y las medias al cartucho de búsqueda
        resultado = self._estrategia.buscar(lista_catalogo, diccionario_medias)

        if resultado is None:
                print("Aviso: La estrategia no ha encontrado ninguna coincidencia.")

        return resultado