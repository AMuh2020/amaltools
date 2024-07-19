from pypdf import PdfMerger
import io

def merge_pdfs(pdfs):
    merger = PdfMerger()

    for pdf in pdfs:
        # print(pdf)
        merger.append(pdf)

    buf = io.BytesIO()
    merger.write(buf)
    merger.close()
    buf.seek(0)
    return buf

