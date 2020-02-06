import socket

# version (1 byte), tipo (1 byte) (1=req, 2= resp), comando, data
# comandos: 1=date, 2= reverse, 3=download

s = socket.socket()
host = '127.0.0.1'
puerto = 2222

req_header = b'\x01\x01'

s.connect((host, puerto))


def main():
    enviar_invalido_req()


def enviar_fecha_req():
    s.send(req_header + b'\x01')
    data = s.recv(1024)
    print(data)


def enviar_reverse_req(data=b"hola"):
    s.send(req_header + b'\x02' + data)
    data = s.recv(1024)
    print(data)


def enviar_descargar_req(data=b"http://midescarga.com/"):
    s.send(req_header + b'\x03' + data)
    data = s.recv(1024)
    print(data)


def enviar_invalido_req():
    s.send(req_header + b'\x08')
    data = s.recv(1024)
    print(data)


if __name__ == '__main__':
    main()
