#pip install plyer
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(title = "Alerta", message = 'Hora de break')
        time.sleep(3600)

