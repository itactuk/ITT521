import time

import ping3
import _thread

host = "google.com"


def imprime_resultado_ping(host):
    r = ping3.ping(host)
    if r is not None:
        print(f"{host} respondio en {r}s")

for i in range(1, 255):
    _thread.start_new_thread(imprime_resultado_ping, (f"192.168.77.{i}", ))
time.sleep(5)

# r = ping3.ping('google.com')  # Se necesita ser root o administrador
# print(r)

