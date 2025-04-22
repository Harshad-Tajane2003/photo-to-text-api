#  Photo to Text Generator API

A simple API to extract text from images using FastAPI, Pillow, and pytesseract.

---

##  Requirements

- Python 3.10+
- Tesseract-OCR installed (https://github.com/tesseract-ocr/tesseract)
- pip packages from `requirements.txt`

---

##  Project Structure
Photo_to_Text_api/ 
│ 
├── main.py 
├── utils/ 
│ └── ocr.py 
├── static/ 
├── requirements.txt 
└── README.md

##  How to Run

```bash
uvicorn main:app --reload


You are only using:
1) FastAPI – for the web API
2) Pytesseract – for OCR (text extraction)
3) PIL (Pillow) – for image processing
4) Uvicorn – for running the API