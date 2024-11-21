import requests
import json


# Make the GET request to the horoscope API
response = requests.get("https://digimoncard.io/api-public/getAllCards.php?sort=name&series=Digimon Card Game&sortdirection=asc")
data = response.json()  # Convert the response to JSON

# Store the JSON data in a file
with open("digimon.json", "w") as file:
    json.dump(data, file)

print("Data stored successfully!")
