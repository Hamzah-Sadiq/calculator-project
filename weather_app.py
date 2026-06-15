import requests

city = input("City ka naam enter karo: ")

api_key = "8c9a2ab0e2646c819d0fb9212cfdc3f5"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print("\n🌦 Weather Report")
print("------------------")

print("City:", data["name"])
print("Country:", data["sys"]["country"])
print("Temperature:", data["main"]["temp"], "°C")
print("Feels Like:", data["main"]["feels_like"], "°C")
print("Humidity:", data["main"]["humidity"], "%")
print("Weather:", data["weather"][0]["description"])
print("Wind Speed:", data["wind"]["speed"], "m/s")