# import pyttsx3
# import pypdf
# from io import BytesIO
# import os

# # https://pypi.org/project/pyffmpeg/
# # https://pypi.org/project/pyttsx3/
# # https://pypi.org/project/pypdf/
# def pdf_to_audio(pdf_file,filename):
#     fn = filename + ".mp3"
#     engine = pyttsx3.init()
#     audio = engine.getProperty('voices')
#     engine.setProperty('voice', audio[1].id)
#     arr = []
#     with open(pdf_file, 'rb') as book:
#         reader = pypdf.PdfReader(book)
        
#         for page in reader.pages:
#             text = page.extract_text()
#             text = text.replace('\n', '')
#             arr.append(text)
#     print(arr)
#     engine.save_to_file(arr, )

#     engine.runAndWait()
#     byte = BytesIO
#     with open(fn,"rb") as file:
#         byte.write(file.read())

#     try:
#         os.remove(fn)
#     except:
#         print("file not deleted")
#     byte.seek(0)
#     return byte