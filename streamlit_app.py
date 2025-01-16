import streamlit as st
from pathlib import Path

st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)

def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'Test.pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)

left, right = st.columns([3,3], gap="medium")

left, right = st.columns(2)

with right:

    st.markdown("""
                <h3>David Lecjaks</h3>
                <br>
                <p>Ich bin davon überzeugt, dass Ki die Welt verändern wird.
                und ich möchte ein Teil davon sein.</em>
                """, unsafe_allow_html=True)

st.download_button(
            label="📄 Download Lebenslauf",
            data=file_bytes,
            file_name=file_path,
            mime='application/pdf'
        )

st.write("lecjaksdavid@gmail.com")


right.write("")

right.write("*Ich finde It faszienirend, weil es die Zukunft beeinflusst*")

st.header("IT-Kompetenzen",anchor=False, divider="blue")
st.markdown("""
            - Webentwicklung: Grundlagen in HTML, CSS und Streamlit (Fullstack-Framework)
            -  Programmierung: Anfänger in  Python, Entwicklung kleiner Anwendungen und Skripte
            -  Office-Suite: Umgang mit Microsoft Word, Excel und PowerPoint
            """)
st.header("Schulbildung",anchor=False,divider="blue")





st.header("Arbeitserfahrung",anchor=False,divider="blue")
st.markdown("""
         -Berufspraktische Tage 1: Beim Augenarzt  von 18. bis 22. Nov. 2024   
         -Berufspraktische Tage 2: Bei XYZ von 24. bis 28. Feb. 2025
            """)

st.header("Zusätzliche Qualifikationen",anchor=False,divider="blue")
st.markdown("""
        - Schnelle Auffassungsgabe für neue Softwareanwendungen und Technologien
        - Großes Interesse an der kontinuierlichen Weiterentwicklung im IT-Bereich
        - Teamfähigkeit und Kommunikationsstärke bei gemeinsamen Coding-Projekten    
            """)

st.header("Interessen und Hobbys",anchor=False,divider="blue")
st.markdown("""
        - Ich spiele gerne Basketball mit freunden   
            """)










