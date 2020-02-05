import requests
url = 'http://192.168.77.66:8000/'

r = requests.get(url)

print(r.content)
