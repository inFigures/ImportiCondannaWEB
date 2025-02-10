# Usa l'immagine ufficiale di Python
FROM python:3.10

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia i file di progetto
COPY . .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Esponi la porta per Streamlit
EXPOSE 8501

# Comando per avviare l'app Streamlit
CMD ["python", "-m", "streamlit", "run", "main.py"]
