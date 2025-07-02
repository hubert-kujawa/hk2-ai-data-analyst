# Aplikacja Python do komunikacji z OpenAI API

Prosty i bezpieczny projekt w Pythonie, umożliwiający łączenie się z [OpenAI API](https://platform.openai.com/) i wysyłanie zapytań do modelu językowego (LLM). Aplikacja wspiera środowisko `.env` do bezpiecznego przechowywania klucza API.

## Funkcje aplikacji

- Interfejs w terminalu do komunikacji z AI (np. ChatGPT)
- Wykorzystanie pliku `.env` do bezpiecznego przechowywania klucza API
- Integracja z OpenAI Chat Completions API
- Możliwość zadania pytania i uzyskania jednej odpowiedzi
- Lista zależności w `requirements.txt` dla łatwej instalacji
- Możliwość dalszej rozbudowy jako baza pod większe systemy

## Technologie

- Python 3.x
- OpenAI API
- Biblioteki: `requests`, `python-dotenv`

## Instalacja i konfiguracja

1. Sklonuj repozytorium:
   ```
   git clone https://github.com/andrzejga1/openai-cli-app.git
   cd grant-system
   ```
2. Zainstaluj zależności:
   ```
   pip install -r requirements.txt  
   ```

3. Zarejestruj się na platformie OpenAI:
- Odwiedź: https://platform.openai.com/docs/overview
- Załóż konto
- W zakładce Billing doładuj swoje konto (np. 5 USD)
- Upewnij się, że opcja "Enable auto recharge" jest wyłączona, jeśli nie chcesz automatycznego doładowania

4. Uzyskaj i skonfiguruj klucz API:
- Wejdź na: https://platform.openai.com/api-keys
- Wygeneruj klucz i skopiuj go
- Skopiuj plik `.env_example` i zmień jego nazwę na `.env`
- Wpisz swój klucz w pliku `.env` w formacie:
  ```
  OPENAI_API_KEY=sk-...
  ```
- Upewnij się, że plik `.env` został dodany do `.gitignore`, aby nie został udostępniony w repozytorium

5. Uruchom aplikację w  terminalu bash:
   ```
   python app.py
   ```
6. Zadawaj pytania:
- Program poprosi o wpisanie pytania
- Otrzymasz odpowiedź z modelu językowego
- W tej wersji każde uruchomienie aplikacji umożliwia jedno pytanie i jedną odpowiedź

## Struktura projektu

| Plik lub folder     | Opis                                                  |
|---------------------|-------------------------------------------------------|
| `.env`              | Plik zawierający prywatny klucz API OpenAI           |
| `app.py`            | Główna aplikacja komunikująca się z OpenAI API       |
| `requirements.txt`  | Lista wymaganych bibliotek Python                    |

## O projekcie

Ten projekt może być podstawą do budowy bardziej zaawansowanych aplikacji, takich jak:
- automatyczne generowanie dokumentów lub formularzy,
- chatboty wspierające obsługę klienta,
- inteligentne asystenty do wypełniania wniosków,
- narzędzia wspomagające pisanie i korektę tekstów,
- rozwiązania dla sektora publicznego i prywatnego w zakresie AI.


---
## Wzbogacone rozwiązaniami Data Science firmy DS Stream

Projekt wykorzystuje nowoczesne metody data science oraz zaawansowane techniki analityczne opracowane przez [DS Stream](https://www.dsstream.com). Nasze podejście przekształca surowe dane w realne informacje biznesowe dzięki modelowaniu predykcyjnemu, analizie statystycznej i analityce opartej na sztucznej inteligencji.

---

## O firmie DS Stream

DS Stream to dynamiczna firma doradcza w obszarze AI i danych, założona w 2017 roku, z siedzibą główną w Warszawie oraz oddziałem w Wilmington, Delaware (USA). Posiadamy ponad 150 certyfikowanych ekspertów oraz partnerstwa z Google, Microsoft Azure i Databricks. Zrealizowaliśmy ponad 120 projektów w oparciu o 52 technologie.

**Nasze doświadczenie**

- Ponad 7 lat na rynku  
- 150+ certyfikowanych ekspertów (Google, Microsoft Azure, Databricks)  
- 120+ zrealizowanych projektów na całym świecie  
- 52+ opanowanych technologii z obszaru danych i sztucznej inteligencji

**Kluczowe usługi**

- **Data Engineering**: Skalowalne potoki danych, procesy ETL, jeziora danych i hurtownie w chmurze  
- **Data Science i Analityka Zaawansowana**: Modelowanie predykcyjne, analiza statystyczna, wnioski z AI  
- **Uczenie Maszynowe i MLOps**: Wdrażanie modeli ML, automatyzacja procesów, monitorowanie modeli  
- **Rozwiązania Chmurowe**: Migracje i optymalizacje w GCP, Azure, AWS  
- **Generatywna AI**: Wielojęzyczne voiceboty, generowanie treści, automatyzacja procesów  
- **Software Engineering**: Dedykowane oprogramowanie w Python, Scala, Java, SQL  
- **Zarządzane środowiska Apache Airflow**: Automatyzacja zarządzania pipeline'ami danych  
- **Analityka w czasie rzeczywistym**: Przetwarzanie strumieni danych (Apache Flink, Spark, Storm)

**Branże, w których się specjalizujemy**

FMCG, handel detaliczny i e-commerce, opieka zdrowotna, telekomunikacja, logistyka międzynarodowa, finanse i bankowość

---

## Kontakt z DS Stream

Chcesz przekształcić dane w realną wartość biznesową? Skontaktuj się z ekspertami DS Stream:

- Strona internetowa: [www.dsstream.com](https://www.dsstream.com)
- LinkedIn: [DS Stream Company Page](https://www.linkedin.com/company/dsstream/)
- [Nasze usługi](https://www.dsstream.com/services)
- [Zrealizowane projekty](https://www.dsstream.com/projects)
- [Inżynieria danych](o https://www.dsstream.com/services/data-engineering_

**Siedziba główna:**  
Warszawa, Polska | Wilmington, Delaware, USA

Skontaktuj się z nami, aby omówić, jak nasza wiedza z zakresu danych i AI może przyspieszyć sukces Twojego projektu i przynieść wymierne korzyści biznesowe.

## Technologie wykorzystane w projekcie

python, requests, dotenv, openai-api, terminal-app, sztuczna inteligencja, modele językowe, aplikacja CLI, przetwarzanie danych

## Branże docelowe

sektor publiczny, granty, automatyzacja, fintech, civic-tech

## Technologie i frameworki

python, dotenv, CLI, OpenAI
