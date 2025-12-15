import streamlit as st
import google.generativeai as genai
import PyPDF2
import os
from dotenv import load_dotenv

# Load Environment Variables (Local testing ke liye)
load_dotenv()

# Page Config
st.set_page_config(page_title="Adhikar-AI", page_icon="🇮🇳")
st.title("🇮🇳 Adhikar-AI")
st.subheader("Aapka Personal Legal Assistant (Powered by Gemini)")

# --- API KEY SETUP ---
# Hum check karenge ki key kahan hai (Local .env me ya Cloud Secrets me)
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    # Agar .env me nahi mili, to Streamlit Cloud secrets check karo
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except:
        st.error("🔑 API Key nahi mili! Setup required.")
        st.stop()

# Gemini Configure karein
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Tabs
tab1, tab2, tab3 = st.tabs(["💰 Sarkari Yojna", "⚖️ Pocket Vakeel", "👁️ Notice Reader"])

# --- TAB 1: SCHEMES ---
with tab1:
    st.header("Sarkari Yojna Finder")
    st.info("Coming Soon...")

# --- TAB 2: LEGAL ADVISOR (REAL AI) ---
with tab2:
    st.header("Pocket Vakeel (Legal Advisor)")
    st.write("Apni pareshani batayein, AI Wakeel turant salah dega.")
    
    user_query = st.text_area("Sawal likhein:", placeholder="Mera shopkeeper fridge wapas nahi le raha...")
    
    if st.button("Salah Lein"):
        if not user_query:
            st.error("Kripya pehle apna sawal likhein.")
        else:
            with st.spinner("Gemini Wakeel soch raha hai..."):
                try:
                    # AI ko prompt bhejein
                    prompt = f"""
                    You are an expert Indian Legal Advisor named 'Adhikar-AI'. 
                    User Query: {user_query}
                    
                    Please provide advice in simple Hinglish (Hindi + English mix).
                    Structure your answer:
                    1. Identify the relevant Law/Act (e.g., Consumer Protection Act).
                    2. Simple steps the user should take immediately.
                    3. Where to complain (Portal names/Links).
                    Keep it short, practical, and empathetic.
                    """
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")

# --- TAB 3: NOTICE READER (REAL AI SUMMARY) ---
with tab3:
    st.header("🔍 Mushkil Notice Padhein")
    uploaded_file = st.file_uploader("Apna PDF Notice upload karein", type="pdf")
    
    if uploaded_file is not None:
        try:
            # 1. Read PDF
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            
            with st.expander("📄 Asli Notice Text Dekhein"):
                st.write(text)
            
            # 2. Explain with AI
            if st.button("Iska Matlab Samjhao"):
                with st.spinner("Notice padh raha hoon..."):
                    prompt = f"""
                    Analyze this legal document text:
                    {text[:4000]} (Text truncated for safety)
                    
                    Explain this in simple Hinglish bullet points:
                    1. Who sent this?
                    2. What is the main accusation/demand?
                    3. What should the user do next?
                    """
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                    
        except Exception as e:
            st.error(f"Error reading PDF: {e}")