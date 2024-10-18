import os
import time
import logging, sys
import winsound

from datetime import datetime

h = [
    logging.FileHandler('./logs/log.log'), 
    logging.StreamHandler(stream=sys.stdout),
]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=h,
)

logger = logging.getLogger(__name__)

# Genera un pitido de 2000 Hz durante 1500 ms
def generar_pitido():   
    frecuencia=2000
    duracion=1500
    winsound.Beep(frecuencia, duracion)

def check_internet_connection():
    # Probando la conexión a internet intentando hacer ping a Google
    response = os.system("ping -n 1 google.com > nul 2>&1")
    return response == 0  # Retorna True si la conexión está activa, False si no

def main():
    internet_connected = True  # Inicialmente, asumimos que hay conexión

    # Imprimir un mensaje en la terminal
    print("Prueba de conexion a Internet Iniciada.")
    # Imprimir un mensaje en el archivo de log
    logger.info("Prueba de conexion a Internet Iniciada.")

    while True:
        time.sleep(1) 

        # Verifica la conexión a Internet
        if not check_internet_connection():
            if internet_connected:  # Solo registra si la conexión cambia a desconectado
                # Obtiene la hora actual en el formato deseado
                now = datetime.now()
                current_time = now.strftime('%H:%M:%S')
                print("Hora PERDIDA INTERNET ::: " + current_time)
                logger.info("Hora PERDIDA INTERNET ::: " + current_time)
                generar_pitido()
                internet_connected = False
        else:
            internet_connected = True 

if __name__ == "__main__":
    main()
