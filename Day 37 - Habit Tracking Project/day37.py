# ----- PIXELA ----- #
import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "alex25"
TOKEN = "***"
GRAPH_ID = "graph1"


# ----- CREATE A USER ----- #
parameters = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)


# ----- CREATE A GRAPH ----- #
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
parameters2 = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=parameters2, headers=headers)
# print(response.text)


# ----- CREATE A PIXEL ----- #
pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")
print(today)

parameters3 = {
    "date": today,
    "quantity": input("How many kilometers did you cycle today"),
}

# response = requests.post(url=pixel_endpoint, json=parameters3, headers=headers)
# print(response.text)


# ----- UPDATE A PIXEL ----- #
parameters4 = {
    "quantity": "36.7",
}

update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# response = requests.put(url=update_endpoint, json=parameters4, headers=headers)
# print(response.text)


# ----- DELETE A PIXEL -----
delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# response = requests.delete(url=update_endpoint, json=parameters4, headers=headers)
# print(response.text)