import json


def build_weather_prompt(weather_data: dict, city_name: str = "Milano") -> str:
  """Costruisce il prompt da inviare all'intelligenza artificiale."""
  current = weather_data.get("current", {})

  summary = {
      "city": city_name,
      "temperature_c": current.get("temperature_2m"),
      "humidity_pct": current.get("relative_humidity_2m"),
      "precipitation_mm": current.get("precipitation"),
      "wind_speed_kmh": current.get("wind_speed_10m"),
  }

  prompt = f"""
Sei un meteorologo e assistente personale. Analizza i dati meteo attuali per {city_name}:
{json.dumps(summary, indent=2, ensure_ascii=False)}

Fornisci:
1. Una sintesi chiara e discorsiva della situazione attuale (2-3 frasi).
2. Consigli pratici su abbigliamento e attività all'aperto.
3. Eventuali accortezze o avvisi (es. pioggia imminente, vento fastidioso, umidità elevata).
"""
  return prompt.strip()
