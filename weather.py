import requests

# Tabella di decodifica dei codici meteo standard WMO in italiano
WMO_CODES = {
    0: "Cielo sereno",
    1: "Prevalentemente sereno",
    2: "Parzialmente nuvoloso",
    3: "Coperto",
    45: "Nebbia",
    48: "Nebbia con brina",
    51: "Pioggerella leggera",
    53: "Pioggerella moderata",
    55: "Pioggerella densa",
    61: "Pioggia debole",
    63: "Pioggia moderata",
    65: "Pioggia forte",
    71: "Neve debole",
    73: "Neve moderata",
    75: "Neve forte",
    80: "Rovesci di pioggia deboli",
    81: "Rovesci di pioggia moderati",
    82: "Rovesci di pioggia violenti",
    95: "Temporale",
}


def get_coordinates(city_name: str = "Milano") -> tuple[float, float, str]:
  """Trova latitudine e longitudine della città cercata."""
  geo_url = "https://geocoding-api.open-meteo.com/v1/search"
  params = {"name": city_name, "count": 1, "language": "it", "format": "json"}
  res = requests.get(geo_url, params=params, timeout=10)
  res.raise_for_status()
  data = res.json()

  if not data.get("results"):
    raise ValueError(f"Città '{city_name}' non trovata.")

  first = data["results"][0]
  resolved_name = f"{first.get('name')}, {first.get('admin1', '')} ({first.get('country', '')})"
  return first["latitude"], first["longitude"], resolved_name


def get_weather(city_name: str = "Milano") -> dict:
  """Scarica le condizioni attuali per la città specificata."""
  lat, lon, full_name = get_coordinates(city_name)

  weather_url = "https://api.open-meteo.com/v1/forecast"
  params = {
      "latitude": lat,
      "longitude": lon,
      "current": [
          "temperature_2m",
          "relative_humidity_2m",
          "apparent_temperature",
          "precipitation",
          "weather_code",
          "wind_speed_10m",
      ],
      "timezone": "auto",
  }
  res = requests.get(weather_url, params=params, timeout=10)
  res.raise_for_status()

  raw = res.json()
  current = raw.get("current", {})
  code = current.get("weather_code", 0)

  return {
      "città": full_name,
      "condizione": WMO_CODES.get(code, f"Codice meteo {code}"),
      "temperatura_reale": f"{current.get('temperature_2m')} °C",
      "temperatura_percepita": f"{current.get('apparent_temperature')} °C",
      "umidita": f"{current.get('relative_humidity_2m')} %",
      "pioggia": f"{current.get('precipitation')} mm",
      "vento": f"{current.get('wind_speed_10m')} km/h",
  }


if __name__ == "__main__":
  meteo_milano = get_weather("Milano")
  print("=== METEO MILANO IN TEMPO REALE ===")
  for chiave, valore in meteo_milano.items():
    print(f"{chiave.capitalize()}: {valore}")
