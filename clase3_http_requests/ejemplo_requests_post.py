import requests
url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=mykeyhere'
payload = "kfladsjfds"
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=payload, headers=headers)

print(r)
