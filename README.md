# Konsola Python do interakcji z OpenAI API

To prosty i bezpieczny projekt w Pythonie, który pozwala na komunikację z [OpenAI API](https://platform.openai.com/) i przesyłanie zapytań do modeli językowych. Aplikacja wykorzystuje plik `.env` do ochrony Twojego klucza API.

## Co potrafi aplikacja?

- Terminalowy interfejs do zadawania pytań i otrzymywania odpowiedzi od AI (np. ChatGPT)  
- Zarządzanie kluczem API za pomocą pliku `.env`  
- Wykorzystanie OpenAI Chat Completion API do generowania odpowiedzi  
- Obsługa pojedynczych zapytań z natychmiastową odpowiedzią  
- Wygodna instalacja dzięki listy bibliotek w `requirements.txt`  
- Elastyczna baza do dalszego rozwoju i integracji w większe projekty  

## Technologie i narzędzia

- Python 3.x  
- OpenAI API  
- Kluczowe biblioteki: `openai`, `python-dotenv`  

## Jak zainstalować i uruchomić?

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/mkarasds/ds-ai-data-analyst.git
   cd ds-ai-data-analyst
   ```
2. Zainstaluj niezbędne pakiety:
   ```bash
   pip install -r requirements.txt
   ```
3. Załóż konto na platformie OpenAI, jeśli jeszcze tego nie zrobiłeś:
   - Odwiedź https://platform.openai.com/signup  
   - Skonfiguruj sposób płatności i limity wykorzystania  
4. Uzyskaj swój klucz API:
   - Przejdź do https://platform.openai.com/api-keys  
   - Wygeneruj nowy klucz i skopiuj go  
5. Stwórz plik `.env` w katalogu projektu i dodaj do niego:
   ```
   OPENAI_API_KEY=twój_klucz_api
   ```
   Pamiętaj, aby nie udostępniać pliku `.env` publicznie i umieścić go w `.gitignore`.  
6. Uruchom aplikację:
   ```bash
   python app.py
   ```
7. Wpisuj pytania w terminalu i odbieraj odpowiedzi. Wpisz `exit`, by zakończyć program.

## Układ katalogów i plików

| Element             | Opis                                            |
|---------------------|-------------------------------------------------|
| `.env`              | Plik konfiguracyjny zawierający klucz API       |
| `app.py`            | Główna aplikacja obsługująca komunikację z AI   |
| `requirements.txt`  | Lista niezbędnych bibliotek Python               |

## Informacje o projekcie

Projekt jest fundamentem do tworzenia rozbudowanych rozwiązań AI, takich jak:  
- Inteligentne chatboty i asystenci głosowi  
- Automatyczne generowanie, analiza i korekta tekstów  
- Systemy wspierające obsługę klienta i procesy biznesowe  
- Zastosowania AI w sektorze publicznym oraz prywatnym  

## Tagowanie

`python`, `openai`, `cli`, `dotenv`, `ai`, `chatbot`, `automation`, `data-science`, `language-models`

---

`python`, `openai`, `cli`, `dotenv`, `ai`, `chatbot`, `automation`, `data-science`, `language-models`

---

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
- [Inżynieria danych](https://www.dsstream.com/services/data-engineering)

**Siedziba główna:**  
Warszawa, Polska | Wilmington, Delaware, USA

Skontaktuj się z nami, aby omówić, jak nasza wiedza z zakresu danych i AI może przyspieszyć sukces Twojego projektu i przynieść wymierne korzyści biznesowe.

## Technologie wykorzystane w projekcie

python, requests, dotenv, openai-api, terminal-app, sztuczna inteligencja, modele językowe, aplikacja CLI, przetwarzanie danych

## Branże docelowe

sektor publiczny, granty, automatyzacja, fintech, civic-tech

## Technologie i frameworki

python, dotenv, CLI, OpenAI
