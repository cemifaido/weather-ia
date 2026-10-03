
import requests


def get_weather(latitude: float = 45.4642, longitude: float = 9.1900) -> dict:
  """Recupera le condizioni meteo attuali da Open-Meteo."""
  url = "https://api.open-meteo.com/v1/forecast"
  params = {
      "latitude": latitude,
      "longitude": longitude,
      "current": [
          "temperature_2m",
          "relative_humidity_2m",
          "precipitation",
          "wind_speed_10m",
      ],
      "timezone": "auto",
  }

  response = requests.get(url, params=params, timeout=10)
  response.raise_for_status()
  return response.json()


if __name__ == "__main__":
  data = get_weather()
  current = data.get("current", {})
  print("--- METEO ATTUALE ---")
  print(f"Temperatura: {current.get('temperature_2m')} °C")
  print(f"Umidità: {current.get('relative_humidity_2m')} %")
  print(f"Precipitazioni: {current.get('precipitation')} mm")
  print(f"Vento: {current.get('wind_speed_10m')} km/h")
