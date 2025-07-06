import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_gemini(prompt: str, image: bytes) -> str:
    try :
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content([
            prompt,
            {"mime_type": "image/jpeg", "data": image}
        ])
        return response.text
    except Exception as e :
        print ("ASK_GEMIN ERROR :" , e)
        return "GAGAL MENGHASILKAN DESKRIPSI GAMBAR"
