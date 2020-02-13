import unittest
from scapy.all import *
from scapy.layers.inet import TCP
from scapy.layers.l2 import Ether

from clase4_disectando_paquetes.disector_netpro_scapy import NetProRequest, NetPro


class TestSuma(unittest.TestCase):
    def test_req_fecha(self):
        escaped_string = b"\x00\x0c\x29\x1d\x94\x72\x00\x0b\xfd\x44\x50\x00\x08\x00\x45\x00" \
                    b"\x00\x2b\x06\xaf\x40\x00\x7e\x06\x79\x56\x0a\x64\x64\x79\xc0\xa8" \
                    b"\x4d\x42\xc4\x83\x08\xb0\xef\x35\x27\x9b\x38\xb7\xc3\xcd\x50\x18" \
                    b"\x18\x03\x38\x74\x00\x00\x01\x01\x01\x1d\x70\xc0"


        p = Ether(escaped_string)

        self.assertTrue(TCP in p, "packet has tcp")
        self.assertTrue(NetProRequest in p, "packet has NetProRequest layer")
        self.assertTrue(isinstance(p[TCP].payload, NetPro), "packet has NetProRequest layer")
        self.assertEqual(p[NetPro].version, 1)
        self.assertEqual(p[NetPro].tipo, 1)
        self.assertEqual(p[NetProRequest].comando, 1)
        self.assertEqual(p[NetProRequest].data, b"")

