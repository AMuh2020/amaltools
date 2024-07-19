from django.shortcuts import render
from .functions import audio_extract, csv_tsv, pdf_image#, pdf_audiobook, selenium_vid_extractor_embed,
import base64
from django.core.files.base import ContentFile
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect
import os
import re
import urllib.parse 

# Create your views here.
def mp4_mp3(request):
    library_reference = {
        "name": "moviepy",
        "link": "https://github.com/Zulko/moviepy",
    }
    if request.method == "POST":
        file = request.FILES['file']
        #print(file[:3])
        mp3 = audio_extract.mp4TOmp3(file)
        mp3_file_name = file.name.split('.')[0] + ".mp3"
        print(mp3_file_name)
        #print(fnUrl)
        return FileResponse(mp3, as_attachment=True, filename=mp3_file_name)
    return render(request,"fileconverters/mp4_mp3.html",{"library_reference":library_reference})

# needs to be worked on
def svg_to_png(request):
    library_reference = {
        "name": "matplotlib",
        "link": "https://matplotlib.org/",
    }
    if request.method == "POST":
        file = request.FILES['file']
        pass
        
def vid_extractor(request):
    library_reference = {
        "name": "Selenium",
        "link": "https://www.selenium.dev/",
    }
    if request.method == "POST":
        url = request.POST['url']
        vid_src = selenium_vid_extractor_embed.get_vid_src(url)
        return render(request,"fileconverters/vid_extractor.html",{"vid_src":vid_src,"library_reference":library_reference})
    return render(request,"fileconverters/vid_extractor.html",{"library_reference":library_reference})

def csv_tsv_view(request):
    if request.method == "POST":
        file = request.FILES['file']
        file_name = file.name.split('.')[0]
        # print(file_name)
        if request.POST['direction'] == "csv_to_tsv":
            output = csv_tsv.csv_to_tsv(file)
            file_name += ".tsv"
            return FileResponse(output, as_attachment=True, filename=file_name)
        elif request.POST['direction'] == "tsv_to_csv":
            output = csv_tsv.tsv_to_csv(file)
            file_name += ".csv"
            return FileResponse(output, as_attachment=True, filename=file_name)
    return render(request,"fileconverters/csv_tsv.html")

# import io
# def test(request):
#     b = io.BytesIO()
#     with open(r"","rb") as file:
#         for chunk in file:
#             b.write(chunk)

#     b.seek(0)
#     return FileResponse(b,as_attachment="True",filename="test_through.jpg")

# needs more work
# def pdf_to_audiobook_view(request):
#     library_reference = {
#         "name": "",
#         "link": "",
#     }
#     if request.method == "POST":
#         file = request.FILES['file']
#         file_name = file.name.split('.')[0] + ".mp3"
#         print(file_name)
#         mp3_file = pdf_audiobook.pdf_to_audio(file,file_name)
#         return FileResponse(mp3_file, as_attachment=True, filename=file_name)
#     # create the template
#     return render(request,"",{"library_reference":library_reference})

def pdf_image_view(request):
    library_reference = {
        "name": "pymupdf",
        "link": ""
    }
    if request.method == "POST":
        file = request.FILES['pdf']
        file_name = file.name.split('.')[0]
        print(file_name)
        images = pdf_image.convert_pdf_to_image(file,file_name, fmt="png")
        print(images)
        return FileResponse(images, as_attachment=True, filename=file_name + ".zip")
    return render(request,"fileconverters/pdf_image.html",{"library_reference":library_reference})