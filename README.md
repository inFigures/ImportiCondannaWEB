
# Estrazione Dati da Sentenza PDF

Questo progetto utilizza **Streamlit**, **PyPDF2**, e **Google Generative AI** per estrarre e analizzare il contenuto di una sentenza in formato PDF. 
L'applicazione permette di estrarre il testo dal PDF, fare delle richieste al modello Gemini di Google per sintetizzare la sentenza e ottenere informazioni come i nomi dei condannati, gli importi della condanna e le spese di giustizia.

## Funzionalità

- **Estrazione testo**: L'applicazione estrae il testo da un file PDF di sentenza.
- **Sintesi**: Il modello genera una sintesi del contenuto della sentenza.
- **Nomi dei condannati**: Estrae i nomi dei condannati dalla sentenza.
- **Importo totale della condanna**: Estrae l'importo totale della condanna.
- **Spese di giustizia**: Estrae il valore delle spese di giustizia.
- **Condannati e importi**: Crea una lista dei condannati e dei rispettivi importi di condanna.
- **Tabella**: Mostra una tabella con i nomi dei condannati e gli importi di condanna estratti.

## Requisiti

Assicurati di avere Python 3.8+ installato. Puoi installare i seguenti pacchetti Python utilizzando `pip`:

```bash
pip install streamlit PyPDF2 pandas google-generativeai
```

## Come Usare

1. **Carica il PDF**: Carica il file PDF della sentenza cliccando sul pulsante "Carica una sentenza in PDF".
2. **Inserisci la tua API Key**: Per utilizzare il modello Gemini di Google, inserisci la tua chiave API nel campo "Inserisci la tua GEMINI API Key".
3. **Visualizza i Risultati**: Dopo aver caricato il PDF, l'applicazione estrarrà il testo dalla sentenza e mostrerà i risultati, inclusi:
   - Sintesi della sentenza.
   - Nomi dei condannati.
   - Importo totale della condanna.
   - Spese di giustizia.
   - Elenco condannati e importi con una tabella.

Se non desideri eseguire l'applicazione localmente, puoi anche utilizzare la versione online accessibile tramite il seguente link:

https://importi-condanna.streamlit.app/

## Esecuzione

Per avviare l'applicazione, esegui il seguente comando:

```bash
streamlit run main.py
```

Questo avvierà un server locale e potrai accedere all'applicazione nel tuo browser.

## Struttura del Codice

- **`estrai_contenuto(pdf_file)`**: Funzione per estrarre il testo da un file PDF.
- **`interroga_modello(prompt)`**: Funzione per inviare una richiesta al modello Gemini di Google per ottenere una risposta.
- **UI con Streamlit**: Interfaccia utente per caricare il PDF, inserire la chiave API, e visualizzare i risultati.
