# 1. Uzycie obrazu Python
FROM python:3.10

# 2. Ustawienie katalogu roboczego wewnątrz kontenera
WORKDIR /app

# 3. Kopiowanie plików (bez .venv i zbednych [plikow])
COPY . /app/

# 4. Instalacja zaleznosci
RUN pip install --no-cache-dir -r requirements.txt

# 5. Otworzenie portu dla aplikacji
EXPOSE 8000

# 6. Ustawienie punktu wejscia dla kontenera
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
