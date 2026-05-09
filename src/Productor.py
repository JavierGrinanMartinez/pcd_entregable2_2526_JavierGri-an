import json
import time
from kafka import KafkaProducer

def iniciar_productor():
    productor = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    canciones_escuchadas = ["Jesucristo Garcia", "So payaso", "Fiesta pagana"]
    
    for titulo in canciones_escuchadas:
        mensaje = {
            "id_usuario": 1,
            "titulo_cancion": titulo,
            "accion": "PLAY"
        }
        productor.send('historial_escuchas', value=mensaje)
        time.sleep(3)

    productor.flush()

if __name__ == "__main__":
    iniciar_productor()