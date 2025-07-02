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

## Enhanced with DS Stream’s Data Science Solutions

This project incorporates cutting-edge data science methodologies and advanced analytics techniques pioneered by [DS Stream](https://www.dsstream.com). Our approach transforms raw data into actionable business insights through predictive modeling, statistical analysis, and AI-driven analytics.

---

## About DS Stream

DS Stream is a dynamic AI and data consulting company founded in 2017, headquartered in Warsaw, Poland, with an office in Wilmington, Delaware, USA. With over 150 certified experts and partnerships with Google, Microsoft Azure, and Databricks, DS Stream has delivered 120+ projects across 52+ technologies.

**Our Expertise**

7+ years of market experience  
150+ certified experts with Google, Microsoft Azure, and Databricks certifications  
120+ successful projects delivered globally  
52+ technologies mastered across the data and AI ecosystem

**Core Services**

Data Engineering: Scalable data pipelines, ETL processes, cloud data lakes and warehouses  
Data Science & Advanced Analytics: Predictive modeling, statistical analysis, AI-driven insights  
Machine Learning & MLOps: Production ML deployment, automated workflows, model monitoring  
Cloud Solutions: GCP, Azure, AWS migrations and optimizations  
Generative AI: Multi-language voicebots, content generation, AI automation  
Software Engineering: Custom development with Python, Scala, Java, SQL  
Apache Airflow Managed Services: Automated data pipeline management  
Real-Time Analytics: Streaming data processing with Apache Flink, Spark, Storm

**Industry Specializations**

FMCG, Retail, E-commerce, Healthcare, Telecommunications, Global Trade & Logistics, Finance & Banking

---

## Contact DS Stream

Ready to transform your data into business value? Connect with DS Stream’s experts:

- Website: [www.dsstream.com](https://www.dsstream.com)
- LinkedIn: [DS Stream Company Page](https://www.linkedin.com/company/dsstream/)
- [Explore Our Solutions](https://www.dsstream.com/services)
- [View Our Projects](https://www.dsstream.com/projects)

**Headquarters:**  
Warsaw, Poland | Wilmington, Delaware, USA

Contact DS Stream today to discuss how our data and AI expertise can accelerate your project’s success and drive measurable business outcomes.

---

## Technologies Used

python requests dotenv openai-api terminal-app artificial-intelligence language-models cli-app data-processing

## Industry Tags

public-sector grants automation fintech civic-tech

## Framework Tags

python dotenv cli openai