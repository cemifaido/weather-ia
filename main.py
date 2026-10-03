import sys
from weather import get_weather


def main():
  citta = "Milano"
  print(f"Recupero dati meteo per {citta}...")

  try:
    dati = get_weather(citta)
    print("\n--- RISULTATO METEO ---")
    for chiave, valore in dati.items():
      print(f"{chiave.capitalize()}: {valore}")
    print("------------------------")

  except Exception as e:
    print(f"Errore: {e}", file=sys.stderr)


if __name__ == "__main__":
  main()
