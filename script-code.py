# Importamos las herramientas necesarias
import pygame  # Reproductor de música
import psutil
import time
import psutil
import time
from datetime import datetime

# Configuración inicial

pygame.mixer.init()
APPS_MONITOREADAS = {'firefox.exe','Code.exe'}
INTERVALO = 1  # Segundos entre chequeos
ARCHIVO_LOG = 'monitor_ventanas.log'


def escribir_log(mensaje):
    """Registra eventos con timestamp en un archivo"""
    with open(ARCHIVO_LOG, 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] {mensaje}\n")

def monitorear_ventanas():
    estado_anterior = set()
    musica_en_curso = False
    print(f"Iniciando monitor 24/7 para: {', '.join(APPS_MONITOREADAS)}")
    escribir_log(f"INICIO - Monitor comenzado para: {APPS_MONITOREADAS}")
    
    try:
        while True:
            # Obtener procesos actuales (solo los que nos interesan)
            estado_actual = set()
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] in APPS_MONITOREADAS:
                    estado_actual.add(proc.info['name'])
            
            # Detectar cambios
            nuevas = estado_actual - estado_anterior
            cerradas = estado_anterior - estado_actual
            
            # Registrar aperturas
            for app in nuevas:
                mensaje = f"APP ABIERTA: {app}"
                print(mensaje)
                escribir_log(mensaje)
                
                print(len(estado_actual)) 
                if not pygame.mixer.music.get_busy() and not musica_en_curso:
                    pygame.mixer.music.load("eye_of_the_tiger.mp3")
                    pygame.mixer.music.play()
                    musica_en_curso = True
                    print("▶️ Reproduciendo música por primera vez")
                elif pygame.mixer.music.get_busy():
                    print("🔊 La música ya está sonando (no se reproduce de nuevo)")
                else:
                    print("⏹️ La música ya terminó")                    
                            #time.sleep(20)  # Reproduce solo 5 segundos
                    pygame.mixer.music.stop()

            # Registrar cierres
            for app in cerradas:
                mensaje = f"APPS CERRADA: {app}"
                print(mensaje)
                escribir_log(mensaje)
                 # si nuevas esta vacia
                print(len(estado_actual))
                if len(estado_actual) == 0:
                    pygame.mixer.music.stop()     
                    musica_en_curso = False     # Actualizar estado
            estado_anterior = estado_actual

            time.sleep(INTERVALO)
            
    except KeyboardInterrupt:
        escribir_log("MONITOR DETENIDO (por usuario)")
        print("\nMonitor detenido manualmente")
    except Exception as e:
        escribir_log(f"ERROR: {str(e)}")
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    monitorear_ventanas()

