import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load keys
load_dotenv()
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
key = os.getenv("AZURE_OPENAI_API_KEY")
model = os.getenv("AZURE_DEPLOYMENT_NAME")

print(f"Testing Connection to: {endpoint}")
print(f"Model Name: {model}")

try:
    client = AzureOpenAI(
        azure_endpoint=endpoint, 
        api_key=key,  
        api_version="2024-02-15-preview"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Hello, are you working?"}],
        max_tokens=10
    )
    print("✅ SUCCESS! Reply from AI:", response.choices[0].message.content)

except Exception as e:
    print("❌ ERROR:", e)