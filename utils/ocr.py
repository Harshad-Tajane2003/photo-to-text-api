from PIL import Image
import pytesseract

# Set your Tesseract path here (VERY IMPORTANT for Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path: str) -> str:
    """
    Reads an image from a given path and returns the extracted text.
    """
    try:
        image = Image.open(image_path)  # Open the image
        text = pytesseract.image_to_string(image)  # OCR: extract text
        return text
    except Exception as e:
        return f"Error processing image: {e}"
