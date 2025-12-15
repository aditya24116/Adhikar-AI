import streamlit as st
import time
import PyPDF2  # PDF padhne wala tool

# Page Config
st.set_page_config(page_title="Adhikar-AI", page_icon="🇮🇳")
st.title("🇮🇳 Adhikar-AI")
st.subheader("Na Notice ka darr, na Scheme ki chinta.")

# Tabs
tab1, tab2, tab3 = st.tabs(["💰 Sarkari Yojna", "⚖️ Pocket Vakeel", "👁️ Notice Reader"])

# --- TAB 1: SCHEMES ---
with tab1:
    st.header("Sarkari Yojna Finder")
    st.info("Coming Soon: Yahan aapko schemes milengi.")

# --- TAB 2: LEGAL ADVISOR (SIMULATION) ---
with tab2:
    st.header("Pocket Vakeel (Legal Advisor)")
    st.write("Apni pareshani batayein (Hindi/English me).")
    
    user_query = st.text_area("Sawal likhein:", placeholder="Example: Mera landlord security deposit wapas nahi kar raha...")
    
    if st.button("Salah Lein (Get Advice)"):
        if not user_query:
            st.error("Kripya pehle apna sawal likhein.")
        else:
            with st.spinner("AI Wakeel soch raha hai... (Simulation Mode)"):
                time.sleep(2) # Fake wait
                st.success("Adhikar-AI ki Salah:")
                st.markdown(f"""
                **Samasya:** {user_query}
                
                **Kanooni Salah:**
                1.  Yeh mamla **Consumer Protection Act** ya **Rent Control Act** mein aata hai.
                2.  Sabse pehle ek **Legal Notice** bhejein.
                3.  Agar wo na maane, toh **Helpline 1915** par call karein.
                
                *Note: Yeh Demo Mode hai.*
                """)

# --- TAB 3: NOTICE READER (REAL PDF TOOL) ---
with tab3:
    st.header("🔍 Mushkil Notice Padhein")
    st.write("Koi bhi PDF file upload karein, main uska text nikal kar dikhaunga.")
    
    # File Upload Button
    uploaded_file = st.file_uploader("Apna PDF yahan upload karein", type="pdf")
    
    if uploaded_file is not None:
        # PDF Read karne ki koshish
        try:
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            
            # Saare pages se text nikalna
            for page in reader.pages:
                text += page.extract_text()
            
            st.success("✅ PDF Padh liya!")
            
            # Text dikhana
            st.subheader("PDF ke andar ye likha hai:")
            st.text_area("Extracted Text:", value=text, height=300)
            
            if st.button("Iska Matlab Samjhao"):
                st.info("Summary Feature abhi ban raha hai. Lekin upar diya gaya text asli PDF se nikala gaya hai!")
                
        except Exception as e:
            st.error(f"Error: {e}")