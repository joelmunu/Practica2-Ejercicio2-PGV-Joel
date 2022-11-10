import platform
import os

host = input("Introduce una IP o nombre de dominio al que hacer ping: ")

if (platform.system() == "Windows"):
    os.system(f'ping { host }')

elif (platform.system() == 'Linux' or platform.system() == 'Darwin'):
    # https://es.itsfoss.com/comando-ping-linux/
    os.system(f"ping -c 4 { host }")

else:
    print('Tu S.O. no es compatible con este programa')