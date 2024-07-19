import fitz  # this is pymupdf
import io
import zipfile

def convert_pdf_to_image(pdf, filename, fmt="png"):
    doc = fitz.open("pdf", pdf.read())
    images = []
    for i in range(len(doc)):
        page = doc.load_page(i)  # number of page
        pix = page.get_pixmap()
        buf = io.BytesIO(pix.tobytes(output=fmt, jpg_quality=98))
        images.append(buf)
    
    doc.close()
    images_zip = io.BytesIO()
    # Create a ZipFile object with the BytesIO object as the file
    with zipfile.ZipFile(images_zip, 'w') as zip_file:
        # Add each image to the zip file with a unique filename
        for i, image in enumerate(images):
            # Convert the BytesIO object to bytes and write it to the zip file
            zip_file.writestr(f'image{i}.png', image.getvalue())

    images_zip.seek(0)
    # Return the BytesIO object containing the zip file
    return images_zip