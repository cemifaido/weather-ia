import sys
from ai_analyst import build_weather_prompt
from weather import get_weather


def main():
  print("Recupero dati meteo in corso...")
  try:
    # Coordinate di default (Milano: lat 45.4642, lon 9.1900)
    weather_data = get_weather(latitude=45.4642, longitude=9.1900)
    prompt = build_weather_prompt(weather_data, city_name="Milano")

    print("\n=== PROMPT PRONTO PER L'AI ===")
    print(prompt)
    print("==============================")

  except Exception as e:
    print(f"Errore durante l'esecuzione: {e}", file=sys.stderr)


if __name__ == "__main__":
  main()
