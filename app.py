import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Błąd: Nie znaleziono klucza OPENAI_API_KEY w środowisku.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def zapytaj_model(pytanie):
    try:
        odpowiedz = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Jesteś pomocnym asystentem AI."},
                {"role": "user", "content": pytanie}
            ]
        )
        return odpowiedz.choices[0].message.content
    except Exception as e:
        print(f"Błąd API: {e}")
        sys.exit(1)

def main():
    print("Witaj! Zadaj pytanie lub wpisz 'exit', aby zakończyć.")
    while True:
        pytanie = input("\nTwoje pytanie: ").strip()
        if pytanie.lower() in ("exit", "quit", "q"):
            print("Do zobaczenia!")
            break

        odpowiedz = zapytaj_model(pytanie)
        print("\n--- Odpowiedź AI ---")
        print(odpowiedz)

if __name__ == "__main__":
    main()
