from fastapi import UploadFile, File, APIRouter, HTTPException
from app.service.gemini_engine import ask_gemini
from app.models.chat import ChatResponse
import os

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def image_description(image: UploadFile = File(...)):
    try:
        contents = await image.read()
        caption = ask_gemini("Jelaskan isi gambar ini dalam Bahasa Indonesia.", image=contents)

        # Simpan gambar 
        uploud_file = "static/uploud"
        os.makedirs(uploud_file, exist_ok=True)
        file_path = os.path.join(uploud_file, image.filename)
        with open(file_path, "wb") as f:
            f.write(contents)

        # Untuk url Gambar
        img_url = f"/static/uploads/{image.filename}"

        return ChatResponse(question="Deskripsi Gambar :",
                            answer=f"{caption}",
                            img_url=img_url
                            )
    except Exception as e:
        print("UPLOAD ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))
