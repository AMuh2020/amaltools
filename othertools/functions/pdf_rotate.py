from pypdf import PdfReader, PdfWriter
import io

# def rotate_pdf(input_pdf_path, output_pdf_path, rotation_angle):
#     pdf_in = open(input_pdf_path, 'rb')
#     pdf_reader = PdfReader(pdf_in)
#     pdf_writer = PdfWriter()
    
#     for pagenum in range(pdf_reader._get_num_pages()):
#         page = pdf_reader.pages[pagenum]

#         pdf_writer.add_page(page)
#         pdf_writer.pages[pagenum].rotate(rotation_angle)

#     with open(output_pdf_path, 'wb') as pdf_out:
#         pdf_writer.write(pdf_out)

#     pdf_in.close()

def rotate_pdf(pdf, rotation_angle):
    pdf_reader = PdfReader(pdf)
    pdf_writer = PdfWriter()
    
    for pagenum in range(pdf_reader._get_num_pages()):
        page = pdf_reader.pages[pagenum]

        pdf_writer.add_page(page)
        pdf_writer.pages[pagenum].rotate(int(rotation_angle))


    pdf_out = io.BytesIO()
    pdf_writer.write(pdf_out)

    pdf_out.seek(0)
    return pdf_out


