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

    # 2. Corregido: Ahora tiene su sangría (espacios) para estar dentro de la clase
    def recomendar(self) -> object:
        """
        Conecta el Decorator, la Sesion y el Strategy para devolver una recomendación.
        """

        if self._catalogo_activo is None:
            print("Error: Falta el catálogo.")
            return None

        if self._estrategia is None:
            print("Error: Falta la estrategia de búsqueda.")
            return None
            
        if self._sesion_actual is None:
            print("Error: Falta iniciar la sesión.")
            return None

        # 2. PATRÓN DECORATOR: saca la lista catalogo
        lista_catalogo = self._catalogo_activo.obtener_elementos()

        # 3. PATRÓN CHAIN OF RESP: Saca los calculos
        diccionario_medias = self._sesion_actual.get_media_sonora()

        # 4. PATRÓN STRATEGY: Le pasamos la lista y las medias al cartucho de búsqueda
        resultado = self._estrategia.buscar(lista_catalogo, diccionario_medias)

        return resultado