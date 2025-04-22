from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import io
import os

from utils.ocr import extract_text  # Import from ocr.py

app = FastAPI()

@app.post("/extract-text/")
async def extract_text_from_upload(file: UploadFile = File(...)):
    """
    Endpoint to receive an image file and return extracted text using OCR.
    """
    try:
        # Read the uploaded file into memory
        contents = await file.read()

        # Open the image using Pillow
        image = Image.open(io.BytesIO(contents))

        # Save the uploaded image temporarily
        temp_path = "uploaded_image.png"
        image.save(temp_path)

        # Use the reusable OCR function
        text = extract_text(temp_path)

        # Remove the temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)

        return JSONResponse(content={"text": text})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
