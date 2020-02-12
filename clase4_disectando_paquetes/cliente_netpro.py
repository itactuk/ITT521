import socket

# version (1 byte), tipo (1 byte) (1=req, 2= resp), comando, data
# comandos: 1=date, 2= reverse, 3=download

host = '192.168.77.66'
puerto = 2224

req_header = b'\x01\x01'


def main():
    enviar_fecha_req()
    enviar_reverse_req()
    enviar_descargar_req()
    enviar_invalido_req()


def enviar_fecha_req():
    s = socket.socket()
    s.connect((host, puerto))
    s.send(req_header + b'\x01')
    data = s.recv(1024)
    s.close()
    print(data)


def enviar_reverse_req(data=b"hola"):
    s = socket.socket()
    s.connect((host, puerto))
    s.send(req_header + b'\x02' + data)
    data = s.recv(1024)
    s.close()
    print(data)


def enviar_descargar_req(data=b"http://midescarga.com/"):
    s = socket.socket()
    s.connect((host, puerto))
    s.send(req_header + b'\x03' + data)
    data = s.recv(1024)
    s.close()
    print(data)


def enviar_invalido_req():
    s = socket.socket()
    s.connect((host, puerto))
    s.send(req_header + b'\x08')
    data = s.recv(1024)
    s.close()
    print(data)


if __name__ == '__main__':
    main()
