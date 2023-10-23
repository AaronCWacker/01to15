import streamlit as st
import json
import pandas as pd
import streamlit.components.v1 as components

# Function to load JSONL file into a DataFrame
def load_jsonl(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return pd.DataFrame(data)

# Function to filter DataFrame by keyword
def filter_by_keyword(df, keyword):
    return df[df.apply(lambda row: row.astype(str).str.contains(keyword).any(), axis=1)]

# Function to generate HTML with textarea
def generate_html_with_textarea(text_to_speak):
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Read It Aloud</title>
        <script type="text/javascript">
            function readAloud() {{
                const text = document.getElementById("textArea").value;
                const speech = new SpeechSynthesisUtterance(text);
                window.speechSynthesis.speak(speech);
            }}
        </script>
    </head>
    <body>
        <h1>🔊 Read It Aloud</h1>
        <textarea id="textArea" rows="10" cols="80">
    {text_to_speak}
        </textarea>
        <br>
        <button onclick="readAloud()">🔊 Read Aloud</button>
    </body>
    </html>
    '''

# Streamlit App 🚀
st.title("USMLE Medical Questions Explorer with Speech Synthesis 🎙")

# Dropdown for file selection
file_option = st.selectbox("Select file:", ["usmle_16.2MB.jsonl", "usmle_2.08MB.jsonl"])
st.write(f"You selected: {file_option}")

# Load data
large_data = load_jsonl("usmle_16.2MB.jsonl")
small_data = load_jsonl("usmle_2.08MB.jsonl")

data = large_data if file_option == "usmle_16.2MB.jsonl" else small_data

# Top 20 healthcare terms for USMLE
top_20_terms = ['Heart', 'Lung', 'Pain', 'Memory', 'Kidney', 'Diabetes', 'Cancer', 'Infection', 'Virus', 'Bacteria', 'Neurology', 'Psychiatry', 'Gastrointestinal', 'Pediatrics', 'Oncology', 'Skin', 'Blood', 'Surgery', 'Epidemiology', 'Genetics']

# Create Expander and Columns UI for terms
with st.expander("Search by Common Terms 📚"):
    cols = st.columns(4)
    for term in top_20_terms:
        with cols[top_20_terms.index(term) % 4]:
            if st.button(f"{term}"):
                filtered_data = filter_by_keyword(data, term)
                st.write(f"Filtered Dataset by '{term}' 📊")
                st.dataframe(filtered_data)
                if not filtered_data.empty:
                    html_blocks = []
                    for idx, row in filtered_data.iterrows():
                        question_text = row.get("question", "No question field")
                        documentHTML5 = generate_html_with_textarea(question_text)
                        html_blocks.append(documentHTML5)
                    all_html = ''.join(html_blocks)
                    components.html(all_html, width=1280, height=1024)

# Text input for search keyword
search_keyword = st.text_input("Or, enter a keyword to filter data:")
if st.button("Search 🕵️‍♀️"):
    filtered_data = filter_by_keyword(data, search_keyword)
    st.write(f"Filtered Dataset by '{search_keyword}' 📊")
    st.dataframe(filtered_data)
    if not filtered_data.empty:
        html_blocks = []
        for idx, row in filtered_data.iterrows():
            question_text = row.get("question", "No question field")
            documentHTML5 = generate_html_with_textarea(question_text)
            html_blocks.append(documentHTML5)
        all_html = ''.join(html_blocks)
        components.html(all_html, width=1280, height=1024)



# Inject HTML5 and JavaScript for styling
st.markdown("""
<style>
    .big-font {
        font-size:24px !important;
    }
</style>
""", unsafe_allow_html=True)

# Markdown and emojis for the case presentation
st.markdown("# 🏥 Case Study: 32-year-old Woman's Wellness Check")
st.markdown("## 📋 Patient Information")
st.markdown("""
- **Age**: 32
- **Gender**: Female
- **Past Medical History**: Asthma, Hypertension, Anxiety
- **Current Medications**: Albuterol, Fluticasone, Hydrochlorothiazide, Lisinopril, Fexofenadine
- **Vitals**
  - **Temperature**: 99.5°F (37.5°C)
  - **Blood Pressure**: 165/95 mmHg
  - **Pulse**: 70/min
  - **Respirations**: 15/min
  - **Oxygen Saturation**: 98% on room air
""")

# Clinical Findings
st.markdown("## 📋 Clinical Findings")
st.markdown("""
- Cardiac exam reveals a S1 and S2 heart sound with a normal rate.
- Pulmonary exam is clear to auscultation bilaterally with good air movement.
- Abdominal exam reveals a bruit, normoactive bowel sounds, and an audible borborygmus.
- Neurological exam reveals cranial nerves II-XII as grossly intact with normal strength and reflexes in the upper and lower extremities.
""")

# Next Step Options
st.markdown("## 🤔 What is the best next step in management?")

# Multiple Choice
options = ["Blood Test", "MRI Scan", "Ultrasound with Doppler", "Immediate Surgery"]
choice = st.selectbox("", options)

# Explanation
if st.button("Submit"):
    if choice == "Ultrasound with Doppler":
        st.success("Correct! 🎉")
        st.markdown("""
        ### Explanation
        The patient's high blood pressure coupled with an abdominal bruit suggests the possibility of renal artery stenosis.
        An **Ultrasound with Doppler** is the best next step for assessing blood flow and evaluating for renal artery stenosis.
        """)
    else:
        st.error("Incorrect. 😞")
        st.markdown("""
        The best next step is **Ultrasound with Doppler**.
        """)
