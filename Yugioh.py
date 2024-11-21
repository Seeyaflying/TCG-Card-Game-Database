import requests
import json


# Make the GET request to the horoscope API
response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
data = response.json()  # Convert the response to JSON

# Store the JSON data in a file
with open("yugioh.json", "w") as file:
    json.dump(data, file)

print("Data stored successfully!")

