import requests
from datetime import datetime

TOKEN = "asdadadwehjrnerjrvnerfiufhweufhweiufwenc"
USERNAME = "ferra"
GRAPH_ID = "graph1"

# resquests.post()
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
"""
response = requests.post(url=pixela_endpoint, json=user_params) # es un como un jason porque es un diccionario
print(response.text)
"""
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Python dedication",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN # forma de autenticacion
}
"""
response = requests.post(url=graph_endpoint, json=graph_params, headers=headers) # por seguridad se usan estos headers para que no se vea en el buscador (headers es un kwards, key optional arguments)
print(response.text)
# para probar el grafico "https://pixe.la/v1/users/ferra/graphs/graph1.html"
"""
# post a pixel

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
yesterday = datetime(year=2024, month=4, day=16)
print(today.strftime("%Y%m%d"))

post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": str(input("How much time did you spent studying python today?")),
}

response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers) # por seguridad se usan estos headers para que no se vea en el buscador (headers es un kwards, key optional arguments)
print(response.text)


# requests.put()

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime("%Y%m%d")}"

update_pixel_params = {
    "quantity": "8.5",
    "optionalData": "{\"Prueba\":\"prueba\"}",
}

"""
response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers) # por seguridad se usan estos headers para que no se vea en el buscador (headers es un kwards, key optional arguments)
print(response.text)
"""
# requests.delete()

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


"""
response = requests.delete(url=delete_pixel_endpoint, headers=headers) # por seguridad se usan estos headers para que no se vea en el buscador (headers es un kwards, key optional arguments)
print(response.text)
"""
