import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(city: str) -> str:
    # Get latitude and longitude
    geo_response = requests.get(
        GEOCODING_URL,
        params={
            "name": city,
            "count": 1
        },
        timeout=10
    )

    geo_data = geo_response.json()

    if "results" not in geo_data:
        return f"Could not find city: {city}"

    location = geo_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    # Get current weather
    weather_response = requests.get(
        WEATHER_URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m"
        },
        timeout=10
    )

    weather_data = weather_response.json()["current"]

    return (
        f"Weather in {city}\n"
        f"Temperature: {weather_data['temperature_2m']}°C\n"
        f"Wind Speed: {weather_data['wind_speed_10m']} km/h"
    )