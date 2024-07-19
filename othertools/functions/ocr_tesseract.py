import pytesseract
from PIL import Image
from io import BytesIO
# donwload tesseract ubuntu
# extend by allowing psm and oem to be passed as parameters
def ocr_image(image_bytes):
    # Load the image from the BytesIO object
    with image_bytes as f:
        image = Image.open(f)

        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(image)

    # Return the OCR result
    return text