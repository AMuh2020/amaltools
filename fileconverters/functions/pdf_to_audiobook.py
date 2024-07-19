import pyttsx3
import pypdf
from io import BytesIO
import os

# https://pypi.org/project/pyffmpeg/
# https://pypi.org/project/pyttsx3/
# https://pypi.org/project/pypdf/
def pdf_to_audio(pdf_file,file_name):
    engine = pyttsx3.init()
    audio = engine.getProperty('voices')
    engine.setProperty('voice', audio[1].id)
    byte = BytesIO()
    arr = []
    with pdf_file as book:
        # check this out
        reader = pypdf.PdfReader(book)

        for page in reader.pages:
            text = page.extract_text()
            text = text.replace('\n', '')
            arr.append(text)
    print(arr)
    # os path to directory of this file

    path_file = os.path.dirname(os.path.abspath(__file__))
    path = os.getcwd() + '/fileconverters/store_temp/' + file_name + ".mp3"
    engine.save_to_file(arr, path)
    print(path)
    engine.runAndWait()
    
    with open(path,"rb") as file:
        byte.write(file.read())
    # error check
    byte.seek(0)
    try:
        os.remove(path)
    except:
        print("file not deleted")

    # return byte stream
    return byte
    # possible extension is to add documents as well as pdfs

# file path to parent of current file directory


# stor = BytesIO()
# with open(r'C:\Users\leasu\Desktop\programming\workspace\web\WebTools\amaltools_app\fileconverters\store_temp\no_man_is_an_island.pdf', 'rb') as file:
#     stor.write(file.read())
#     stor.seek(0)
# pdf_to_audio(stor,'1')