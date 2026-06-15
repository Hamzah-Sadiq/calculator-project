import requests

response = requests.get("https://api.agify.io?name=ali")

data = response.json()

print(data)

