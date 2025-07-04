import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Załaduj klucz API z pliku .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Błąd: Klucz OPENAI_API_KEY nie został znaleziony w zmiennych środowiskowych.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def zapytaj_ai(pytanie):
    try:
        odpowiedz = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Jesteś pomocnym asystentem AI odpowiadającym na pytania."},
                {"role": "user", "content": pytanie}
            ]
        )
        return odpowiedz.choices[0].message.content
    except Exception as e:
        print(f"Błąd podczas komunikacji z API OpenAI: {e}")
        sys.exit(1)

def main():
    print("Witaj! Wpisz pytanie, na które chcesz uzyskać odpowiedź. Aby zakończyć, wpisz 'exit'.")
    while True:
        pytanie = input("\nTwoje pytanie: ").strip()
        if pytanie.lower() in ("exit", "quit", "q"):
            print("Koniec działania programu. Do zobaczenia!")
            break

        wynik = zapytaj_ai(pytanie)
        print("\n--- Odpowiedź AI ---")
        print(wynik)

if __name__ == "__main__":
    main()
