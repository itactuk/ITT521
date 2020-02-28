import requests

url = "http://quotes.toscrape.com/"

inicio_texto = '<span class="text" itemprop="text">'
fin_texto = '</span>'

lista_citas = []

res = requests.get(url)
contenido = res.content.decode('utf-8')

# print(contenido)
while inicio_texto in contenido:
    i1 = contenido.find(inicio_texto)
    contenido = contenido[i1+ len(inicio_texto):]
    i2 = contenido.find(fin_texto)
    cita = contenido[:i2]
    lista_citas.append(cita)

print(lista_citas)
for c in lista_citas:
    print(c)
