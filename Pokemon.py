import json
import requests


# Make the GET request to the horoscope API
response = requests.get("https://api.pokemontcg.io/v2/cards/")
data = response.json()  # Convert the response to JSON

# Store the JSON data in a file
with open("pokemon.json", "w") as file:
    json.dump(data, file)

print("Data stored successfully!")