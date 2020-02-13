from scapy.all import *
from scapy.layers.inet import TCP


def main():
    ruta_pcap = "prueba.pcap"
    paquetes = rdpcap(ruta_pcap)
    for p in paquetes:
        if TCP in p and (p[TCP].sport == 2224 or p[TCP].dport == 2224):
            if (len(p[TCP].payload)>0):
                print(p.summary())


class NetPro(Packet):
    fields_desc = [
        XByteField("version", 0),  # valor por defecto 1 como hexadecimal
        ByteEnumField("tipo", 0, {1: "PETICION", 2: "RESPUESTA"})
    ]

    def guess_payload_class(self, payload):
        if self.tipo == 1:
            return NetProRequest
        elif self.tipo == 2:
            return NetProResponse
        else:
            return Packet.guess_payload_class(self, payload)


class NetProRequest(Packet):
    fields_desc = [
        ByteEnumField("comando", 0, {1: "FECHA", 2: "INVERSO", 3: "DESCARGA"}),
        StrField("data", "")
    ]


class NetProResponse(Packet):
    fields_desc = [
        ByteEnumField("estado", 0, {1: "EXITO", 2: "FALLO"}),
        StrField("data", "")
    ]


bind_layers(TCP, NetPro, sport=2224)
bind_layers(TCP, NetPro, dport=2224)

if __name__ == '__main__':
    main()
