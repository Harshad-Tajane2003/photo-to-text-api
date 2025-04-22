from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from PIL import Image, ImageEnhance
import pytesseract
import shutil
import os
import uuid

app = FastAPI()

# Tell pytesseract where Tesseract-OCR is installed (update path if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Create uploads directory if it doesn't exist
UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# API Endpoint: Extract text from uploaded image
@app.post("/extract-text/")
async def extract_text(
    image: UploadFile = File(...), 
    language: str = Form("eng")  # Default language is English
):
    try:
        # Step 1: Save uploaded image to temporary file
        file_ext = image.filename.split('.')[-1]
        temp_filename = f"{uuid.uuid4()}.{file_ext}"
        temp_path = os.path.join(UPLOAD_DIR, temp_filename)

        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        # Step 2: Open the uploaded image
        img = Image.open(temp_path)

        # Step 3: Preprocess image (convert to grayscale and enhance contrast)
        img = img.convert("L")  # Convert to grayscale
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2.0)  # Increase contrast (try values from 1.5 to 3.0)

        # Step 4: Run OCR with specified language
        extracted_text = pytesseract.image_to_string(img, lang=language)

        # Step 5: Delete the temporary image file
        os.remove(temp_path)

        # Step 6: Return the extracted text as JSON response
        return JSONResponse(content={"extracted_text": extracted_text})
    
    except Exception as e:
        # Handle any error that occurs during the process
        return JSONResponse(status_code=500, content={"error": str(e)})
