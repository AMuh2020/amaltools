from django.shortcuts import render
from django.http import FileResponse
from .functions import text_to_qr, ocr_tesseract, yt_to_x,plot, pdf_merger, pdf_rotate
import django.utils.datastructures
# from .tasks import yt_tool_task
import os
# Create your views here.

def word_count(request):
    return render(request,"othertools/word_count.html")

def qr_code(request):
    library_reference = {
        "name": "qrcode",
        "link": "https://github.com/lincolnloop/python-qrcode"
    }
    if request.method == "POST":
        text = request.POST["text"]
        settings = {
            "version": request.POST["version"],
            # options are L, M, Q, H
            "error_correction": request.POST["error_correction"],
            "box_size": request.POST["box_size"],
            "border": request.POST["border"],
            "fill_color": request.POST["fill_color"],
            "back_color": request.POST["back_color"],
        }
        print(settings)
        # variable stores the bytes for the image
        qr_image = text_to_qr.qr_code_function(text,settings)
        return render(request, "othertools/text_to_qr.html",{"qr_code":qr_image,"library_reference":library_reference})
    return render(request, "othertools/text_to_qr.html",{"library_reference":library_reference})

def ocr_view(request):
    library_reference = {
        "name": "pytesseract",
        "link": "https://github.com/tesseract-ocr/tesseract",
    }
    if request.method == "POST":
        file = request.FILES['file']
        text = ocr_tesseract.ocr_image(file)
        return render(request,"othertools/ocr.html",{"text":text,"library_reference":library_reference})
    return render(request,"othertools/ocr.html",{"library_reference":library_reference})

# extension of FileResponse to delete the file after it is sent
class FileCleanupResponse(FileResponse):
    def __init__(self, *args, file_to_delete_path, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_to_delete_path = file_to_delete_path
    
    def close(self):
        super().close()
        os.remove(self.file_to_delete_path)

# only works in production, no ffmpeg on local
def yt_to_x_view(request):
    library_reference = {
        "name": "youtube-dL",
        "link": "https://github.com/ytdl-org/youtube-dl",
    }
    if request.method == "POST":
        file_type = request.POST["type"]
        link = request.POST["yt_link"]
        quality = request.POST["quality"]
        if quality == "-":
            quality = "best"

        # using celery to run the task in the background, disabled for now
        # res = yt_tool_task.delay(link,file_type,quality)
        # fpath, filename = res.get()
        # print(filename)
        # request_finished.send(sender=yt_to_x_view, file_path=fpath)
        try:
            fpath, filename = yt_to_x.yt_download(link,file_type,quality)
        except Exception as e:
            return render(request,"othertools/yt_to_x.html",{"error_msg":"Error: There was an error accessing the video, please try a different video or check the link. (file size is limited to 100MB)"})

        return FileCleanupResponse(open(fpath,"rb"), as_attachment=True, filename=filename, file_to_delete_path=fpath)
    return render(request,"othertools/yt_to_x.html",{"library_reference":library_reference})

# uses matplotlib to create many types of graphs based on the users inputs
def plot_view(request):
    library_reference = {
        "name": "matplotlib",
        "link": "https://matplotlib.org/",
    }
    if request.method == "POST":
        plot_type = request.POST["graph_type"]
        try:
            show_grid_lines = request.POST["show_grid"]
            print(show_grid_lines)
        except django.utils.datastructures.MultiValueDictKeyError:
            show_grid_lines = False

        # x_axis_start = request.POST["x_axis_start"]
        # y_axis_start = request.POST["y_axis_start"]

        data = request.FILES["data"]
        b64_string = plot.plot_graph(data,plot_type=plot_type,grid_lines=show_grid_lines)
        return render(request,"othertools/graph_plotter.html",{"library_reference":library_reference,"b64":b64_string})


    return render(request,"othertools/graph_plotter.html",{"library_reference":library_reference})

# this tool is fully on the frontend
def paste_image(request):
    return render(request,"othertools/paste.html")

def pdf_merger_view(request):
    library_reference = {
        "name": "PyPDF2",
        "link": ""
    }
    if request.method == "POST":
        pdfs = request.FILES.getlist("pdfs")
        if len(pdfs) < 2:
            return render(request,"othertools/pdf_merger.html",{"error_msg":"Error: Please select at least 2 pdfs to merge."})
        
        output_filename = request.POST["output_filename"]
        if output_filename == "":
            output_filename = pdfs[0].name

        merged_pdf = pdf_merger.merge_pdfs(pdfs)
        return FileResponse(merged_pdf, as_attachment=True, filename=f"{output_filename}")
    return render(request,"othertools/pdf_merger.html",{"library_reference":library_reference})

# def time_tools(request):
#     return render(request,"othertools/unix_time_tools.html")

# def teleprompter(request):
#     return render(request,"othertools/teleprompter_tool_page.html")

# def teleprompter_scroller(request):
#     if request.method == "GET":
#         # get the text from the url
#         text = request.GET.get("text")
#         print(request.GET)
#         return render(request,"othertools/teleprompter.html",{"text":text})
    
def pdf_rotate_veiw(request):
    library_reference = {
        "name": "PyPDF2",
        "link": ""
    }
    if request.method == "POST":
        pdf = request.FILES["pdf"]
        rotation_angle = request.POST["rotation_angle"]
        rotated_pdf = pdf_rotate.rotate_pdf(pdf,rotation_angle)
        return FileResponse(rotated_pdf, as_attachment=True, filename=pdf.name)
    return render(request,"othertools/pdf_rotate.html",{"library_reference":library_reference})