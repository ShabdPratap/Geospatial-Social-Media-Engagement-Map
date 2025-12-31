import pandas as pd
import requests
import time

# Load city-level data
df = pd.read_csv("city_level_engagement.csv")

latitudes = []
longitudes = []

for city in df["City"]:
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "Geospatial-Tableau-Assignment"
    }

    response = requests.get(url, params=params, headers=headers).json()

    if response:
        latitudes.append(response[0]["lat"])
        longitudes.append(response[0]["lon"])
    else:
        latitudes.append(None)
        longitudes.append(None)

    time.sleep(1)  # Respect API rate limits

df["latitude"] = latitudes
df["longitude"] = longitudes

df.to_csv("city_level_engagement_geocoded.csv", index=False)

print("Geocoding completed successfully")