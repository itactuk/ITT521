import socket

host = ""
puerto = 2224

try:
    s = socket.socket()
    s.bind((host, puerto))
    print("Enlazando el puerto: " + str(puerto))
    s.listen(5)
    while True:
        print("Esperando por conexiones")
        conn, address = s.accept()
        print("La conexión ha sido establecida! |" + " IP " + address[0] + " | Puerto" + str(address[1]))
        client_response = conn.recv(1024)
        # version (1 byte), tipo (1 byte) (1=req, 2= resp), comando, data
        # comandos: 1=date, 2= reverse, 3=download
        comando = client_response[2]
        reponse_header = b'\x01\x02'
        if comando == 0x01:  # fecha
            conn.send(reponse_header + b'\x01' + b'20200205')
            print("Fecha Request")
        elif comando == 0x02:  # inverso
            data = client_response[3:]
            conn.send(reponse_header + b'\x01' + data[::-1])
            print("Fecha Inverso")
        elif comando == 0x03:  # download
            conn.send(reponse_header + b'\x01')
            print("Download Request")
        else:
            conn.send(reponse_header + b'\x02')
            print("Unknown Request")
        conn.close()
        print("Conexion cerrada")
except socket.error as msg:
    print("Error: " + str(msg))
