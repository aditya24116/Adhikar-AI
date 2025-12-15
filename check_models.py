import google.generativeai as genai
import os
from dotenv import load_dotenv

# Environment variables load karein
load_dotenv()

# API Key uthayein
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: API Key nahi mili! .env file check karein.")
else:
    print(f"✅ Key mil gayi: {api_key[:5]}... (Testing connection...)")
    
    try:
        genai.configure(api_key=api_key)
        
        print("\n🔍 Google ke paas ye Models available hain:")
        print("-" * 40)
        
        # Google se list maango
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"👉 {m.name}")
                
        print("-" * 40)
        print("✅ Jo naam '👉' ke aage likha hai, wahi app.py mein use karein.")
        
    except Exception as e:
        print(f"\n❌ Connection Error: {e}")