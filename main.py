import streamlit as st
import PyPDF2
import pandas as pd
import google.generativeai as genai


# Funzione per estrarre il testo dal PDF
def estrai_contenuto(pdf_file):
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Funzione per interrogare il modello
@st.cache_data
def interroga_modello(prompt):
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = model.generate_content(prompt)
    return "".join(part.text for chunk in response for part in chunk.parts)

# UI con Streamlit
st.title("Estrazione dati da sentenza PDF")
api_key = st.text_input("Inserisci la tua GEMINI API Key:", type="password")
if api_key:
    genai.configure(api_key=api_key)           
else:
    st.warning("Inserisci la chiave API per continuare.")

caricato = st.file_uploader("Carica una sentenza in PDF", type=["pdf"])

if caricato:
    sentenza = estrai_contenuto(caricato)
    st.subheader("Testo estratto:")
    st.text_area("", sentenza, height=250)
    
    with st.spinner("Analizzando la sentenza..."):
        risultati = {
            "Sintesi": f"Sintetizza il contenuto di questa sentenza:\n\n{sentenza}",
            "Nomi condannati": f"Quali sono i nomi dei condannati di questa sentenza:\n\n{sentenza}",
            "Importo totale condanna": f"Questa è una sentenza. Rispondimi dicendomi qual è l'importo totale di condanna. Dammi solo il valore in euro e nulla più:\n\n{sentenza}",
            "Spese di giustizia": f"Questa è una sentenza. Rispondimi dicendomi qual è il valore complessivo delle spese di giustizia. Dammi solo il valore in euro e nulla più:\n\n{sentenza}",
            "Condannati e importi": f"La seguente sentenza identifica i nominativi dei condannati e relativi importi di condanna. Restituisci un elenco strutturato in formato 'Nome: Importo'. Testo: {sentenza}"
        }

        risultati_ottenuti = {k: interroga_modello(v) for k, v in risultati.items()}
        
        for titolo, contenuto in risultati_ottenuti.items():
            st.subheader(titolo)
            st.write(contenuto)
            
        # Creazione del DataFrame con nomi e importi
        data = {"nome condannato": [], "importo condanna": []}
        for line in risultati_ottenuti["Condannati e importi"].strip().split('\n'):
            try:
                nome, importo = line.split(':')
                data["nome condannato"].append(nome.strip())
                data["importo condanna"].append(importo.strip())
            except ValueError:
                continue
        
        if data["nome condannato"]:
            df = pd.DataFrame(data)
            st.subheader("Tabella Importi di Condanna")
            st.dataframe(df)
