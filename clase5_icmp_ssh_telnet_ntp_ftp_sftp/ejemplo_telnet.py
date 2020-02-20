import time
from telnetlib import Telnet

with Telnet('192.168.56.1', 5004) as tn:
    # La ip de arriba es la ip y el puerto que GNS3 muestra en el panel superior izquierdo
    print(tn.write(b"show ip\r\n"))
    time.sleep(5)
    print(tn.read_very_eager())
    print(tn.read_all())

with Telnet('192.168.56.1', 5004) as tn:
    tn.interact()

