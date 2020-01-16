#!/usr/bin/python

import sys


if len(sys.argv) < 3:
 print("Error. Syntaxis: calcula.py <n1> <n2>")
else:
 a = int(sys.argv[1])
 b = int(sys.argv[2])

print("El resultado es:" + str(a + b))

