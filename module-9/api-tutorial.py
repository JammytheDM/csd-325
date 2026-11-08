
import requests

# Request astronaut data from the API.
url = "https://ll.thespacedevs.com/2.2.0/astronaut/"
response = requests.get(url, timeout=20)

print("Status code:", response.status_code)

# Convert the JSON response into Python data.
data = response.json()

# Display a formatted list of astronauts.
print(f"Total astronaut records: {data['count']}")
print("\nAstronauts:")

for astronaut in data["results"]:
    name = astronaut["name"]
    nationality = astronaut.get("nationality", "Unknown")
    status = astronaut.get("status", {}).get("name", "Unknown")

    print(f"{name} | Nationality: {nationality} | Status: {status}")