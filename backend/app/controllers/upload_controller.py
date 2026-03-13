from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import extract_text
from app.utils.ai_client import generate_summary_and_quiz2  # version factice ou OpenAI
import os
import json

router = APIRouter()

# Crée le dossier temp si inexistant
if not os.path.exists("temp"):
    os.makedirs("temp")

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Vérifie le type de fichier
    if not file.filename.endswith(".pdf"):
        return {"error": "Seuls les fichiers PDF sont acceptés"}

    # Sauvegarde PDF
    file_location = f"temp/{file.filename}"
    contents = await file.read()  # async read
    with open(file_location, "wb") as f:
        f.write(contents)

    # Extraction texte
    text = extract_text(file_location)

    # Génération IA (ou factice)
    result_text = generate_summary_and_quiz2(text)

    # Essaye de parser JSON renvoyé par l'IA
    try:
        result = json.loads(result_text)
    except Exception:
        # Fallback si l'IA renvoie du texte brut
        result = {"summary": result_text, "quiz": []}

    return result