import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Błąd: Brak klucza OPENAI_API_KEY w zmiennych środowiskowych.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def ask_ai(question):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Jesteś pomocnym asystentem AI."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Błąd podczas wywołania API: {e}")
        sys.exit(1)

def main():
    print("Witaj! Zadaj pytanie lub wpisz 'exit', aby zakończyć.")
    while True:
        question = input("\nTwoje pytanie: ").strip()
        if question.lower() in ("exit", "quit", "q"):
            print("Do zobaczenia!")
            break

        answer = ask_ai(question)
        print("\n--- Odpowiedź AI ---")
        print(answer)

if __name__ == "__main__":
    main()