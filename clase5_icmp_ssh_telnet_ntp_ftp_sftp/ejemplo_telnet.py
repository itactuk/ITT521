import time
from telnetlib import Telnet

with Telnet('192.168.56.1', 5004) as tn:
    print(tn.write(b"show ip\r\n"))
    time.sleep(5)
    print(tn.read_very_eager())
    print(tn.read_all())

with Telnet('192.168.56.1', 5004) as tn:
    tn.interact()

