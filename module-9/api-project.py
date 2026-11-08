
import requests

# Request spell data from the D&D 5e API.
url = "https://www.dnd5eapi.co/api/2014/spells/fireball"
response = requests.get(url, timeout=15)

# Test the API connection.
print("Status code:", response.status_code)

# Display the raw API response.
print("\nRaw response:")
print(response.text)

# Display selected spell details in a readable format.
if response.status_code == 200:
    spell = response.json()

    print("\nFormatted response:")
    print(f"Spell: {spell['name']}")
    print(f"Level: {spell['level']}")
    print(f"School: {spell['school']['name']}")
    print(f"Casting Time: {spell['casting_time']}")
    print(f"Range: {spell['range']}")
    print(f"Duration: {spell['duration']}")
else:
    print("Request failed.")