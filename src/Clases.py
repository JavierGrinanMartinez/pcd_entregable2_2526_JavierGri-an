class Fecha:
    def __init__(self, dia: int, mes: int, anio: int):
        self.dia = dia
        self.mes = mes
        self.año = año


    def __eq__(self, otra: "Fecha"):
        return self.año == otra.año and self.mes == otra.mes and self.dia == otra.dia


    def __lt__(self, otra: 'Fecha'):

        if self.año != otra.año:
            return self.anio < otra.anio

        elif self.mes != otra.mes:
            return self.mes < otra.mes

        else:
            return self.dia < otra.dia
            

class Cancion:
    def __init__(self, id_cancion:int, titulo:str, fecha_creacion: Fecha, atributos_sonoros:dict, atributos_sentimentales:dict):
        self._id_cancion = id_cancion
        self._titulo = titulo
        self._fecha_creacion = fecha_creacion
        self._atributos_sonoros = atributos_sonoros
        self._atributos_sentimentales = atributos_sentimentales

    def __str__(self): #esto para que luego poder ordenar alfabeticamente
        return self.get_titulo()

    # Getters
    def get_id_cancion(self): 
        return self._id_cancion
        
    def get_titulo(self): 
        return self._titulo
        
    def get_fecha(self): #todos los metodo get_fecha son asi para poder luego ordenarlos llamando a ese metodo, por eso mismo son toods iguales
        return self._fecha_creacion
        
    def get_atributos_sonoros(self): 
        return self._atributos_sonoros
        
    def get_atributos_sentimentales(self): 
        return self._atributos_sentimentales

    # Setters
    def set_id_cancion(self, id_cancion): 
        self._id_cancion = id_cancion
        
    def set_titulo(self, titulo): 
        self._titulo = titulo
        
    def set_fecha_creacion(self, fecha_creacion): 
        self._fecha_creacion = fecha_creacion
        
    def set_atributos_sonoros(self, atributos_sonoros): 
        self._atributos_sonoros = atributos_sonoros
        
    def set_atributos_sentimentales(self, atributos_sentimentales): 
        self._atributos_sentimentales = atributos_sentimentales

class Cantante:
    def __init__(self, nombre:str, fecha_nacimiento:Fecha, canciones=None):
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._canciones = canciones if canciones is not None else []

    def __str__(self): #esto para que luego poder ordenar alfabeticamente
        return self.get_nombre()
    # Getters
    def get_nombre(self): 
        return self._nombre
        
    def get_fecha(self): 
        return self._fecha_nacimiento
        
    def get_canciones(self): 
        return self._canciones

    # Setters
    def set_nombre(self, nombre:str): 
        self._nombre = nombre
        
    def set_fecha_nacimiento(self, fecha_nacimiento:int): 
        self._fecha_nacimiento = fecha_nacimiento
        

    #metodos
    def agregar_cancion(self,cancion:Cancion):
        self._canciones.append(cancion)

    def calcular_media_sonora(self) -> dict:
        if not self._canciones:
            return {}
            
        # Tomamos los atributos de la primera canción y aplicamos tu fórmula directa
        atributos = self._canciones[0].get_atributos_sonoros()
        media_general = sum(atributos.values()) / len(atributos)
        
        return {"media_general": media_general}

    def calcular_media_sentimental(self) -> dict:
        if not self._canciones:
            return {}
            
        # Misma lógica para los atributos sentimentales
        atributos = self._canciones[0].get_atributos_sentimentales()
        media_general = sum(atributos.values()) / len(atributos)
        
        return {"media_general": media_general}

class Playlist:
    def __init__(self, titulo:str, fecha_creacion:Fecha, canciones=None):
        self._titulo = titulo
        self._fecha_creacion = fecha_creacion
        self._canciones = canciones if canciones is not None else []

    def __str__(self): #esto para que luego poder ordenar alfabeticamente
        return self.get_titulo()
    # Getters
    def get_titulo(self): 
        return self._titulo
        
    def get_fecha(self): 
        return self._fecha_creacion
        
    def get_canciones(self): 
        return self._canciones

    # Setters
    def set_titulo(self, titulo:str): 
        self._titulo = titulo
        
    def set_fecha_creacion(self, fecha_creacion:int): 
        self._fecha_creacion = fecha_creacion
        
    #metodos

    def agregar_cancion(self,cancion:Cancion):
        self._canciones.append(cancion)

    def calcular_media_sonora(self) -> dict:
        if not self._canciones:
            return {}
            
        atributos = self._canciones[0].get_atributos_sonoros()
        media_general = sum(atributos.values()) / len(atributos)
        
        return {"media_general": media_general}

    def calcular_media_sentimental(self) -> dict:
        if not self._canciones:
            return {}
            
        atributos = self._canciones[0].get_atributos_sentimentales()
        media_general = sum(atributos.values()) / len(atributos)
        
        return {"media_general": media_general}

class Sesion:
    def __init__(self):
        self._canciones_escuchadas = []
        self._media_sonora = {}
        self._desviacion_sonora = {}
        self._media_sentimental = {}
        self._desviacion_sentimental = {}

    # Getters
    def get_canciones_escuchadas(self): 
        return self._canciones_escuchadas
        
    def get_media_sonora(self): 
        return self._media_sonora
        
    def get_desviacion_sonora(self): 
        return self._desviacion_sonora
        
    def get_media_sentimental(self): 
        return self._media_sentimental
        
    def get_desviacion_sentimental(self): 
        return self._desviacion_sentimental

    # Setters
    def set_canciones_escuchadas(self, canciones): 
        self._canciones_escuchadas = canciones
        
    def set_media_sonora(self, media): 
        self._media_sonora = media
        
    def set_desviacion_sonora(self, desviacion): 
        self._desviacion_sonora = desviacion
        
    def set_media_sentimental(self, media): 
        self._media_sentimental = media
        
    def set_desviacion_sentimental(self, desviacion): 
        self._desviacion_sentimental = desviacion

    # metodos

    def agregar_cancion(self, cancion: Cancion):
            self._canciones_escuchadas.append(cancion)